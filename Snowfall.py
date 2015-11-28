__author__ = 'madsens'
import Movies

print 'Starting'
Movies.StartLoop('/home/pi/Christmas-2015/Assets/Snowfall')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        break  # stops the loop
    else :
        Movies.PlayMovie()