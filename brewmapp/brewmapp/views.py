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


@app.route("/api/brewery/name/<breweryname>")
def get_brewery_info(breweryname):
    """This method searches through the database and returns brewery info"""
    # TODO below
    # Search database for name, address and type
    sql = "SELECT name,address,type FROM breweries WHERE name='%s';" % breweryname
    try:
        cursor.execute(sql)
        brewery = cursor.fetchone()
        return brewery[0] + "," + brewery[1] + "," + brewery[2]
    except:
        return 'No results.'


@app.route("/api/brewery/all")
def get_all_breweries():
    sql = "SELECT name,address,type FROM breweries"
    cursor = get_cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    csv = "\n".join([",".join([item.replace(","," ") for item in i]) for i in data])
    return csv
