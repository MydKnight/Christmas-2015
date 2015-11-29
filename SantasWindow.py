__author__ = 'madsens'
import Movies
import time
import datetime

print 'Starting'
#Movies.StartLoop('/home/pi/Halloween2015/Assets/LivingLogo')

while True:
    now = datetime.datetime.now()
    now_time = datetime.now.time()
    #If between 6AM and 5PM, Play Daytime
    if time(6,00) <= datetime.now.time() <= time(17,00):
        print "Its Daytime"
        #Movies.StopLoop()
        #Movies.StartLoop('/home/pi/Halloween2015/Assets/DayLoop')
    else:
        print "Its Night Time"
        #Movies.StopLoop()
        #Movies.StartLoop('/home/pi/Halloween2015/Assets/NightLoop')
    print "Sleeping for one hour"
    time.sleep(3600)
