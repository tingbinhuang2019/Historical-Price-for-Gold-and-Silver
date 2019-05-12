from flask import render_template
from flask import request, Response
from app import app
from flask import jsonify
from flask_mysqldb import MySQL
import json
import numpy as np

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'historical_price'
mysql = MySQL(app)


def convertDateToNumber(date):
    return int(date.replace('-', ''))


@app.route('/commodity')
def index():

    # convert date to number
    startDate = convertDateToNumber(request.args.get('start_date'))
    endDate = convertDateToNumber(request.args.get('end_date'))
    com_type = request.args.get('commodity_type')

    # get data from database(mysql)

    cur = mysql.connection.cursor()
    query = 'select * from goldPrice where date >=%s and date <=%s'
    param = (startDate, endDate)
    cur.execute(query, param)
    data = cur.fetchall()

    # calculate data for mean and variance
    obj = {}
    obj["data"] = {}
    list = []
    for t in data:
        obj["data"][t[1]] = float(t[2])
        list.append(float(t[2]))

    obj["mean"] = round(np.mean(list), 2)  # using numpy(np) to get mean
    obj["variance"] = round(np.var(list), 2)  # using numpy(np) to get variance
    p = json.dumps(obj, sort_keys=False, indent=1)
    res = Response(p, mimetype='application/json')

    return res
