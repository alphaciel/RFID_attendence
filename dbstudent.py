#!/usr/bin/env python
# -*- coding: utf8 -*-
from __future__ import print_function
from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError
import sqlite3 as sql
import sys
app = Flask(__name__)


class ContactForm(Form):
    name = TextField("Name Of Student", [validators.Required("Please ente your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Org = TextAreaField("Organizations")

    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    Age = IntegerField("age")
    language = SelectField('Languages', choices=[('cpp', 'C++'),
                                                 ('py', 'Python')])
    submit = SubmitField("Send")
@app.route('/')
def home():
    return render_template('./home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():

    global msg

    if request.method == 'POST':
        try:

            nm = request.form['nm']

            email = request.form['email']

            org = request.form['org']

            nphone = request.form['nphone']

            ftrain = request.form['ftrain']

            tstudy = request.form['tstudy']

            dstudy = request.form['dstudy']
            
            gen = request.form['generation']

            rfid = request.form['rfid']
            msg = "Thank you successfully added"
                

            with sql.connect("student.db") as con:
                cur = con.cursor()

                con.execute("INSERT INTO STUDENTDAT (NAME, EMAIL,ORG, NPHONE,FTRAINNING ,TSTUDY , DSTUDY,GENERATION, RFID ) VALUES(?, ?, ?, ?,?,?,?,?,?)",(nm,email,org,nphone,ftrain,tstudy,dstudy,gen,rfid) )
                cur.execute("PRAGMA busy_timeout = 30000")
                con.commit()

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()




@app.route('/list')
def list():
    con = sql.connect("student.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from STUDENTDAT")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    cur = sql.connect("student.db")

    cur.execute("PRAGMA busy_timeout = 30000")
    app.run(debug=True, host= '0.0.0.0', port=1012)