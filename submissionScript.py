import json
import grequests

"""___________ Configuration ___________"""
numClients = 1 #change this to modify number of clients 
numMessages = 10 #Change this to modify number of messages sent by each client
ID = "ADC1" #if you want to change id, you can


url = "http://192.168.1.1/formSubmit.json"

i = 0
j = 0
values = [{ "clientID" : ID,
            "message" : "Edge isn't that bad"}]

for i in range(numMessages):
    for j in range(numClients):
        values.append({"clientID": ID,
                        "message" : "message number" + str(j)})

    rs = (grequests.post(url,params=p) for p in values)
    print(grequests.map(rs))
