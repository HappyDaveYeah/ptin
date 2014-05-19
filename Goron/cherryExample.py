import cherrypy
import json
from subprocess import call

apps = {'0': 'enabled', '3': 'disabled', '7': 'enabled'}


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
    def ADD(self, id=None):
        host = cherrypy.request.headers['Host']
        message = id + "You have successfully reached " + host
        return json.dumps(message)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def CMD(self, command = None):
        call(command, shell=True)
        return json.dumps(command + " done.")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def DEL(self, id=None):
        call('rm apps/'+id, shell=True)
        return json.dumps(id + ' removed from NAVI')
        #set headers a jsons

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def START(selfself, id=None):
        #call(id, shell=True)
        return json.dumps(id + ' started on NAVI')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getRep(self):
        return json.dumps(apps)

cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())