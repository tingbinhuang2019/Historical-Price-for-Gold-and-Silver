import mysql.connector
from mysql.connector import errorcode

DATABASE = "gold_and_silver_price"

table = {}

table["gold"] = (
	"CREATE TABLE IF NOT EXISTS `gold` ("
	"`id` int NOT NULL AUTO_INCREMENT,"
	"`date` int NOT NULL,"
	"`price` decimal(6,2) NOT NULL,"
	"`realDate` varchar(20) NOT NULL,"
	"PRIMARY KEY(`id`)"
	") ENGINE=InnoDB"
	)

table["silver"] = (
	"CREATE TABLE IF NOT EXISTS `silver` ("
	"`id` int NOT NULL AUTO_INCREMENT,"
	"`date` int NOT NULL,"
	"`price` decimal(6,2) NOT NULL,"
	"`realDate` varchar(20) NOT NULL,"
	"PRIMARY KEY(`id`)"
	") ENGINE=InnoDB"
	)

def passSchema():
	cnx = mysql.connector.connect(host='localhost', user='root', passwd='123')
	cur = cnx.cursor()
	test = True
	try:
		cur.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DATABASE))
	except mysql.connector.Error as err:
		test = False

	if(test):
		cur.execute("USE {}".format(DATABASE))
		for table_name in table:
			table_description = table[table_name]
			cur.execute(table_description)
	cur.close()
	cnx.close()

# Call function 'passSchema' to create database and tables.
# passSchema()








