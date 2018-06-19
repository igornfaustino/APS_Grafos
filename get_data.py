import json


def get_data():
    with open('data.json') as json_file:  
        data = json.load(json_file)
        return data
