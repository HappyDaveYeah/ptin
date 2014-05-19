from xml.dom import minidom

from Hylian.PySide.app import *


__author__ = 'Nikiva'

def getAppList():
    # TODO: GET call to Navy
    appsNavy = [("0", "0", "1"), ("1", "1", "1"), ("2", "1", "1"), ("3", "1", "1"),
                   ("4", "1", "1"), ("5", "0", "0"), ("6", "1", "1"), ("7", "0", "0")]

    xmlRep = minidom.parse('../Resources/AppsXML/appRep.xml')
    appListXML = xmlRep.getElementsByTagName('app')

    appList = []
    for item in appsNavy:
        app = App(item[0], item[1], item[2], appListXML)
        appList.append(app)

    return appList


def add(app):
    #TODO: ADD call to Navy
    pass


def delete(app):
    #TODO: DEL call to Navy
    pass


def enable(app):
    #TODO: START call to Navy
    pass


def disable(app):
    #TODO: STOP call to Navy
    pass