#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ("Helder")
__version__ = ("0.1")
__url__ = ('http://williams.best.vwh.net/sunrise_sunset_algorithm.htm')

#imports
PY3=True
from math import floor, ceil, pi, atan, tan, sin, asin, cos, acos
from datetime import timedelta
import datetime
import sys
#   script imports
#imports

d2r = pi/180

###############################################
def getInput(statement):
    if PY3: return(input(statement))
    else: return(raw_input(statement))

###############################################
def dayOfYear(d,m,y):
    return(floor(275*m/9) - (floor((m+9)/12) * (1+floor((y-4*floor(y/4)+2)/3))) + d - 30)

###############################################
def timeCalc(lat, lng, doy, td_utc, sunrise):
    
    #convert the longitude to hour value and calculate an approximate time
    lngH = lng/15
    t = doy + ((6 if sunrise else 18) - lngH)/24

    #m => Sun's mean anomaly
    m = (0.9856 * t) - 3.289
    
    #l => Sun's true longitude
    l = m + (1.916 * sin(m*d2r)) + (0.020 * sin(2 * m*d2r)) + 282.634
    l +=  -360 if l > 360 else 360 if l < 360 else 0
    
    #ra = Sun's right ascension (right ascension value needs to be in the same quadrant as L)
    ra = atan(0.91764 * tan(l*d2r))/d2r
    ra +=  -360 if ra > 360 else 360 if ra < 360 else 0
    ra += (floor(l/90) - floor(ra/90)) * 90
    ra /= 15

    #sinDec, cosDec => Sine and Cosine of Sun's declination
    sinDec = 0.39782 * sin(l*d2r)
    cosDec = cos(asin(sinDec))

    #Sun's local hour angle
    cosH = (cos(90.8333333333333*d2r) - (sinDec * sin(lat*d2r))) / (cosDec * cos(lat*d2r))
    if sunrise and cosH > 1: print('the sun never rises on this location (on the specified date)'); sys.exit()
    elif not sunrise and cosH < -1: print('the sun never sets on this location (on the specified date)'); sys.exit()
    h = ((360 - (acos(cosH)/d2r)) if sunrise else (acos(cosH)/d2r))/15
    
    #Local mean time of rising/setting
    meanT = h + ra - (0.06571 * t) - 6.622

    #adjust back to local standard time
    local = meanT - lngH + td_utc
    local += 24 if local < 0 else -24 if local > 24 else 0
    return(local)
    
###############################################
def timeDate(date):
    return(timedelta(seconds = date*3600))

###############################################
def main(sunrise, sunset, length):
#     lat = float(getInput('Enter Latitude (+ve for N & -ve for S): '))
#     lng = float(getInput('Enter Longitude (+ve for E & -ve for W):'))
#     d,m,y = map(int,getInput('DD-MM-YYYY: ').split('-'))
#     td_utc = float(getInput('Enter time difference from UTC: '))
    
    lat = float('51.972820')
    lng = float('5.345250')
    d,m,y = map(int,'12-11-2020'.split('-'))
    td_utc = float('1')
    
    datum = datetime.datetime.now()
    y = (datum.year)
    m = (datum.month)
    d = (datum.day)

    if 0 < d < 32 and 0 < m < 13:
        sunrise = timeCalc(lat, lng, dayOfYear(d,m,y), td_utc, True)
        sunset = timeCalc(lat, lng, dayOfYear(d,m,y), td_utc, False)

        lod = sunset - sunrise

        #print(sunrise, sunset, lod)
        sunrise = ('Sunrise: {}'.format(timeDate(sunrise)))
        sunset = ('Sunset: {}'.format(timeDate(sunset)))
        length = ('Length of day: {}'.format(timeDate(lod)))
        
        sunrise = sunrise.replace("Sunrise: ","")
        sunset = sunset.replace("Sunset: ","")
        length = length.replace("Length of day: ","")
        
        sunrise = sunrise[:8]
        sunset = sunset[:8]
        length = length[:8]

    else:
        print('Please check date.')
        sys.exit()
    return sunrise, sunset, length
