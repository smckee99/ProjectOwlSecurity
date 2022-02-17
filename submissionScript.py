import grequests
from getDMSData import *
import json
import time


"""___________ Configuration ___________"""
# numClients = 10 #change this to modify number of clients 
# numMessages = 10 #Change this to modify number of messages sent by each client
# ID = ""
expectedOutput = "expected.out"
debugOutput = "debug.txt"


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

def submitMessages(numClients,numMessages,ID,debugOut):
    url = "http://192.168.1.1/formSubmit.json"
    dataOut = open(expectedOutput,"w")
    

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


def runMessages(debugOut):
    numClients = getClients()
    numMessages = getNumMessages()
    ID = getID()
    timeToWait = getWaitTime()

    print("Submitting messages\n")
    submitMessages(numClients,numMessages,ID,debugOut)
    print("Done submitting\n")
    time.sleep(timeToWait)


def main():
    messagesSent = False
    startTime = int(time.time())
    debugOut = open(debugOutput,"w")
    # startTime = 1642060858
    # endTime = 1644393122
    
    ret = input("Send messages? (y/n)")
    while((ret!="y") and (ret!="n")):
        ret = input("Please type 'y' or 'n'")

    if(ret == 'y'):
        input("Please ensure you are connected to DuckLink. [Press enter to continue]")
        messagesSent = True
        runMessages(debugOut)

    endTime = int(time.time())

    ret = input("Retrieve messages? (y/n)")
    while((ret!="y") and (ret!="n")):
        ret = input("Please type 'y' or 'n'")

    if(ret == 'y'): 
        input("Please ensure you are connected to normal network. [Press enter to continue]")
        #Start time and end time won't make sense if we didnt send messages, so ask user for time
        if(not messagesSent):
            startTime = input("Please input start time of when to retrieve messages (Unix format)")
            endTime = input("Please input end time of when to retrieve messages (Unix format)")
        print("Getting data\n")
        DMSData = getData(startTime,endTime)
        print("Done with data\n")
    else if messagesSent:
        dataOut.write("Start time: "+startTime + "\nEnd time: "+endTime)
        

if __name__ == '__main__':
    main()




