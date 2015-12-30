__author__ = 'madsens'
import MySQLdb
import datetime
import socket
import fcntl
import struct
from uuid import getnode as get_mac

# This file manages the connectivity to the database for logging access to the units. As a fallback, it
# writes the access to a local log file

#Global Variables used by most/all functions
db = MySQLdb.connect(host="mysql.shilohmadsen.com",
              user="shilohmadsencom",
              passwd="6DNN7Snp",
              db="themagiccastle")

mac = get_mac()

#Current Time - Used for various logging
logTime = datetime.datetime.now()
logTime = logTime.strftime('%Y-%m-%d %H:%M:%S')

#DB Cursor
cur = db.cursor()

def HeartBeat():
    #Select the row in the pis table that matches the mac address
    res = cur.execute("SELECT * FROM  PIS WHERE MacAddress = %s;",str(mac))
    #print res

    #Get the IP address of the unit.
    ip = get_ip_address('wlan0')
    #print ip

    #If no rows returned, create a new row.
    if res == 0:
        #print "Row not found. Need to create a new entry."
        res = cur.execute("INSERT INTO PIS (Status, InstallDate, IPAddress, MacAddress) VALUES (1,%s,%s, %s);",(logTime,str(ip), str(mac)))
        print res

    #Once row is created in PIs if need be, update activity with heartbeat time and ip address
    else:
        print "Row Found. Need to update row."
        cur.execute("SELECT PIID FROM PIS WHERE MacAddress = %s;",str(mac))
        piid = cur.fetchone()[0]
        #Create new item for the Heartbeat Activity
        res = cur.execute("""INSERT INTO Activity (ActivationTime, ActivationType, PIID) VALUES (%s, 1, %s);""", (logTime, piid))
        #Update the pis table with IP address
        res = cur.execute("UPDATE PIS SET IPAddress = %s WHERE PIID = %s;",(ip, piid))
        print res

    #ToDo: Allow remote naming of PI by MAC Address.

    #try to write access of the pi to a log file
    activationTime = datetime.datetime.now()
    activationTime = activationTime.strftime('%Y-%m-%d %H:%M:%S')
    #res = cur.execute("INSERT INTO Activity (RFID, PIID, ActivationTime) VALUES (%s,1,%s);",(rfid,activationTime))
    #print res
    #if connect fails or if write fails, log connection failure to an error log and log the access to a local access log.

def PowerLog():
    db = MySQLdb.connect(host="mysql.shilohmadsen.com",
                  user="shilohmadsencom",
                  passwd="6DNN7Snp",
                  db="themagiccastle")

    #Get the PIs Mac Address
    mac = get_mac()
    print mac

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    #Select the row in the pis table that matches the mac address
    res = cur.execute("SELECT * FROM  PIS WHERE MacAddress = %s;",str(mac))
    print res

    #If no rows returned, create a new row.
    if res == 0:
        #print "Row not found. Need to create a new entry."
        #Assume install date is now as its not in our database
        installDate = datetime.datetime.now()
        installDate = installDate.strftime('%Y-%m-%d %H:%M:%S')
        #Get the IP address of the unit.
        ip = get_ip_address('wlan0')
        #print ip
        res = cur.execute("INSERT INTO PIS (Status, InstallDate, IPAddress, MacAddress) VALUES (1,%s,%s, %s);",(installDate,str(ip), str(mac)))
        #print res

    #Now that we have an entry in the Pis DB, Update the activity for this pi in the activities db.
    heartbeat = datetime.datetime.now()
    heartbeat = heartbeat.strftime('%Y-%m-%d %H:%M:%S')

    #Get the IP address of the unit.
    ip = get_ip_address('wlan0')
    #print ip

    #Get the PIID of the device.
    cur.execute("SELECT PIID FROM PIS WHERE MacAddress = %s;",str(mac))
    piid = cur.fetchone()[0]

    #Update the Activity table with a heartbeat type action.
    res = cur.execute("""INSERT INTO Activity (ActivationTime, ActivationType, PIID) VALUES (%s, 1, %s);""", (heartbeat, piid))

    #Update the PI table with IP address
    res = cur.execute("UPDATE PIS SET IPAddress = %s WHERE PIID = %s;",(ip, piid))
    print res

    #ToDo: Allow remote naming of PI by MAC Address.

    #try to write access of the pi to a log file
    activationTime = datetime.datetime.now()
    activationTime = activationTime.strftime('%Y-%m-%d %H:%M:%S')
    #res = cur.execute("INSERT INTO Activity (RFID, PIID, ActivationTime) VALUES (%s,1,%s);",(rfid,activationTime))
    #print res
    #if connect fails or if write fails, log connection failure to an error log and log the access to a local access log.


def LogAccess(rfid):
    # This file manages the connectivity to the database for logging access to the units. As a fallback, it
    # writes the access to a local log file
    db = MySQLdb.connect(host="mysql.shilohmadsen.com",
                  user="shilohmadsencom",
                  passwd="6DNN7Snp",
                  db="themagiccastle")

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    #try to write access of the pi to a log file
    activationTime = datetime.datetime.now()
    activationTime = activationTime.strftime('%Y-%m-%d %H:%M:%S')
    res = cur.execute("INSERT INTO Activity (RFID, PIID, ActivationTime) VALUES (%s,1,%s);",(rfid,activationTime))
    print res
    #if connect fails or if write fails, log connection failure to an error log and log the access to a local access log.

def LogAudioAccess(rfid, filename):
    # This file manages the connectivity to the database for logging access to the units. As a fallback, it
    # writes the access to a local log file
    db = MySQLdb.connect(host="mysql.shilohmadsen.com",
                  user="shilohmadsencom",
                  passwd="6DNN7Snp",
                  db="themagiccastle")

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    #try to write access of the pi to a log file
    activationTime = datetime.datetime.now()
    activationTime = activationTime.strftime('%Y-%m-%d %H:%M:%S')
    res = cur.execute("INSERT INTO Activity (RFID, PIID, ActivationTime, FileName) VALUES (%s,1,%s, %s);",(rfid,activationTime, filename))
    print res
#if connect fails or if write fails, log connection failure to an error log and log the access to a local access log.

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])