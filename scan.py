#! /usr/bin/env python
# -*- coding: utf8 -*-
import MFRC522
import signal
import RPi.GPIO as GPIO
import time
import datetime
import sqlite3
from PyQt4.QtCore import *
import sys
from PyQt4.QtGui import *
from RFIDGUI import Ui_MainWindow
from luma.core.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

class LCD(object):
    def __init__(self):
        super(LCD, self).__init__()
        self.serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(serial, rotate=0)
    def write(self, name ,att):
        with canvas(self.device) as draw:
            if len(name) < 20:

                draw.text((10, 20), "Welome Arrowdot", fill="red")
                draw.text((10, 40), name,font='Ubuntu')
                draw.co


class dataControl():
    def __init__(self, rfid):
        super(dataControl, self).__init__()
        self.con = sqlite3.connect("student.db",timeout=1)
        self.cur = self.con.cursor()
        self.rfid = rfid

    def send_rfid(self):
      ddate = str(datetime.datetime.now().date())
      dtime = str(datetime.datetime.now().time())

      self.cur.execute("INSERT TABLE ATT(DATE, TIME, RFID, NAME, ATTENDANCE)\
              VALUES(%s, %s,%s ,%s, %d)(?,?,?,?,?)"%(ddate, dtime, rfid,  name,  1))

    def compare_name(self,rfid):
        #FIX THIS First

        self.cur.execute("SELECT STUDENTDAT FROM list WHERE RFID=?", (rfid,))
        a = 0
        return
class RFID(object):
    led_g = 11
    led_r = 13
    buz = 15
    def __init__(self):
        super(RFID, self).__init__()
        self.MReader = MFRC522.MFRC522()
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUdT)
        signal.signal(signal.SIGINT, self.end_read)

    def end_read(self, frame):

        print "Ctrl+C captured, ending read."
        GPIO.cleanup()
        return False

    def run(self):
        while (not(self.end_read)):

            # Scan for cards
            (status, TagType) = self.MReader.MFRC522_Request(self.MReader.PICC_REQIDL)

            # If a card is found
            if status == self.MReader.MI_OK:
                print "Card detected"

            # Get the UID of the card
            (status, uid) = self.MReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == self.MReader.MI_OK:
                # Print UID
                uidF = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
                return uidF


def main():
    "something"
if __name__ == '__main__':
  main()



