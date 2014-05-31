import cherrypy
from subprocess import call
import json

def addApp(appName):
    print("SEND: App " + appName + " deleted from NAVI.")
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


def wrongPetition():
    print("SEND: Petition is not found, please try again.")
    data = "SERVER: Petition is not found, please try again"
    return data

class Repository:
    exposed = True
    def GET(self, id=None, appName=None):
        if id == None:
            return(wrongPetition())
        elif id == 'ADD':
            return(addApp(appName))
        elif id == 'DEL':
            return(deleteApp(id))
        else:
            return(wrongPetition())


if __name__ == '__main__':

    cherrypy.tree.mount(
        Repository(), '/navi/repository',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    #cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 80})
    cherrypy.engine.start()
    cherrypy.engine.block()