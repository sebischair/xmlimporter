#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import bleach

# u'body strikeout'
f = open('example.xml', 'r')
content = f.read()
f.close()
xml_soup = BeautifulSoup(content, 'xml')
for field in xml_soup.findAll('Field'):
	if field['Value']:

		print(field['RefName'])
		print(field['Value'] if field['RefName'] != "System.Description" else bleach.clean(field['Value'], strip=True))
		print(field.parent.parent['Id'])
