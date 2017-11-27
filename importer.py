#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import bleach
import html
import json 
from pymongo import MongoClient


def connect_to_mongo():
	config = json.load(open("config.json", "r"))
	user = config["db"]["username"]
	password = config["db"]["pwd"]
	host = "localhost:27017"
	db_name = config["db"]["db_name"]
	uri = "mongodb://%s:%s@%s/%s" % (
    user, password, host, db_name)
	client = MongoClient(uri)
	return client.dfmc_issues

if __name__ == '__main__':
	db = connect_to_mongo()
	#print(db.issues.find({})[0])
	f = open('items.xml', 'r')
	content = f.read()
	f.close()
	xml_soup = BeautifulSoup(content, 'xml')
	for field in xml_soup.findAll('Field'):
		if field['Value']:
			try:
				db.issues.find_one_and_update(
					{'id':field.parent.parent['Id'] }, 
					{ '$set':{
								field['RefName']:field['Value'] if field['RefName'] != "System.Description" else bleach.clean(html.unescape(field['Value']), strip=True), 
							} 
					},
					upsert=True)
			except:
				print("Unexpected error:", sys.exc_info()[0])
	f.close()

