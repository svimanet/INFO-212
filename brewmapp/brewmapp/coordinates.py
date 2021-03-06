import requests
import MySQLdb
import time

conn = MySQLdb.connect("brewmapp.pw", "root", "weberootnow", "brewmapp")
cursor = conn.cursor()


def get_coords(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=AIzaSyCN0vhX2FQSENp9161rhLuoXUDCo-PmXiQ&libraries'
    r = requests.get(url)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    return {"lat": location['lat'], "lng": location['lng']}


def insert_all_coords():
    cursor.execute('SELECT id, address FROM breweries;')
    data = cursor.fetchall()
    for brewery in data:
        try:
            coords = get_coords(brewery[1])
            sql = 'UPDATE breweries SET lat = %s, lng = %s Where id = %s;' % (coords["lat"], coords["lng"], brewery[0])
            cursor.execute(sql)
            conn.commit()
            print(sql)
        except:
            print('Possible QUERY_LIMIT. Waiting 10 seconds.')
            time.sleep(10)
    conn.commit()


# insert_all_coords()

