from xml.dom import minidom
from app import *

__author__ = 'Nikiva'

def getAppList():
    # TODO: remote call to Navy
    appsNavy = [("0", "0"), ("1", "1"), ("2", "1"), ("3", "1"),
                   ("4", "1"), ("5", "0"), ("6", "1"), ("7", "0")]

    xmlRep = minidom.parse('../Resources/AppsXML/appRep.xml')
    appListXML = xmlRep.getElementsByTagName('app')

    appList=[]
    for item in appsNavy:
        app = App(item[0], item[1], appListXML)
        appList.append(app)



    return appList
    #return [("bus", "0"), ("lightning", "1"), ("cams", "1"), ("factory", "1"),("health", "1"), ("roll", "0"), ("store", "1"), ("test", "0")]
