from brewmapp import app
from flask import render_template, jsonify

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


@app.route('/guides')
def guides():
    """This method renders the guides page"""
    return render_template('guides.html')


@app.route('/about')
def about():
    """This method renders the about page"""
    return render_template('about.html')


@app.route("/api/brewery/name/<breweryname>")
def get_brewery_info(breweryname):
    """This method searches through the database and returns brewery info"""
    sql = "SELECT name,address,type FROM breweries WHERE name='%s';" % breweryname
    try:
        cursor = get_cursor()
        cursor.execute(sql)
        brewery = cursor.fetchone()
        return brewery[0] + "," + brewery[1] + "," + brewery[2]
    except:
        return 'No results.'


@app.route('/api/brewery/search/<breweryname>')
def query_possible_breweries(breweryname):
    """This methods looks for possible breweries"""
    sql = "SELECT name FROM breweries WHERE name LIKE '%s';" % ("%" + breweryname + "%")
    try:
        cursor = get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        results = [mv[0] for mv in data]
        return jsonify(results=results)
    except:
        return 'No results.'


@app.route("/api/brewery/all")
def get_all_breweries():
    """This method selects all breweries and returns them as csv"""
    sql = "SELECT name,address,type,lat,lng FROM breweries"
    cursor = get_cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    csv = "\n".join([",".join([item.replace(",", " ") for item in i]) for i in data])
    return csv


@app.route("/api/brewery/allcoords")
def get_all_breweries_json():
    """This method selects all breweries and returns them as json"""
    sql = "SELECT name, address, type, lat, lng FROM breweries;"
    cursor = get_cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return jsonify(results=data)
