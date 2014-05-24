import logging
import cherrypy
import json
from subprocess import call
import os

apps = {"apps":[{"id":0,"enabled":1},{"id":1,"enabled":0},{"id":3,"enabled":0},{"id":5,"enabled":1}]}


# class user:
#     def to_JSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

""" Cross-Origin resource sharing """
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*" # mean: CORS to all; insert spec. origin to allow spec access
    #cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    #cherrypy.response.headers["Access-Control-Request-Headers"] = "x-requested-with"


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
        call(command, shell=True)
        message = {command: 1}
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
        call('rm apps/'+id, shell=True)
        message = {"DEL": 1}
        return json.dumps(message)
        #set headers a jsons

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def START(selfself, id=None):
        #call(id, shell=True)
        message = {"START": 1}
        return json.dumps(message)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getRep(self):
        return json.dumps(apps)

cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())