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

# u = user()
# u.name = 'david'
# u.age = 3
# u.mihijo = user()
# u.mihijo.name = 'pepe'
# u.mihijo.age = 35
# print u.to_JSON()


class Navi(object):
    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['Host']
        return "You have successfully reached " + host

    @cherrypy.expose
    def ADD(self, id=None):
        host = cherrypy.request.headers['Host']
        message = id + "You have successfully reached " + host
        return message
        #return u.to_JSON()

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(Navi())