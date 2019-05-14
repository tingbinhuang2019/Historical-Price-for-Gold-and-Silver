import mysql.connector
from mysql.connector import errorcode

DATABASE = "gold_and_silver_price"
table = {}

table["gold"] = (
    "CREATE TABLE IF NOT EXISTS `gold` ("
    "`id` int NOT NULL AUTO_INCREMENT,"
    "`numberOfDate` int NOT NULL,"
    "`price` decimal(6,2) NOT NULL,"
    "`realDate` varchar(20) NOT NULL,"
    "UNIQUE(`numberOfDate`),"
    "PRIMARY KEY(`id`)"
    ")"
)

table["silver"] = (
    "CREATE TABLE IF NOT EXISTS `silver` ("
    "`id` int NOT NULL AUTO_INCREMENT,"
    "`numberOfDate` int NOT NULL,"
    "`price` decimal(6,2) NOT NULL,"
    "`realDate` varchar(20) NOT NULL,"
    "UNIQUE(`numberOfDate`),"
    "PRIMARY KEY(`id`)"
    ")"
)


def passSchema():
    cnx = mysql.connector.connect(host='localhost', user='root', passwd='123')
    cur = cnx.cursor()
    test = True
    try:
        cur.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DATABASE))
    except mysql.connector.Error as err:
        test = False

    if(test):
        cur.execute("USE {}".format(DATABASE))
        for table_name in table:
            table_description = table[table_name]
            cur.execute(table_description)
    cur.close()
    cnx.close()


def insertData(list, table):
    connection = mysql.connector.connect(
        host='localhost', database='gold_and_silver_price', user='root', passwd='123')
    cursor = connection.cursor(prepared=True)
    for t in list[::-1]:
        if table == 'gold':
            query = """INSERT INTO gold(`numberOfDate`,`price`,`realDate`) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE price = %s"""
        else:
            query = """INSERT INTO silver(`numberOfDate`,`price`,`realDate`) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE price = %s"""

        param = (t[0], t[1], t[2], t[1])
        result = cursor.execute(query, param)

        connection.commit()
    connection.close()


# Call function 'passSchema' to create database and tables.
# passSchema()
