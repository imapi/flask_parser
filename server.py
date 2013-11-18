import csv
from os import listdir
from os.path import isfile, join
from flask import Flask
from flaskext.jsonify import jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/data')
@jsonify
def logs():
    dict = []
    for file in files():
        f = open("data/" + file)
        reader = csv.DictReader(f, fieldnames=("timestamp", "ip", "id",
            "ua", "address", "coordinates", "size", "score", "ex1", "ex2", "count",
            "stability", "site", "time"))
        dict = dict + [row for row in reader]
    return dict

def files():
    return [f for f in listdir('data') if isfile(join('data',f))]

if __name__ == '__main__':
    app.run()
