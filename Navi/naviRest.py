import urllib
import cherrypy
import json
from subprocess import call
from datetime import datetime
import requests
import time

idNavi = "1"
repIP = "37.187.9.5:7777"
databaseIP = "37.187.9.5:13370"
appsDB = []
processData = []
appsLocal = []


""" Cross-Origin resource sharing """
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*" # mean: CORS to all; insert spec. origin to allow spec access
    #cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    #cherrypy.response.headers["Access-Control-Request-Headers"] = "x-requested-with"

""" Registra el log en la BD """
def logDB(timestamp, levelno, message, event, extra):
    url = 'http://'+ databaseIP +'/log/logging'
    payload = {'timestamp': timestamp, 'levelno': levelno, 'message': message, 'event': event, 'idNavi': idNavi, 'extra': extra}
    r = requests.post(url, data=json.dumps(payload))
    return r.status_code == requests.codes.ok


def searchLocalById(id):
    find = False
    i = 0
    while (i < len(appsLocal)) and (not find):
        if appsLocal[i]["id"] == id: find = True
        else: i += 1
    if find: return i

class Navi(object):

    """ Load Local state """
    @staticmethod
    def loadState():
        json_data = open('data.json')
        appsLocal.extend(json.load(json_data))
	print appsLocal

    """ Descarrega el repository dapps """
    @staticmethod
    def getApps():
        r = requests.get('http://' + databaseIP + '/app')
        appsDB.extend(r.json())

    """ Cerca i retorna lapp en el repository obtingut """
    def getAppFromDB(self, id=None):
        return next((app for app in appsDB if app['id'] == int(id)), None)


    #--------INSTALL--------
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def install(self, id=None):
        app = self.getAppFromDB(id)
        # Descarrega de lapp
        call('mkdir apps/'+id, shell=True)
        urllib.urlretrieve('http://' + repIP + '/repository/' + app['dir'] + '/' + app['file_name'], 'apps/' + id + '/' + app['file_name'])
        #install + creacio imatge de la app (docker)
        file = open('apps/'+id+'/Dockerfile', 'w')
        file.write('FROM pybuntu\n'
                   'ADD ' + app['file_name'] + ' /apps/'+app['file_name'] + '\nEXPOSE 808'+id+'\nRUN echo "Image created"')
        file.close()
        call('docker build -t ' + id + ' ./apps/'+id, shell=True)
        #consistenciaLocal
        ap = {"id":id, "run":0}
        appsLocal.append(ap)
        with open('data.json', 'w') as outfile:
            json.dump(appsLocal, outfile)
        # Logging
        message = ""+ app['name'] +" - Application Installed"
        extra = {'idApp': id }
        response = logDB(str(time.time()), "20", message, "install", extra)
        return json.dumps({"success": response})

    #--------REMOVE---------
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def remove(self, id=None):
        #remove docker image + all files related
        app = self.getAppFromDB(id)
        call('rm -rf apps/'+id, shell=True)
        #incloure if esta started, ferli kill
        call('docker kill '+ id, shell=True)
        call('docker rm ' + id, shell=True)
        call('docker rmi ' + id, shell=True)
        #consistenciaLocal
        t = searchLocalById(id)
        appsLocal.pop(t)
        with open('data.json', 'w') as outfile:
            json.dump(appsLocal, outfile)
        # Logging
        message = ""+ app['name'] +" - Application Removed"
        extra = {'idApp': id }
        response = logDB(str(time.time()), "20", message, "remove", extra)
        return json.dumps({"success": response})

    #--------START--------
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def start(self, id=None):
        app = self.getAppFromDB(id)
        #run del contenidor
        call('docker run -p 808'+id+':808'+id+' -d --name ' + id + ' ' + id + ' python /apps/'+app['file_name'], shell=True)
        #call('docker run -p 808'+id+':808'+id+' -d --name ' + id + ' ' + id + ' echo "hello world" >> testecho', shell=True)
	print "he fet un run"
        #consistenciaLocal
        appsLocal[searchLocalById(id)]["run"] = 1
        with open('data.json', 'w') as outfile:
            json.dump(appsLocal, outfile)
        # Logging
        message = ""+ app['name'] +" - Application Started"
        extra = {'idApp': id }
        response = logDB(str(time.time()), "20", message, "start", extra)
        return json.dumps({"success": response})

    #--------STOP--------
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def stop(self, id=None):
        app = self.getAppFromDB(id)
        #stop i esborrada del contenidor
        call('docker kill '+ id, shell=True)
        call('docker rm ' + id, shell=True)
        #consistenciaLocal
        appsLocal[searchLocalById(id)]["run"] = 0
        with open('data.json', 'w') as outfile:
            json.dump(appsLocal, outfile)
        # Logging
        message = ""+ app['name'] +" - Application Stopped"
        extra = {'idApp': id }
        response = logDB(str(time.time()), "20", message, "stop", extra)
        return json.dumps({"success": response})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def cmd(self, command = None):
        # TODO: Case amb la comanda corresponent
        #response = call(command, shell=True)
        response = True
        return json.dumps({"success": response})
        # out = []
        # pipe = os.popen(command)
        # for line in pipe:
        #     print line
        #     out.append(line)
        # return json.dumps(out)


# Obtneir tots la BBDD de les apps en el repository
Navi.getApps()
Navi.loadState()
for i in appsLocal:
    if i["run"] == 1:
        app = Navi.getAppFromDB(i["id"])
        call('docker run -p 808'+i["id"]+':808'+i["id"]+' -d --name ' + i["id"] + ' ' + i["id"] + ' python /apps/'+app['file_name'], shell=True)


# Start CherryPy
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())
