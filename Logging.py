__author__ = 'madsens'
import MySQLdb
import datetime
import socket
import fcntl
import struct
from uuid import getnode as get_mac

def HeartBeat():
    # This file manages the connectivity to the database for logging access to the units. As a fallback, it
    # writes the access to a local log file
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
        print "Row not found. Need to create a new entry."
        #Assume install date is now as its not in our database
        installDate = datetime.datetime.now()
        installDate = installDate.strftime('%Y-%m-%d %H:%M:%S')
        #Get the IP address of the unit.
        ip = get_ip_address('wlan0')
        print ip
        res = cur.execute("INSERT INTO PIS (Status, InstallDate, IPAddress, MacAddress) VALUES (1,%s,%s, %s);",(installDate,str(ip), str(mac)))
        print res
    else:
        print "Row Found. Need to update row."
        heartbeat = datetime.datetime.now()
        heartbeat = heartbeat.strftime('%Y-%m-%d %H:%M:%S')
        #Get the IP address of the unit.
        ip = get_ip_address('wlan0')
        print ip
        cur.execute("SELECT PIID FROM PIS WHERE MacAddress = %s;",str(mac))
        piid = cur.fetchone()[0]
        res = cur.execute("INSERT INTO Activity (ActivationTime, ActivationType, PIID) VALUES (%s, 1 %d);",(heartbeat, int(piid)))
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