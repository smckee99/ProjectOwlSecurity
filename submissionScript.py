import json
import grequests

"""___________ Configuration ___________"""
numClients = 10 #change this to modify number of clients 
numMessages = 10 #Change this to modify number of messages sent by each client
ID = "ADC1" #if you want to change id, you can
fileOutput = "dataOut"

url = "http://192.168.1.1/formSubmit.json"
dataOut = open(fileOutput,"w")

i = 1 
j = 0
for i in range(numMessages):
    values = []
    for j in range(numClients):
        values.append({"clientID": ID,
                        "message" : "message number" + str(j)})

    rs = (grequests.post(url,params=p,timeout=2) for p in values)
    ret = grequests.map(rs)
    print(ret)
    dataOut.write("Message #"+str(i)+"\n")
    for response in ret:
        if(response != None):
            dataOut.write("Response " +str(response.status_code))
            dataOut.write("\tTime elapsed: "+str(response.elapsed)+ "\n") 

    dataOut.write("\n\n")
    #print(grequests.map(rs))
