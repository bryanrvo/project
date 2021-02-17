#!/usr/bin/env python3
from templates.python.phue import Bridge
import re
from PIL import ImageColor
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import requests
import time
import datetime
from rpi_ws281x import *
from templates.python.strandtesttesten import *
from templates.python.Sun import main
from templates.python.Telnet import *
import threading
import platform
import os
import sys

tn = ""
hue = Bridge('192.168.68.50')
hue.connect()
huestate = True
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, GPIO.PUD_DOWN)
app = Flask(__name__)
app.static_folder = 'static'
led_stripValue = ""
ambilightValue = ""
sensorValue = ""
strip = ""
test2 = ""
sunrise = ""
sunset = ""
length = ""
tijd_nu = ""
kleurenhtml = "rgb(255, 0, 0)"
state = "vullen"
newstate = ""
r, g, b = 0, 0, 0

def aansturing(self):
    global led_stripValue, ambilightValue
    global r,g,b
    global state
    global strip, strip2
    global tn
    while True:
        if led_stripValue == "checked":
            if state == "vullen":
                vullen(strip, Color(r,g,b))
                state = ""
            elif state == "ajax":
                ajax(strip)
                state = ""
            elif state == "ajaxscore":
                ajaxscore(strip)
                vullen(strip, Color(r,g,b))
            elif state == "Sparkle":
                Sparkle(strip, Color(r,g,b), 0)
            elif state == "DrawComet":
                DrawComet(strip, Color(r,g,b))
            elif state == "Twinkle":
                Twinkle(strip, Color(r,g,b), 40, 0.100, False)
            elif state == "TwinkleRandom":
                TwinkleRandom(strip, 50, 0.100, False)
            elif state == "NewKITT":
                NewKITT(strip, r, g, b, 20, 0.010, 0.050)
            elif state == "RunningLights":
                RunningLights(strip,r,g,b,0.05)
            elif state == "theaterChase":
                theaterChase(strip, Color(r,g,b))
            elif state == "theaterChaseRainbow":
                theaterChaseRainbow(strip)
            elif state == "FadeInOut":
                FadeInOut(strip, r, g, b)
            elif state == "Strobe":
                Strobe(strip, Color(r,g,b), 10, 0.050, 1)
            elif state == "HalloweenEyes":
                HalloweenEyes(strip, r,g,b, 12, 6, True, random.randint(5,50), random.randrange(0.050,0.150), random.randrange(1, 10))
            elif state == "CylonBounce":
                CylonBounce(strip, r,g,b, 13, 0.010, 0.050)
            elif state == "rainbowCycle":
                rainbowCycle(strip)
            elif state == "BouncingBalls":
                a = [[255,0,0],[0,255,0],[0,0,255]]
                BouncingBalls(strip, a, 3, 67)
            elif state == "colorWipe":
                colorWipe(strip, Color(r,g,b))
            elif state == "rainbow":
                rainbow(strip)
        else:
            vullen(strip, Color(0,0,0))
        if ambilightValue == "checked":
            print(tn)
            if state == "":
                start_time = datetime.datetime.now()
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                if  execution_time > 3000:
                    setColor(tn, r, g, b)

        


def run(self):
    while True:
        global sunrise
        global sunset
        global length
        global led_stripValue
        global sensorValue
        global r , g, b, state
        global hue, huestate
        time_now = datetime.datetime.now().time()
        tijd_nu = time_now.strftime("%H:%M:%S")
        led_stopt = datetime.time(1, 30, 10)
        led_stop = led_stopt.strftime("%H:%M:%S")
        sunrise, sunset, length = main(1,1,1)
        if tijd_nu == sunset:
            ping(0)
        if tijd_nu == led_stop:
            led_stripValue = ""
            sensorValue = ""
            hue.set_light('Led strip boven','on', False)
            huestate = False
        if hue.get_light('Led strip boven', 'on') == True and huestate == False:
            r = 50
            g = 50
            b = 50
            stoppen(0)
            state == "vullen"
            huestate = True
            sensorValue = "checked"
            led_stripValue = "checked"
        if hue.get_light('Led strip boven', 'on') == False and huestate == True:
            stoppen(1)
            huestate = False
            sensorValue = ""
            led_stripValue = ""

def ping(light_on):
    hostname = "192.168.68.66"
    global led_stripValue
    global sensorValue
    global state
    global strip
    global r , g, b
    global hue, huestate
    y = 1
    while y <= 6:
        if light_on == 0:
            response = os.system("ping -c 1 " + hostname)
            if response == 0:
                light_on = 1
                if hue.get_light('Led strip boven', 'on') == False:
                    huestate = True
                    hue.set_light('Led strip boven','on', True)
                sensorValue = "checked"
                led_stripValue = "checked"
        y +=1

def callback(pin):
    global led_stripValue
    global sensorValue
    global state
    global strip
    global r , g, b
    global hue, huestate
    if sensorValue == "checked":
        if led_stripValue == "":
            led_stripValue = "checked"
            if state != "vullen":
                state = "vullen"
        elif led_stripValue == "checked":
            led_stripValue = ""

thread1 = threading.Thread(target=run, args=(1,))
thread1.daemon = True
thread1.start()


def setup():
    global strip
    LED_COUNT      = 298      # Number of LED pixels.
    LED_PIN        = 13      # G  PIO pin connected to the pixels (18 uses PWM!).
    #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    thread2 = threading.Thread(target=aansturing, args=(1,))
    thread2.daemon = True
    thread2.start()

#start standaart html
@app.route('/', methods=["POST", "GET"])
@app.route("/power", methods=["POST", "GET"])
def power():
    global led_stripValue
    global ambilightValue
    global sensorValue
    global strip
    global r , g, b
    global state
    global hue, huestate
    global tn
    if request.method == 'POST':
        led_strip = request.form.get('led_strip')
        ambilight = request.form.get('ambilight')
        sensor = request.form.get('sensor')
#         led_strip = request.form['led_strip']
#         ambilight = request.form['ambilight']
#         sensor = request.form['sensor']
        if led_strip == 'led strip' and led_stripValue == "":
            stoppen(0)
            if huestate == False:
                huestate = True
                hue.set_light('Led strip boven','on', True)
            led_stripValue = "checked"
            time.sleep(2)
            state = "vullen"
        elif led_strip == None and led_stripValue == "checked":
            led_stripValue = ""
            stoppen(1)
        elif led_strip == "None" and led_stripValue == "checked":
            stoppen(1)
            led_stripValue = ""
        if ambilight == 'ambilight' and ambilightValue == "":
            tn = connect('192.168.68.74', '3636')
            time.sleep(8)
            ambilightValue = "checked"
        elif ambilight == None and ambilightValue == "checked":
            ambilightValue = ""
            disconnect(tn)
        if sensor == 'sensor' and sensorValue == "":
            sensorValue = "checked"
        elif sensor == None and sensorValue == "checked":
            sensorValue = ""
        elif sensor == "None" and sensorValue == "checked":
            sensorValue = ""
    return render_template('power.html', led_stripValue=led_stripValue, ambilightValue=ambilightValue, sensorValue=sensorValue)

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

@app.route("/Sunset", methods=["POST", "GET"])
def Sunset():
    global sunset
    return render_template('sunset.html', sunset = sunset)

@app.route("/colorize", methods=["POST", "GET"])
def colorize():
    global led_stripValue
    global r , g, b
    global kleurenhtml
    global state
    global newstate
    if request.method == 'POST':
        kleur = request.form.get('color')
        newstate = request.form['test']
        if newstate != state:
            stoppen(1)
            state = newstate
        time.sleep(1)
        stoppen(0)
    return render_template('color.html', kleuren = kleurenhtml, state = newstate)

@app.route("/ditiskleur", methods=["POST"])
def ditiskleur():
    if request.method == 'POST':
        global strip
        global led_strip
        global r, g, b
        global kleurenhtml
        global state
        global strip
        oldr = r
        oldg = g
        oldb = b
        data = request.form['javascript_data']
        kleurenhtml = data
        data = data.replace('rgb(','')
        data = data.replace(')','')
        data = data.replace(" ","")
        r, g, b = data.split(",")
        r = int(r)
        g = int(g)
        b = int(b)
        if r > 180 and g > 180 and b > 180:
            r = r / 4
            g = g / 4
            b = b / 4
        elif r > 250 and  g < 30 and b < 30:
            r = 255
            g = 0
            b = 0
        elif r < 30 and  g > 250 and b < 30:
            r = 0
            g = 255
            b = 0
        elif r < 30 and  g < 30 and b > 250:
            r = 0
            g = 0
            b = 255
        elif r > 190 or g > 190 or b > 190:
            r = r / 2
            g = g / 2
            b = b / 2
        r = int(r)
        g = int(g)
        b = int(b)
        if led_stripValue == "checked":
            if oldr != r or oldg != g or oldb != b:
                stoppen(1)
                state = "vullen"
        else:
            vullen(strip, Color(0, 0, 0))
        return render_template('color.html')


GPIO.add_event_detect(10, GPIO.RISING, callback, bouncetime=300)

# start de server
if __name__ == '__main__':
    global led
    setup()
    app.run(host = '192.168.68.75', port = 3000)
    #vullen(strip, Color(r , g, b))


