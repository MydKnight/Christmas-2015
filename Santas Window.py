__author__ = 'madsens'
import Movies
from datetime import datetime
import time

print 'Starting'
#Movies.StartLoop('/home/pi/Halloween2015/Assets/LivingLogo')

while True:
    now = datetime.now()
    now_time = now.time()
    #If between 6AM and 5PM, Play Daytime
    if time(6,00) <= now.time() <= time(17,00):
        print "Its Daytime"
        #Movies.StopLoop()
        #Movies.StartLoop('/home/pi/Halloween2015/Assets/DayLoop')
    else:
        print "Its Night Time"
        #Movies.StopLoop()
        #Movies.StartLoop('/home/pi/Halloween2015/Assets/NightLoop')
    print "Sleeping for one hour"
    time.sleep(3600)