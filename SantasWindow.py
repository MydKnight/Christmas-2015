__author__ = 'madsens'
import Movies
import datetime
import time
from time import sleep

print 'Starting'
#Movies.StartLoop('/home/pi/Halloween2015/Assets/LivingLogo')

while True:
    now = datetime.datetime.now()
    now_time = now.time()
    #If between 6AM and 5PM, Play Daytime
    if datetime.time(6,00) <= now.time() <= datetime.time(17,00):
        print "Its Daytime"
        Movies.StopLoop()
        Movies.StartLoop('/home/pi/Halloween2015/Assets/DayLoop')
    else:
        print "Its Night Time"
        Movies.StopLoop()
        Movies.StartLoop('/home/pi/Halloween2015/Assets/NightLoop')
    print "Sleeping for one hour"
    time.sleep(3600)
