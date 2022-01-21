import json
#import requests
import grequests

numMessages = 10 #change this to modify number of message sent
url = "http://192.168.1.1/formSubmit.json"
ID = "ADC1" #if you want to change id, you can

i = 0 
values = [{ "clientID" : ID,
            "message" : "Edge isn't that bad"}]

for i in range(numMessages):
    values.append({"clientID": ID,
                    "message" : "message number" + str(i)})

    


rs = (grequests.post(url,params=p) for p in values)
print(grequests.map(rs))
