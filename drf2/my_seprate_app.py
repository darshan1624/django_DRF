import requests
import json

URL = "http://127.0.0.1:8000/student_create/"

data = {
    'name':'Anshuman',
    'roll':'101',
    'city':'Indore'
} 

json_data = json.dumps(data)
print(json_data)
send_request = requests.post(url=URL, data = json_data, headers = {'Content-Type': 'application/json'})

received_data = send_request.json()
print(received_data)