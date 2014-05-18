import cherrypy
import json

# l = []
# l.append('hello')
# l.append('pipi')
# l.append('papa')
# l.append('popo')
# l.append('pupu')
# l.append('lala')
# l.append('lolo')


class user:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

u = user()
u.name = 'david'
u.age = 3
# u.mihijo = user()
# u.mihijo.name = 'pepe'
# u.mihijo.age = 35
# print u.to_JSON()

""" Cross-Origin resource sharing """
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*" # mean: CORS to all; insert spec. origin to allow spec access
    #cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    #cherrypy.response.headers["Access-Control-Request-Headers"] = "x-requested-with"

class Navi(object):
    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['Host']
        return "You have successfully reached " + host

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ADD(self, id=None):
        host = cherrypy.request.headers['Host']
        message = id + "You have successfully reached " + host
        #return message
        #return u.to_JSON()
        return json.dumps({"message": "Hello World!"})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def switch(self, id):
        print("Licht nr {} wurde geschaltet".format(id))
        return json.dumps({"text" : "schalter {} ".format(id)})

cherrypy.config.update({'server.socket_host': '0.0.0.0', 'tools.CORS.on': True})
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Navi())