
__author__ = 'dmicomrt'
import requests
from time import sleep

def rcvData():
    if __name__ == '__main__':
        url = "http://localhost:8080/doSomething"
        r = requests.get(url)
        if r == 'GOES': print 'IM DOING SOMEZING!!'
        print r
while(True):
    rcvData()
    sleep(5)