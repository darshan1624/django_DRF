import requests 
import json 

URL = "http://127.0.0.1:8000/studentapi/"

def get_students(id = None):
    data = {}
    if id:
        data = {'id':id}
    json_data = json.dumps(data)
    print(json_data)

    headers = {'content-Type':'applicaton/json'}

    json_data = requests.get(url=URL, headers=headers, data= json_data)

    data = json_data.json()
    print(data)

# get_students()


def post_students():
    data = {
        'name': 'Yash',
        'roll': 105,
        'city': 'Mumbai'
    }

    # Ensure the Content-Type is correctly spelled
    headers = {'Content-Type': 'application/json'}

    json_data = json.dumps(data)
    received_json_data = requests.post(url=URL, headers=headers, data=json_data)
    data = received_json_data.json()
    print(data)


post_students()



def update_students():
    
    data = {
        'id': 12,
        'name': 'Amit',
        'roll': 180,
        'city': 'Mumbai'
    }

    headers = {'content-Type':'applicaton/json'}
    
    json_data = json.dumps(data)
    received_json_data = requests.put(url=URL, headers=headers, data=json_data)
    data = received_json_data.json()
    print(data)

# update_students()


def delete_students():
    
    data = {'id': 3}
    
    json_data = json.dumps(data)
    received_json_data = requests.delete(url=URL, data=json_data)
    data = received_json_data.json()
    print(data)

# delete_students()
