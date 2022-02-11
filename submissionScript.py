import grequests
from getDMSData import *
import json
import time


"""___________ Configuration ___________"""
# numClients = 10 #change this to modify number of clients 
# numMessages = 10 #Change this to modify number of messages sent by each client
# ID = ""
expectedOutput = "expected.out"
debugOutput = "debug.out"


def getClients():
    numClients = input("Number of clients to be run syncronously: ")
    return int(numClients)

def getNumMessages():
    numMessages = input("Number of messages to be sent: ")
    return int(numMessages)

def getID():
    ID = input("ID of message sender (enter for default): ")
    if(ID==''):
        ID = "ABC1"
    return ID

def getWaitTime():
    waitTime = input("Time to wait (seconds) after sending messages for DMS to receive (enter for default): ")
    if(waitTime==''):
        waitTime = '10'

    return int(waitTime)

def submitMessages(numClients,numMessages,ID):
    url = "http://192.168.1.1/formSubmit.json"
    dataOut = open(expectedOutput,"w")
    debugOut = open(debugOutput,"w")

    i = 1 
    j = 0

    for i in range(numMessages):
        values = []
        for j in range(numClients):
            values.append({"clientID": ID,
                            "message" : "message number" + str(j)})
            dataOut.write("Message:\t"+"message number" + str(j)+"\n")

        rs = (grequests.post(url,params=p,timeout=2) for p in values)
        ret = grequests.map(rs)

        debugOut.write("Message #"+str(i)+"\n")
        for response in ret:
            if(response != None):
                debugOut.write("\tResponse " +str(response.status_code))
                debugOut.write("\tTime elapsed: "+str(response.elapsed)+ "\n") 

        debugOut.write("\n\n")

def main():
    startTime = int(time.time())
    # startTime = 1642060858
    # endTime = 1644393122

    numClients = getClients()
    numMessages = getNumMessages()
    ID = getID()
    timeToWait = getWaitTime()

    print("Submitting messages\n")
    submitMessages(numClients,numMessages,ID)
    print("Done submitting\n")
    #Should probably add a busy wait here to ensure that we aren't missing any messages
    time.sleep(timeToWait)
    endTime = int(time.time())

    print("Getting data\n")
    DMSData = getData(startTime,endTime)
    print("Done with data\n")

if __name__ == '__main__':
    main()




