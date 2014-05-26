import cherrypy
import json
from subprocess import call

apps = {"apps":[{"id":0,"enabled":1},{"id":1,"enabled":0},{"id":3,"enabled":0},{"id":5,"enabled":1}]}

""" Cross-Origin resource sharing """
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*" # mean: CORS to all; insert spec. origin to allow spec access
    #cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    #cherrypy.response.headers["Access-Control-Request-Headers"] = "x-requested-with"

processData = []

class Navi(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        host = cherrypy.request.headers['Host']
        return json.dumps("You have successfully reached " + host)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ADD(self, myFile=None):
        savedFile = open(myFile.filename, 'wb')
        savedFile.write(myFile.file.read())
        savedFile.close()
        message = {"ADD": 1}
        return json.dumps(message)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def CMD(self, command = None):
        response = call(command, shell=True)
        message = {command: response}
        return json.dumps(message)
        # out = []
        # pipe = os.popen(command)
        # for line in pipe:
        #     print line
        #     out.append(line)
        # return json.dumps(out)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def DEL(self, id=None):
        retValue = call('rm apps/'+id, shell=True)
        message = {"DEL": retValue}
        return json.dumps(message)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def START(self, id=None):
        response = call('docker run ubuntu ' + 'apps/' + id, shell=True)
        message = {"START": response}
        return json.dumps(message)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def STOP(self, id=None):
        response = call('docker stop ' + id)
        message = {'STOP': response}
        return json.dumps(message)


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getRep(self):
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


cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())