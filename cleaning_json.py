import json
import sys
import os
import yaml
import re

data=[]

if os.stat('solr/current_book_data_13_10.json').st_size != 0:
    file= open('solr/current_book_data_13_10.json')
    data=json.load(file)



    with open('solr/current_book_data_25_10.json', 'w', encoding='utf8') as jsonf: 
        jsonString = json.dumps(data, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
