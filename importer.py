#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import bleach
import html
import json 
from pymongo import MongoClient


def connect_to_mongo():
	config = json.load(open("amelie.config.json", "r"))
	user = config["db"]["username"]
	password = config["db"]["pwd"]
	host = "localhost:27017"
	db_name = config["db"]["db_name"]
	uri = "mongodb://%s:%s@%s/%s" % (
    user, password, host, db_name)
	client = MongoClient(uri)
	return client[db_name]

def import_from_xml(db):
	f = open('items.xml', 'r')
	content = f.read()
	f.close()
	xml_soup = BeautifulSoup(content, 'xml')
	for field in xml_soup.findAll('Field'):
		print(field.parent.parent['Id'])
		if field['Value']:
			try:
				if 'Siemens.SSF.Common.CompletedDate' == field['RefName']:
					field_name = "fields.resolutiondate"
					field_value = field['Value']
				elif 'System.CreatedDate' == field['RefName']:
					field_name = "fields.created"
					field_value = field['Value']
					db.issues.find_one_and_update(
					{'id':field.parent.parent['Id'] }, 
					{ '$set':{
								
								'fields.project.key':"DFMC", 
							} 
					},
					upsert=True)
				elif 'System.Title' == field['RefName']:
					field_name = "fields.summary"
					field_value = field['Value']
				elif 'Sytem.Description' == field['RefName']:
					field_name = "fields.description"
					field_value = bleach.clean(html.unescape(field['Value']), strip=True)

				elif 'System.State' == field['RefName']:
					field_name = "fields.status.name"
					field_value = field['Value']
				elif 'System.AssignedTo' == field['RefName']:
					field_name = "fields.assignee.name"
					field_value = field['Value']
				elif 'System.WorkItemType' == field['RefName']:
					field_name = "fields.issueType.name"
					field_value = field['Value']
				elif 'System.CreatedBy' == field['RefName']:
					field_name = "fields.reporter.name"
					field_value = field['Value']
				else:
					field_name = field['RefName']
					field_value = field['Value']
				db.issues.find_one_and_update(
					{'id':field.parent.parent['Id'] }, 
					{ '$set':{
								
								field_name:field_value, 
							} 
					},
					upsert=True)

			except:
				print("Unexpected error:", sys.exc_info()[0])

if __name__ == '__main__':
	


