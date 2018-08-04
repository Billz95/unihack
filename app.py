from flask import Flask, request, jsonify
from restfultool import *
from flask_cors import CORS
import sqlite3
import json
from database import *
from utils import *

data = Data()
try:
    data.createTable()
except:
    print("Table already there!")

app = Flask(__name__)
CORS(app)


def sql_exec(arg):
    users_conn = sqlite3.connect('users.db')
    user_cursor = users_conn.cursor()
    user_cursor.execute(arg)
    data = user_cursor.fetchall()
    users_conn.commit()
    users_conn.close()
    return data

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "{}"

"""
Create new User
"""
@app.route('/api/user', methods=['POST'])
def add_user():
    request_data = request.get_json()

    if not all(e in request_data for e in ["username", "lon", "lat", "info"]):
        return statusResponse(R400_BADREQUEST)

    username = request_data["username"]
    lon = request_data["lon"]
    lat = request_data["lat"]
    info = request_data["info"]

    data.createOwner(username, lon, lat, info)

    return statusResponse(R200_OK)


"""
Add new item info, the user must exist
"""
@app.route('/api/item', methods=['POST'])
def add_item():
    request_data = request.get_json()
    if not all(e in request_data for e in ["username", "item_name", "item_price", "description", "img"]):
        return statusResponse(R400_BADREQUEST)

    username = request_data["username"]
    item_name = request_data["item_name"]
    item_price = float(request_data["item_price"])
    description = request_data["description"]
    img = request_data["img"]

    # Check if the user exist
    owner = data.findOwner(username)
    print("finish finding")
    # print(owner)
    if owner.count() == 0:
        print("Not matched")
        return statusResponse(R404_NOTFOUND)

    # Add the Item into the items
    data.insertItem(item_name, username, item_price, description, img)

    return statusResponse(R200_OK)


"""
Update Item in the database
"""
@app.route('/api/item', methods=['PUT', 'PATCH'])
def update_item():
    r = request.get_json()
    if not all(e in r for e in ["id", "price", "description", "item_name", "owner_name", "img"]):
        return statusResponse(R400_BADREQUEST)

    data.updateItem(int(r['id']), r['item_name'], r['owner_name'], r['price'], r['description'], r["img"])

    # Add the Item into the items
    return statusResponse(R200_OK)


"""
Search for the Items in the distance with specified name
"""
@app.route('/api/item/term/', methods=['GET'])
def get_item_by_name():
    args = request.args
    if not all(e in args for e in ["s", "lon", "lat", "limit"]):
        return statusResponse(R400_BADREQUEST)

    item_name = request.args.get('s')
    lon = float(request.args.get('lon'))
    lat = float(request.args.get('lat'))
    limit = int(request.args.get('limit'))

    print(lon, lat)

    items = data.searchItemByName(item_name)

    toRet = {'count': 0,
             'items': []}

    for item in items:
        owner_loc = data.findOwner(item.owner)[0].get_loc()
        distance = calculate_distance(lon, lat, *owner_loc)
        if (distance < limit):
            d_item = item.dictify()
            d_item['lon'] = owner_loc[0]
            d_item['lat'] = owner_loc[1]
            d_item['distance'] = distance
            toRet['count']+=1
            toRet['items'].append(d_item)


    # toRet = {'count': items.count(),
    #          'items': [item.dictify() for item in items if
    #                    calculate_distance(lon, lat, *data.findOwner(item.owner)[0].get_loc()) <= limit]}

    # Add the Item into the items
    return fullResponse(R200_OK, toRet)


"""
Find the requested item with the specified id
"""
@app.route('/api/item/id/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    items = data.searchItemById(item_id)
    toRet = {'count': items.count(), 'items': [item.dictify() for item in items]}
    # Add the Item into the items
    return fullResponse(R200_OK, toRet)

"""
Search the requested items From the specified Owner by his name
"""
@app.route('/api/owner/name/<owner_name>', methods=['GET'])
def get_item_by_owner_name(owner_name):

    items = data.searchItemByOwnerName(owner_name)

    toRet = {'count': items.count(),
             'items': [item.dictify() for item in items]}

    # Add the Item into the items
    return fullResponse(R200_OK, toRet)

"""
Search the requested items From the specified Owner by its id
"""
@app.route('/api/owner/id/<int:id>', methods=['GET'])
def get_item_by_owner_id(id):

    items = data.searchItemByOwnerId(id)

    toRet = {'count': items.count(),
             'items': [item.dictify() for item in items]}

    # Add the Item into the items
    return fullResponse(R200_OK, toRet)


if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    app.run()
