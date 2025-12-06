# import requests
# import json

# def send_request(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def send_request(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def parse():
#     data_list = list()
#     for i in range(1, 83):
#         data = send_request(f'https://swapi.dev/api/people/{i}/')
#         if data:
#             data_list.append(data)
#     return data_list
            
# def save_data(data):
#     with open('data.json', mode='w', encoding='utf-8') as file:
#         json.dump(data, file)            

# def update_data(data):
#     data_dict = {}
#     for index, el in enumerate(data):
#         data_dict[index] = el
#     return data_dict
        

# def main():
#     data = parse()
#     data = update_data(data)
#     save_data(data)
    
# if __name__ == '__main__':

#     main()

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS characters(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
); 

'''




















