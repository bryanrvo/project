#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
import random
import math
import datetime
import numpy as np


# LED strip configuration:
LED_COUNT      = 298      # Number of LED pixels.
LED_PIN        = 18      # G  PIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

stopdef = 0

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    global stopdef
    vullen(strip,Color(0,0,0))
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        if stopdef == 1:
            return
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        if stopdef == 1:
            return
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        if stopdef == 1:
            return
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        if stopdef == 1:
            return
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        if stopdef == 1:
            return
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def driekleuren(strip, color):
    gedeeld = int(strip.numPixels() / 3)
    for i in range(gedeeld):
        strip.setPixelColor(i, Color(255, 0, 0))
    for k in range(gedeeld):
        strip.setPixelColor(i + k, Color(0, 255, 0))
    for j in range(gedeeld):
        strip.setPixelColor(i + k + j, Color(0, 0, 255))
    strip.show()

def vullen(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def ajax(strip):
    vullen(strip,Color(0,0,0))
    gedeeld = int(strip.numPixels() / 3)
    for i in range(gedeeld):
        strip.setPixelColor(i, Color(250, 0, 0))
    for k in range(gedeeld):
        strip.setPixelColor(i + k, Color(50, 50, 50))
    for j in range(gedeeld):
        strip.setPixelColor(i + k + j, Color(250, 0, 0))
    strip.show()

def ajaxscore(strip):
    p = 0
    while p < 10:
            gedeeld = int(strip.numPixels() / 3)
            for i in range(gedeeld):
                strip.setPixelColor(i, Color(255, 0, 0))
            for k in range(gedeeld):
                strip.setPixelColor(i + k, Color(50, 50, 50))
            for j in range(gedeeld):
                strip.setPixelColor(i + k + j, Color(255, 0, 0))
            strip.show()
            time.sleep(0.3)
            vullen(strip, Color(0,0,0))
            time.sleep(0.3)
            p = p + 1
    iterations = 50
    vullen(strip, Color(50, 50, 50))
    strip.show()
    for j in range(iterations):
        for q in range(3):
            if q == 1 or q == 3:
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, Color(255, 0, 0))
                strip.show()
                time.sleep(50/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
            elif q == 2:
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, Color(255, 0, 0))
                strip.show()
                time.sleep(50/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    gedeeld = int(strip.numPixels() / 6)
    vullen(strip, Color(0,0,0))
    for a in range(gedeeld):
        strip.setPixelColor(a, Color(255, 0, 0))
    for b in range(a, a + gedeeld):
        strip.setPixelColor(b, Color(50, 50, 50))
    for c in range(b, b + gedeeld):
        strip.setPixelColor(c, Color(255, 0, 0))
    for d in range(c, c + gedeeld):
        strip.setPixelColor(d, Color(255, 0, 0))
    for e in range(d, d + gedeeld):
        strip.setPixelColor(e, Color(50, 50, 50))
    for f in range(e, e + gedeeld):
        strip.setPixelColor(f, Color(255, 0, 0))
    strip.show()
    time.sleep(10/1000.0)
    for g in range(300):
        strip.setPixelColor(a, Color(255, 0, 0))
        strip.setPixelColor(b, Color(50, 50, 50))
        strip.setPixelColor(c, Color(255, 0, 0))
        strip.setPixelColor(d, Color(255, 0, 0))
        strip.setPixelColor(e, Color(50, 50, 50))
        strip.setPixelColor(f, Color(255, 0, 0))
        time.sleep(10/1000.0)
        strip.show()
        a = a + 1
        b = b + 1
        c = c + 1
        d = d + 1
        e = e + 1
        f = f + 1
        if a == 289:
            a = 1
        if b == 289:
            b = 1
        if c == 289:
            c = 1
        if d == 289:
            d = 1
        if e == 289:
            e = 1
        if f == 289:
            f = 1


def FadeInOut(strip, r, g, b):
    """FadeInOut(strip, Color(r, g , b))"""
    for j in range(0,256,2):
        if stopdef == 1:
            return
        red = (j / 256) * r
        green = (j / 256) * g
        bleu = (j / 256) * b
        red = int(red)
        green = int(green)
        bleu = int(bleu)
        vullen(strip, Color(red, green, bleu))
        strip.show()

    for n in range(255,0,-2):
        if stopdef == 1:
            return
        red = (n / 256) * r
        green = (n / 256) * g
        bleu = (n / 256) * b
        red = int(red)
        green = int(green)
        bleu = int(bleu)
        vullen(strip, Color(red, green, bleu))
        strip.show()

def Strobe(strip, color, StrobeCount, FlashDelay, EndPause):
    """Strobe(strip, Color(r,g,b), 10, 50, 1000)"""
    for j in range(StrobeCount):
        if stopdef == 1:
            return
        vullen(strip, color)
        strip.show()
        time.sleep(FlashDelay)
        vullen(strip, Color(0,0,0))
        strip.show()
        time.sleep(FlashDelay)
    time.sleep(EndPause)

def HalloweenEyes(strip, r, g, b, EyeWidth, EyeSpace, Fade, Steps, FadeDelay, EndPause):
    """HalloweenEyes(strip, Color(255,0,0), 1, 4,
                true, random.randint(5,50), random.randint(50,150),
                random.randint(1000, 10000));
    """
    if stopdef == 1:
            return
    FadeDelay = FadeDelay / 10
    EndPause = EndPause / 1000
    StartPoint  = random.randint(0, (strip.numPixels() - (2*EyeWidth) - EyeSpace))
    Start2ndEye = StartPoint + EyeWidth + EyeSpace
    for j in range(EyeWidth):
        strip.setPixelColor(StartPoint + j, Color(r, g, b))
        strip.setPixelColor(Start2ndEye + j, Color(r, g, b))
    strip.show()
    if Fade == True:
        for n in range(Steps,0,-1):
            r = n*(r/Steps)
            g = n*(g/Steps)
            b = n*(b/Steps)
            r = int(r)
            g = int(g)
            b = int(b)
            for i in range(EyeWidth):
                strip.setPixelColor(StartPoint + i, Color(r,g,b))
                strip.setPixelColor(Start2ndEye + i, Color(r,g,b))
        strip.show()
        time.sleep(FadeDelay)
    vullen(strip,Color(0,0,0))
    time.sleep(EndPause)

def CylonBounce(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay):
    """CylonBounce(strip, Color(r,g,b), 4, 10, 50)"""
    for j in range(strip.numPixels() - EyeSize - 2):
        if stopdef == 1:
            return
        vullen(strip, Color(0,0,0))
        r = int(r)
        g = int(g)
        b = int(b)
        strip.setPixelColor(j, Color(r, g, b))
        for n in range(1,EyeSize):
            strip.setPixelColor(n + j, Color(r, g, b))
        strip.setPixelColor(j + EyeSize  , Color(r, g, b))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    for j in range(strip.numPixels() - EyeSize -2, 0, -1):
        if stopdef == 1:
            return
        vullen(strip, Color(0,0,0))
        strip.setPixelColor(j, Color(r, g, b))
        for n in range(1,EyeSize):
            strip.setPixelColor(n + j, Color(r, g, b))
        strip.setPixelColor(j + EyeSize, Color(r, g, b))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def Twinkle(strip, color, Count, SpeedDelay, OnlyOne):
    """Twinkle(strip, Color(r,g,b), 10, 100, false)"""
    vullen(strip,Color(0,0,0))
    for j in range(Count):
        if stopdef == 1:
            return
        strip.setPixelColor(random.randint(0, strip.numPixels()), color)
        strip.show()
        time.sleep(SpeedDelay)
        if OnlyOne == True:
            vullen(strip,Color(0,0,0))
    time.sleep(SpeedDelay)

def TwinkleRandom(strip, Count, SpeedDelay, OnlyOne):
    """Twinkle(strip, 10, 100, false)"""
    vullen(strip,Color(0,0,0))
    for j in range(Count):
        if stopdef == 1:
            return
        strip.setPixelColor(random.randint(0, strip.numPixels()), Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        strip.show()
        time.sleep(SpeedDelay)
        if OnlyOne == True:
            vullen(strip,Color(0,0,0))
    time.sleep(SpeedDelay)

def Sparkle(strip, color, SpeedDelay):
    """Sparkle(strip, Color(r,g,b), 0)"""
    vullen(strip, Color(0,0,0))
    pixel = random.randint(0, strip.numPixels())
    strip.setPixelColor(pixel, color)
    strip.show()
    time.sleep(SpeedDelay)
    strip.setPixelColor(pixel, Color(0, 0, 0))

def BouncingBalls(strip, colors, BallCount, numled):
    """import math"""
    start_time = datetime.datetime.now()

    Gravity = -9.81
    StartHeight = 1

    Height = np.arange(BallCount)
    Height = Height.astype(np.float)

    ImpactVelocityStart = math.sqrt( -2 * Gravity * StartHeight)

    ImpactVelocity = np.arange(BallCount)
    ImpactVelocity = ImpactVelocity.astype(np.float)

    TimeSinceLastBounce = np.arange(BallCount)
    TimeSinceLastBounce = TimeSinceLastBounce.astype(np.float)

    Position = np.arange(BallCount)
    Position = Position.astype(np.int)

    ClockTimeSinceLastBounce = np.arange(BallCount)

    Dampening = np.arange(BallCount)
    Dampening = Dampening.astype(np.float)
    for i in range(BallCount):
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        ClockTimeSinceLastBounce[i] = execution_time
        Height[i] = StartHeight
        Position[i] = 0
        ImpactVelocity[i] = ImpactVelocityStart
        TimeSinceLastBounce[i] = 0
        Dampening[i] = 0.90 - i/pow(BallCount,2)
    while True:
        if stopdef == 1:
            return
        for i in range(BallCount):
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            TimeSinceLastBounce[i] =  execution_time - ClockTimeSinceLastBounce[i]
            Height[i] = 0.5 * Gravity * pow( TimeSinceLastBounce[i]/1000 , 2.0 ) + ImpactVelocity[i] * TimeSinceLastBounce[i]/1000
            if Height[i] < 0:
                Height[i] = 0
                ImpactVelocity[i] = Dampening[i] * ImpactVelocity[i]
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                ClockTimeSinceLastBounce[i] =  execution_time
                if ImpactVelocity[i] < 0.01:
                    ImpactVelocityStart = round(ImpactVelocityStart,2)
                    ImpactVelocity[i] = ImpactVelocityStart
            Height[i] = round(Height[i],2)
            Position[i] = round(Height[i] * (numled - 1) / StartHeight)
        for i in range(BallCount):
            strip.setPixelColor(int(Position[i]), Color(colors[i][0],colors[i][1],colors[i][2]))
        strip.show()
        vullen(strip, Color(0,0,0))
        
def DrawComet(strip, color):
    vullen(strip,Color(0,0,0))
    for i in range(strip.numPixels() + 64):
        if stopdef == 1:
            return
        for j in range(strip.numPixels()):
            if random.randint(0,10) > 5:
                fadeToBlack(strip, j, 64)        
        for j in range(20):
            if (i-j) < strip.numPixels() and (i-j >= 0):
                strip.setPixelColor(i-j, color)
        strip.show()
        time.sleep(0.030)     
    for i in range(strip.numPixels(), 0,-1):
        if stopdef == 1:
            return
        for j in range(strip.numPixels(), 0, -1):
            if random.randint(0,10) > 5:
                fadeToBlack(strip, j, 64)
        for j in range(20):
            if (i-j) < strip.numPixels() and (i-j >= 0):
                strip.setPixelColor(i-j, color)
        
        strip.show()
        time.sleep(0.030)

def fadeToBlack(strip, ledNo, fadeValue): 
    oldColor = strip.getPixelColor(ledNo);
    r = (oldColor & 0x00ff0000) >> 16
    g = (oldColor & 0x0000ff00) >> 8
    b = (oldColor & 0x000000ff)
    r = int(r-(r*fadeValue/256))
    g = int(g-(g*fadeValue/256))
    b = int(b-(b*fadeValue/256))
    strip.setPixelColor(ledNo, Color(r,g,b))
    

def RunningLights(strip, r, g, b, WaveDelay):
    Position = 0
    for j in range(strip.numPixels() * 2):
        if stopdef == 1:
            return
        Position = Position + 1
        for i in range(strip.numPixels()):
          strip.setPixelColor(i, Color(
              int(((math.sin(i+Position) * 127 + 128) /255)*r),
              int(((math.sin(i+Position) * 127 + 128) /255)*g),
              int(((math.sin(i+Position) * 127 + 128) /255)*b)))
        strip.show();
        time.sleep(WaveDelay)
        
def NewKITT(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay):
  RightToLeft(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  LeftToRight(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  OutsideToCenter(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  CenterToOutside(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  LeftToRight(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  RightToLeft(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  OutsideToCenter(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)
  CenterToOutside(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay)

def CenterToOutside(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(int(((strip.numPixels() - EyeSize) / 2)),0,-1):
        if stopdef == 1:
            return
        vullen(strip, Color(0,0,0))
        strip.setPixelColor(i, Color(int(r/10), int(g/10), int(b/10)))
        for j in range(1,EyeSize + 1, 1):
            strip.setPixelColor(i + j, Color(r, g, b))
        strip.setPixelColor(strip.numPixels() - i, Color(int(r/10), int(g/10), int(b/10)))
        for j in range(1, EyeSize + 1, 1):
            strip.setPixelColor(strip.numPixels() - i - j, Color(r, g, b))
        strip.setPixelColor(strip.numPixels() - i - EyeSize - 1, Color(int(r/10), int(g/10), int(b/10)))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    
def OutsideToCenter(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(int(((strip.numPixels() - EyeSize) / 2))):
        if stopdef == 1:
            return
        vullen(strip, Color(0,0,0))
        strip.setPixelColor(i, Color(int(r/10), int(g/10), int(b/10)))
        for j in range(1,EyeSize + 1, 1):
            strip.setPixelColor(i + j, Color(r, g, b))
        strip.setPixelColor(strip.numPixels() - i, Color(int(r/10), int(g/10), int(b/10)))
        for j in range(1, EyeSize + 1, 1):
            strip.setPixelColor(strip.numPixels() - i - j, Color(r, g, b))
        strip.setPixelColor(strip.numPixels() - i - EyeSize - 1, Color(int(r/10), int(g/10), int(b/10)))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    
def LeftToRight(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(strip.numPixels() - 2):
        if stopdef == 1:
            return
        vullen(strip, Color(0,0,0))
        strip.setPixelColor(i, Color(int(r/10), int(g/10), int(b/10)))
        for j in range(1,EyeSize + 1, 1):
            strip.setPixelColor(i + j, Color(r, g, b))
        strip.setPixelColor(i+EyeSize+1, Color(int(r/10), int(g/10), int(b/10)))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def RightToLeft(strip, r, g, b, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(strip.numPixels() - 2,0,-1):
        if stopdef == 1:
            return
        vullen(strip, Color(0,0,0))
        strip.setPixelColor(i, Color(int(r/10), int(g/10), int(b/10)))
        for j in range(1,EyeSize + 1, 1):
            strip.setPixelColor(i + j, Color(r, g, b))
        strip.setPixelColor(i+EyeSize+1, Color(int(r/10), int(g/10), int(b/10)))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    
def stoppen(stop):
    global stopdef
    if stop == 1:
        stopdef = 1
    elif stop == 0:
        stopdef = 0
    return stopdef

def aanroepen(strip, led_stripValue, state, r, g, b):
    global stopdef
    if led_stripValue == "checked":
        if stopdef == 1:
            stopdef = 1
        elif state == "vullen":
            vullen(strip, Color(r,g,b))
        elif state == "ajax":
            ajax(strip)
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
            Sparkle(strip, Color(r,g,b), 0)
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
            HalloweenEyes(strip, r,g,b, 12, 6, True, random.randint(5,50), random.randint(50,150), random.randint(1000, 10000))
        elif state == "CylonBounce":
            CylonBounce(strip, r,g,b, 13, 0.010, 0.050)
        elif state == "rainbowCycle":
            rainbowCycle(strip)
        elif state == "Sparkle":
            Sparkle(strip, Color(r,g,b), 0)
        elif state == "colorWipe":
            colorWipe(strip, Color(r,g,b))
            
    else:
        vullen(strip, Color(0,0,0))


#NewKITT(255, 0, 0, 20, 0.010, 0.050);
#RunningLights(strip,255,0,0,0.05)
#theaterChase(strip, color)
#rainbow(strip)
#rainbowCycle(strip)
#theaterChaseRainbow(strip)
#ajaxscore(strip)
#ajax(strip)
#FadeInOut(strip, 255, 0, 0)
#Strobe(strip, Color(255,0,0), 10, 0.050, 1)
#HalloweenEyes(strip, 255,0,0, 12, 6, True, random.randint(5,50), random.randint(50,150), random.randint(1000, 10000))
#CylonBounce(strip, 255,0,0, 13, 0.010, 0.050)
#Twinkle(strip, Color(255,0,0), 40, 0.100, False)
#TwinkleRandom(strip, 50, 0.100, False)
#Sparkle(strip, Color(0,255,0), 0)
#a = [[255,0,0],[0,255,0],[0,0,255]]
#BouncingBalls(strip, a, 3, 67)
#DrawComet(strip)

