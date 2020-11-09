"""
    测试铺码服务器的接口
"""

import json

import requests

def get_request(url, data, headers):
    response = requests.post(url=url, data=data, headers=headers)
    print(response.status_code)
    print(response.json())

def open_file(filename):
    data = []
    with open(filename, 'r') as f:
        data = f.read()
    return data

def main():
    headers = {"Content-Type": "application/json"}
    data = {"username": "test001", "password": "123456"}
    url = "http://111.231.240.239:8020/TmatrixCode/User/UserLogin"

    print('UserLogin:')
    data = json.dumps(data)
    get_request(url, data, headers)

    print('\nStartTmatrix:')
    url1 = 'http://111.231.240.239:8020/TmatrixCode/User/startTmatrix'
    data = open_file('startTmatrix_copy.json')
    get_request(url=url1, data=data, headers=headers)

if __name__ == "__main__":
    main()
