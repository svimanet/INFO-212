from brewmapp import app
from flask import render_template
import MySQLdb
import json


def get_cursor():
    conf = json.load(open("./config.json"))
    conn = MySQLdb.connect(conf["database"],conf["user"],conf["password"],conf["database"])
    return conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    """This method renders the index page"""
    return render_template('index.html')


@app.route("/brewery/name=<name>")
def get_brewery_info(name):
    """This method searches through the database and return brewery info"""
    # TODO below
    # Search database for info and address

    info = "This is some brewery information"
    address = "Someaddress 1337"

    # Format the info and return as json or something

    # maybe just return json instead of a template
    return render_template('brewery.html', name=name, info=info, address=address)


@app.route("/api/brewery/all")
def get_all_breweries():
    sql = "SELECT name,address,type FROM breweries"
    cursor = get_cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    csv = "\n".join([",".join([item.replace(","," ") for item in i]) for i in data])
    return csv
