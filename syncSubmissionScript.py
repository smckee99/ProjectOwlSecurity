import json
import requests

numMessages = 10 #change this to modify number of message sent
url = "http://192.168.1.1/formSubmit.json"
ID = "ADC1" #if you want to change id, you can

i = 0 
values = { "clientID" : ID,
            "message" : "Edge isn't that bad"}

while(i<numMessages):
    values["message"] = "message number " + str(i)
    r = requests.post(url,params=values)
    print(f"Status Code: {r.status_code}")
    response = r.text
    print("Reponse:" + response)
    i+=1
