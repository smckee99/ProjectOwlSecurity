import json
import requests
import getpass
import re
import time
from submissionScript import *

"""___________ Configuration ___________"""
actualOutput = "DMSData.out"

def writeToFile(dataRet):
    dataOut = open(actualOutput,"w")
    counter = 0
    messages =[]

    for element in dataRet.json():
        #first check to be sure that the event is not a status update (we dont care about those rn)
        eventType = element["eventType"]
        if(eventType=="portal"):
            payload = re.split(',|{|{',element["payload"])
            message = re.split(':',payload[3])[1][7:-2]
            messages.append(message)
            #dataOut.write("Message:\t"+message+"\n")

    #iterate through list in reverse
    for i in range(len(messages) -1,-1,-1) :
        dataOut.write("Message:\t"+messages[i]+"\n")
            
            

def getData(startTime,endTime):
    tokenUrl = "https://owl-dms-api.us-south.cf.appdomain.cloud/api/users/authenticate"

    duckID = input("Enter Papa duck ID: ")
    username = input("Enter DMS Username: ")
    password = getpass.getpass("Enter DMS password: ")

    # startTime = 1581234722
    # endTime = 1644393122

    #Put info into JSON payload
    payload = { "username" : username,
                "password" : password}

    #Parse for the return for the token value
    ret = requests.post(tokenUrl, json=payload)
    jsonRet = ret.json()
    token = jsonRet["token"]

    dataUrl = "https://owl-dms-api.us-south.cf.appdomain.cloud/api/userdata/getrawdata"

    #hopefully make so that user can just run the script and this is auto filled
    timeAppend = "?start="+str(startTime)+"&end="+str(endTime)+"&papaId="+duckID    

    #create the header to contain the token
    tokenHeader = { 'Authorization' : 'Bearer '+token}

    #get the data?
    dataRet = requests.get(dataUrl+timeAppend,headers=tokenHeader)

    writeToFile(dataRet)
