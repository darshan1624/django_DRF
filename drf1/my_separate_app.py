###############################################################################################
''' This is a seprate file. Not has to do anything with DRF.
Just treat it as a seprate application which requests the data from api written in api app.
This is a demonstartion of how api request is sent from diff application to get data from db maintained by app api.  
''' 
###############################################################################################


import requests

URL = "http://127.0.0.1:8000/student"

json_data=requests.get(url=URL)

data = json_data.json()

print(data)