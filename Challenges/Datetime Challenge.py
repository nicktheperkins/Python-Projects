# The Portland-based company you work for just opened two new branches.
# One is in New York City, the other in London. They need a very simple program to find out if the branches are open or closed.
# The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.

from datetime import datetime
import pytz


def getTime():
    Portland = datetime.now(pytz.timezone('US/Pacific'))
    New York = datetime.now(pytz.timezone('US/Eastern'))
    London = datetime.now(pytz.timezone('Europe/London'))
    
time1 = datetime.now(pytz.timezone('Europe/London'))
print(time1.strftime('%I:%M %p %m/%d/%Y'))

time2 = datetime.now(pytz.timezone('US/Pacific'))
print(time2.strftime('%I:%M %p %m/%d/%Y'))

time3 = datetime.now(pytz.timezone('US/Eastern'))
print(time3.strftime('%I:%M %p %m/%d/%Y'))