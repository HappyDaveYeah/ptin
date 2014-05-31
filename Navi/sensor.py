__author__ = 'dmicomrt'
from subprocess import call
from time import sleep

def sendData():
    res = call('curl http://localhost:8080/inputData/random1/random2', shell = True)
    print res


while(True):
    sendData()
    sleep(2)