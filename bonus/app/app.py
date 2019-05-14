from parse import insertToDB
import mysql.connector
import numpy as np
import json
from flask_mysqldb import MySQL
from flask import jsonify
from flask import request, Response
from flask import Flask

app = Flask(__name__)

config = {

    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': 3306,
    'database': 'goldAndSilver'

}


def convertDateToNumber(date):
    return int(date.replace('-', ''))


@app.route('/commodity')
def index():

    insertToDB()
    # convert date to number
    startDate = convertDateToNumber(request.args.get('start_date'))
    endDate = convertDateToNumber(request.args.get('end_date'))
    com_type = request.args.get('commodity_type')

    # get data from database(mysql)

    connection = mysql.connector.connect(
        host=config["host"], database=config["database"], user=config["user"], passwd=config["password"])
    cur = connection.cursor()
    if com_type == 'gold':
        query = 'select * from gold where numberOfDate >=%s and numberOfDate <=%s'
    else:
        query = 'select * from silver where numberOfDate >=%s and numberOfDate <=%s'
    param = (startDate, endDate)
    cur.execute(query, param)
    data = cur.fetchall()

    # calculate data for mean and variance
    obj = {}
    obj["data"] = {}
    list = []
    for t in data:
        obj["data"][t[3]] = float(t[2])
        list.append(float(t[2]))

    obj["mean"] = round(np.mean(list), 2)  # using numpy(np) to get mean
    obj["variance"] = round(np.var(list), 2)  # using numpy(np) to get variance
    p = json.dumps(obj, sort_keys=False, indent=1)
    res = Response(p, mimetype='application/json')

    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
