__author__ = 'madsens'
import Movies
import datetime
import time

print 'Starting'
Movies.StartLoop('/home/pi/Christmas-2015/Assets/Fireplace')
time.sleep(10)

while True:
    now = datetime.datetime.now()
    now_time = now.time()
    #If between 6AM and 5PM, Play Daytime
    if datetime.time(6,00) <= now.time() <= datetime.time(17,00):
        print "Its Daytime"
        Movies.StopLoop()
        Movies.StartLoop('/home/pi/Christmas-2015/Assets/DayLoop')
    else:
        print "Its Night Time"
        Movies.StopLoop()
        Movies.StartLoop('/home/pi/Christmas-2015/Assets/NightLoop')
    print "Sleeping for one hour"
    time.sleep(3600)