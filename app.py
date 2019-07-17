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
        """
        http://127.0.0.1:10001/get_sorted_data?reverse=False

        :param reverse:
        :param criteria:
        :return:
        """
        return self.source_code_object.get_sorted_data(reverse, criteria)

    @cherrypy.expose
    def get_item(self, product_id=None, location=None):
        """
        http://127.0.0.1:10001/get_item?product_id=53fb8f81456e74467b000002
        http://127.0.0.1:10001/get_item?location=36.164473114071,-115.14089578127711

        :param product_id:
        :param location:
        :return:
        """
        return self.source_code_object.get_item(product_id, location)

    @cherrypy.expose
    def get_item_list(self, status=None, user_id=None):
        """
        http://127.0.0.1:10001/get_item_list?status=tos
        http://127.0.0.1:10001/get_item_list?user_id=53f6c9c96d1944af0b00000b

        :param status:
        :param user_id:
        :return:
        """
        return self.source_code_object.get_item_list(status, user_id)

    @cherrypy.expose
    def get_items_in_radius(self, radius, latitude, longitude):
        """
        http://127.0.0.1:10001/get_items_in_radius?radius=0.1&latitude=36.166540711883776&longitude=-115.14080871936427

        :param radius:
        :param latitude:
        :param longitude:
        :return:
        """
        return self.source_code_object.get_items_in_radius(radius, latitude, longitude)


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 10001})
    cherrypy.quickstart(App())
