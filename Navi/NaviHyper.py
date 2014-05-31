__author__ = 'dmicomrt'

import socket
from subprocess import call
import sys
import time

def addApp(appName):

    f = open('new' + appName,'wb')
    conn.send("")
    l = conn.recv(1024)
    f.write(l)
    f.close()
    #print("SEND: App " + appName + " Added to NAVI.")
    data = "SERVER: App " + appName + " Added to NAVI."
    return data


def deleteApp(appName):
    print("SEND: App " + appName + " deleted from NAVI.")
    data = "SERVER: App " + appName + " deleted from NAVI."
    return data


def startApp(appName):
    print("SEND: App " + appName + " running on NAVI.")
    data = "SERVER: App " + appName + " running on NAVI."
    return data


def stopApp(appName):
    print("SEND: App " + appName + " is not running now on NAVI.")
    data = "SERVER: App " + appName + " is not running now on NAVI."
    return data


def getRepository():
    data = "<Respotory list here>"
    return data


def wrongPetition(funcName=None):
    print("SEND: Petition " + funcName + "is not found, please try again.")
    data = "SERVER: Petition  " + funcName + " is not found, please"
    return data


def makeCommand(command=None):
    call(command, shell=True)
    return command + " done."







def responsePetition(petition=None):
    if (petition[0] == 'ADD'):
        response = addApp(petition[1])
    elif (petition[0] == 'DEL'):
        response = deleteApp(petition[1])
    elif (petition[0] == 'START'):
        response = startApp(petition[1])
    elif (petition[0] == 'STOP'):
        response = stopApp(petition[1])
    elif (petition[0] == 'GET'):
        response = getRepository()
    elif (petition[0] == "CMD"):
        response = makeCommand(petition[1])
    else:
        response = wrongPetition(petition[0])

    return response

#------------------------MAIN---------------------------#

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

data = [[None]] * 2

print 'Connected by', addr
while True:
    data[0] = conn.recv(1024)
    conn.send("")
    data[1] = conn.recv(1024)
    print("RECIEVED: " + data[0] + "  " + data[1])
    response = responsePetition(data)
    print response
    conn.send(response)
    if not data: break
conn.close()