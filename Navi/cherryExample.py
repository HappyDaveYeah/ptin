import urllib
import cherrypy
import json
from subprocess import call
from datetime import datetime
import requests
import time

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
    def install(self, id=None):
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
    def remove(self, id=None):
        app = self.getAppFromRep(id)
        response = call('rm apps/'+app['file_name'], shell=True)
        response = True
        return json.dumps({"success": response})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def start(self, id=None):
        app = self.getAppFromRep(id)
        response = call('docker run ubuntu ' + 'apps/' + id, shell=True)
        return json.dumps({"success": response})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def stop(self, id=None):
        //response = call('docker stop ' + 'apps/' + id)
        url = 'http://37.187.9.5:13370/log/logging'
        payload = {'timestamp': '1401019205.97', 'levelno': '50', 'message': 'Stopping App', 'event': 'restart', 'idNavi': '1'}
        r = requests.post(url, data=json.dumps(payload))
        response = True
        return json.dumps({"success": response})

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


# Obtneir tots la BBDD de les apps en el repository
Navi.getRep()

# Start CherryPy
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())
