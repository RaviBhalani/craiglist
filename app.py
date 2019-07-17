import cherrypy
from craiglist import *


class App(object):

    def __init__(self):
        self.source_code_object = Craigslist()

    @cherrypy.expose
    def index(self):
        return "Hello, how are you?"

    @cherrypy.expose
    def get_sorted_data(self, reverse=False, criteria='price'):
        return self.source_code_object.get_sorted_data(reverse, criteria)

    @cherrypy.expose
    def get_item(self, product_id=None, location=None):
        return self.source_code_object.get_item(product_id, location)

    @cherrypy.expose
    def get_item_list(self, status=None, user_id=None):
        return self.source_code_object.get_item_list(status, user_id)

    @cherrypy.expose
    def get_items_in_radius(self, radius, latitude, longitude):
        return self.source_code_object.get_items_in_radius(radius, latitude, longitude)


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 10001})
    cherrypy.quickstart(App())
