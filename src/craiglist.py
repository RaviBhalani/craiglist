import json
import ast
from geopy import distance
from decimal import Decimal


class Craigslist(object):

    def __init__(self):
        self.json_data = []
        with open("/home/meditab/craiglist/data/craiglist_data.json", "r") as read_file:
            self.json_data = json.load(read_file)

    def index(self):
        return "Hello! How are you?"

    def get_sorted_data(self, reverse=False, criteria='price'):
        sorted_user_data = []

        if ast.literal_eval(reverse):
            for user in sorted(self.json_data, key=lambda e: e['price'], reverse=True):
                user_details = str("User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +
                                   str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) + "<br>User ID : " +
                                   user['userId'] + "<br>Description : " + str(user['description']) +
                                   "<br>Price : " + str(user['price']) + "<br>Status : " + user['status'])
                sorted_user_data.append(user_details)
                sorted_user_data.append("<br><br>")
            return sorted_user_data
        else:
            for user in sorted(self.json_data, key=lambda e: e['price']):
                user_details = str("User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +
                                   str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) + "<br>User ID : " +
                                   user['userId'] + "<br>Description : " + str(user['description']) +
                                   "<br>Price : " + str(user['price']) + "<br>Status : " + user['status'])
                sorted_user_data.append(user_details)
                sorted_user_data.append("<br><br>")
            return sorted_user_data

    def get_item(self, product_id=None, location=None):

        if product_id:
            for user in self.json_data:
                if str(user["id"]) == product_id:
                    return "User Details : <br>ID : " + user['id'] + "<br>Location :<br>Lat:" +\
                           str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) + "<br>User ID : " +\
                           user['userId'] + "<br>Description : " + str(user['description']) + "<br>Price : " +\
                           str(user['price']) + "<br>Status : " + user['status']
            else:
                return "Invalid ID"

        elif location:
            location = list(location.split(","))
            for user in self.json_data:
                if repr(user['loc'][0]) == location[0] and repr(user['loc'][1]) == location[1]:
                    return "User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +\
                           str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) + "<br>User ID : "\
                           + user['userId'] + "<br>Description : " + str(user['description']) + "<br>Price : " +\
                           str(user['price']) + "<br>Status : " + user['status']
            else:
                return "Invalid Location"

    def get_item_list(self, status=None, user_id=None):
        items_list_by_status_user_id = []
        
        if status:
            if status == "removed":
                for user in self.json_data:
                    if str(user['status']) == "removed":
                        user_details = str("User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +
                                           str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) +
                                           "<br>User ID : " + user['userId'] +
                                           "<br>Description : " + str(user['description']) +
                                           "<br>Price : " + str(user['price']) + "<br>Status : " +
                                           user['status'])
                        items_list_by_status_user_id.append(user_details)
                        items_list_by_status_user_id.append("<br><br>")
                return items_list_by_status_user_id

            elif status == "tos":
                for user in self.json_data:
                    if str(user['status']) == "tos":
                        user_details = str("User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +
                                           str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) +
                                           "<br>User ID : " + user['userId'] + "<br>Description : " +
                                           str(user['description']) + "<br>Price : " + str(user['price']) +
                                           "<br>Status : " + user['status'])
                        items_list_by_status_user_id.append(user_details)
                        items_list_by_status_user_id.append("<br><br>")
                return items_list_by_status_user_id

            else:
                return "Invalid Status"

        elif user_id:
            for user in self.json_data:
                if str(user['userId']) == user_id:
                    user_details = str("User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +
                                       str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) +
                                       "<br>User ID : " + user['userId'] + "<br>Description : " +
                                       str(user['description']) + "<br>Price : " + str(user['price']) +
                                       "<br>Status : " + user['status'])
                    items_list_by_status_user_id.append(user_details)
                    items_list_by_status_user_id.append("<br><br>")
            if len(items_list_by_status_user_id):
                return items_list_by_status_user_id
            else:
                return "Invalid User ID"
        else:
            return "Invalid Status or User ID"

    def get_items_in_radius(self, radius, latitude, longitude):
        users_within_radius = []
        location = (Decimal(latitude), Decimal(longitude))

        for user in self.json_data:
            user_location = (Decimal(user['loc'][0]), Decimal(user['loc'][1]))
            if distance.distance(location, user_location).km <= Decimal(radius):
                user_details = str("User Details : <br>ID : " + user['id'] + "<br>Location : <br>Lat:" +
                                   str(user['loc'][0]) + "<br>Long:" + str(user['loc'][1]) + "<br>User ID : " +
                                   user['userId'] + "<br>Description : " + str(user['description']) +
                                   "<br>Price : " + str(user['price']) + "<br>Status : " + user['status'])
                users_within_radius.append(user_details)
                users_within_radius.append("<br><br>")

        if len(users_within_radius):
            users_within_radius.pop(0)
            return users_within_radius
        else:
            return "No items in the given radius."
