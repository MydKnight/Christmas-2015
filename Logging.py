__author__ = 'madsens'
import MySQLdb
import datetime
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
        print "Row not found. Need to create a new entry"

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