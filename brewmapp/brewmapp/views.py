from brewmapp import app
from flask import render_template

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
