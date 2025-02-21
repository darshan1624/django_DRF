import requests
import json

URL = 'http://127.0.0.1:8000/students/'

def get_students(id = None):
    data = {}
    if id:
        data = {'id':id}
    
    json_data = json.dumps(data)
    print(json_data)
    json_data = requests.get(data = json_data, url = URL)

    data = json_data.json()
    print(data)

# get_students(2)


def post_students():
    data = {
        'name':'Oliva',
        'roll': 103,
        'city':'Kolkata'
    }

    json_data = json.dumps(data)
    json_data = requests.post(data = json_data, url= URL)

    data = json_data.json()
    print(data)

# post_students()


def put_students():
    data = {
        'id':5,
        'name':'Rahul',
        'roll': 208,
        'city': 'chennai'
    }

    json_data= json.dumps(data)
    json_data = requests.put(data=json_data, url=URL)

    data = json_data.json()
    print(data)

put_students()

def delete_students():
    data = {
        'id':4,
    }

    json_data= json.dumps(data)
    json_data = requests.delete(data=json_data, url=URL)

    data = json_data.json()
    print(data)

# delete_students()