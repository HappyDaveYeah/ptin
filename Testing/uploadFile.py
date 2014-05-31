__author__ = 'Niki'
import requests

if __name__ == '__main__':
    files = open('appstore.png', 'rb')
    url = "http://localhost:8080/ADD"
    r = requests.post(url, files={'myFile': files})
    print r.text