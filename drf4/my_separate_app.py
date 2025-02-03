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

# get_students(1)




def post_students():
    
    data = {
        'name': 'Anket',
        'roll':103,
        'city':'Mumbai'
    }

    json_data = json.dumps(data)
    received_json_data = requests.post(url=URL, data=json_data)
    data = received_json_data.json()
    print(data)

# post_students()



def update_students():
    
    data = {
        'id': 1,
        'name': 'Yash',
        'roll': '110',
        'city':'Mumbai'
    }
    
    json_data = json.dumps(data)
    received_json_data = requests.put(url=URL, data=json_data)
    data = received_json_data.json()
    print(data)

# update_students()


def delete_students():
    
    data = {'id': 1}
    
    json_data = json.dumps(data)
    received_json_data = requests.delete(url=URL, data=json_data)
    data = received_json_data.json()
    print(data)

delete_students()
