import urllib
import cherrypy
import json
from subprocess import call
import requests

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

    """ Cerca i retorna l'app en el repository obtingut """
    def getAppFromRep(self, id=None):
        return next((app for app in repository if app['id'] == int(id)), None)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ADD(self, id=None):
        app = self.getAppFromRep(id)
        # Descarrega de lapp
        urllib.urlretrieve('http://' + repIP + '/repository/' + app['dir'] + '/' + app['file_name'], 'apps/' + app['file_name'])

        response = 1
        return json.dumps(response)

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
        response = call('rm apps/'+id, shell=True)
        return json.dumps(response)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def START(self, id=None):
        response = call('docker run ubuntu ' + 'apps/' + id, shell=True)
        return json.dumps(response)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def STOP(self, id=None):
        response = call('docker stop ' + id)
        return json.dumps(response)


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
        return("getAllLog")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getLog(self, timestamp=None):
        return json.dumps({"success": True, "payload": timestamp})

Navi.getRep()
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())