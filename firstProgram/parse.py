import lxml.html
import requests as req 
from db import passSchema,insertData

gold_url = 'https://www.investing.com/commodities/gold-historical-data/'
silver_url = 'https://www.investing.com/commodities/silver-historical-data/'
month = {
  'Jan': '01',
  'Feb': '02',
  'Mar': '03',
  'Apr': '04',
  'May': '05',
  'Jun': '06',
  'Jul': '07',
  'Aug': '08',
  'Sep': '09',
  'Oct': '10',
  'Nov': '11',
  'Dec': '12'
}

def convertToNumber(str):
	arr = str.split(",")
	temp = arr[0].split(" ")
	return int(arr[1].strip() + month[temp[0]] + temp[1])

def convertToDate(str): 
	arr = str.split(",")
	temp = arr[0].split(" ")
	return arr[1].strip() + '-' + month[temp[0]] + '-' + temp[1]

def parser(list, url):

	# Setting up xpath to parse data from above urls 
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	html = req.get(url,headers = headers)
	doc = lxml.html.fromstring(html.content)
	table = doc.xpath('//table[@id="curr_table"]')

	# Using list to store data from text contents of htmlElements  
	list1 = []
	list = [] 
	for n in table:
		list1.append(n[1])

	for tr in list1[0]: 
		arr = tr.text_content().split("\n")
		list.append((convertToNumber(arr[1].strip()), float(arr[2].strip().replace(',','')), convertToDate(arr[1].strip())))
	return list

# function call to create database and tables in mysql 
passSchema()

# extract data from urls 
goldPrice = parser([],gold_url)
silverPrice = parser([],silver_url)

# insert data to table
insertData(goldPrice,"gold")
insertData(silverPrice,"silver")







