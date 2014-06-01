import logging
import urllib
import cherrypy
import json
from subprocess import call
from datetime import datetime
import jsonlogger
import requests
import time

apps = {"apps":[{"id":0,"enabled":1},{"id":1,"enabled":0},{"id":3,"enabled":0},{"id":5,"enabled":1}]}
repIP = "37.187.9.5:7777"
repository = []
processData = []


""" Cross-Origin resource sharing """
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*" # mean: CORS to all; insert spec. origin to allow spec access
    #cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    #cherrypy.response.headers["Access-Control-Request-Headers"] = "x-requested-with"


class Navi(object):
    """ Descarrega el repository dapps """
    @staticmethod
    def getRep():
        r = requests.get('http://' + repIP + '/repository/repo.json')
        repository.extend(r.json()['apps'])

    """ Cerca i retorna lapp en el repository obtingut """
    def getAppFromRep(self, id=None):
        return next((app for app in repository if app['id'] == int(id)), None)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ADD(self, id=None):
        app = self.getAppFromRep(id)
        # Descarrega de lapp
        urllib.urlretrieve('http://' + repIP + '/repository/' + app['dir'] + '/' + app['file_name'], 'apps/' + app['file_name'])

        response = True
        return json.dumps({"success": response})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def CMD(self, command = None):
        response = call(command, shell=True)
        return json.dumps(response)
        # out = []
        # pipe = os.popen(command)
        # for line in pipe:
        #     print line
        #     out.append(line)
        # return json.dumps(out)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def DEL(self, id=None):
        app = self.getAppFromRep(id)
        response = call('rm apps/'+app['file_name'], shell=True)
        return json.dumps({"success": response})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def START(self, id=None):
        app = self.getAppFromRep(id)
        response = call('docker run ubuntu ' + 'apps/' + id, shell=True)
        logger.info("Starting " + app['name'] + " Application", extra={"timestamp": time.time()})
        return json.dumps({"success": response})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def STOP(self, id=None):
        response = call('docker stop ' + 'apps/' + id)
        return json.dumps({"success": response})


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getApps(self):
        return json.dumps(apps)


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def inputData(self, id=None, data=None):
        processData.append(data)
        print('Data '+ data + ' recieved from ' + id + '.')
        return json.dumps('OK')

    @cherrypy.expose
    def doSomething(self):
        if len(processData) >= 5:
            return('GOES')
        else:return('')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getAllLog(self):
    # Obtenir log
        json_log = open('log/navi.log')
        log = json.load(json_log)
        json_log.close()
        return json.dumps(log)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getLog(self, timestamp=None):
        # Obtenir log
        json_log = open('log/navi.log')
        log = json.load(json_log)
        json_log.close()

        # TODO: filtar els logs i enviar els logs > timestamp

        return json.dumps({"success": True, "payload": log})

# Obtneir tots la BBDD de les apps en el repository
Navi.getRep()

# Setup el Logger
logger = logging.getLogger("NaviLogger")
logHandler = logging.FileHandler('log/navi.log')
formatter = jsonlogger.JsonFormatter('%(timestamp)s %(levelno)s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Start CherryPy
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())
