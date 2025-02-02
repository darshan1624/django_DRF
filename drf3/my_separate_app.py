import requests 
import json 

URL = "http://127.0.0.1:8000/get_students/"

def get_students(id = None):
    data = {}
    if id:
        data = {'id':id}
    json_data = json.dumps(data)
    print(json_data)
    json_data = requests.get(url=URL, data= json_data)

    data = json_data.json()
    print(data)

get_students(1)