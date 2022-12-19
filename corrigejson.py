#!/usr/bin/env python

with open('collection.txt', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('},]', '}]')

with open('collection.json', 'w') as file:
  file.write(filedata)
