import os

__author__ = 'dmicomrt'
from subprocess import Popen, PIPE


from subprocess import call
from time import sleep

def rcvData():

    res = call('curl http://localhost:8080/doSomething', shell = True)
    #if  res == 0: print ' AIM DOING SOMZING'
    #print res
    #print type(res)

while(True):
    rcvData()
    sleep(5)