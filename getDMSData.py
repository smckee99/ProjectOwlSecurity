import json
import requests
import getpass

url = "https://owl-dms-api.us-south.cf.appdomain.cloud/api/users/authenticate"
username = input("Enter DMS username: ")
password = getpass.getpass("Enter DMS password: ")

#Put info into JSON payload
payload = { "username" : username,
            "password" : password}

ret = requests.post(url, json=payload)
jsonRet = ret.json()


print(jsonRet["token"])
