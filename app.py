#!/usr/bin/env python3
# import RPi.GPIO as GPIO
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


# def setupGPIO():
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
# GPIO.setup(18, GPIO.OUT)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # setupGPIO()
    if request.method == 'POST':
        print("I am posting!")
        circulation_pump = request.form.get('circulation_pump')
        # if data == 'On':
        #     GPIO.output(18, GPIO.HIGH)
        # else:
        #     GPIO.output(18, GPIO.LOW)

        print("Circulation Pump is {}".format(circulation_pump))
    if request.method == 'GET':
        print("I am getting!!")

    return render_template("status.html")
