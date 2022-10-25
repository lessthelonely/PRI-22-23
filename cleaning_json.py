import json
import sys
import os
import yaml
import re

data=[]

if os.stat('solr/current_book_data_13_10.json').st_size != 0:
    file= open('solr/current_book_data_13_10.json')
    data=file.read()

reg= u"\"[\u4e00-\u9fff]+.*?"
pattern=re.compile(reg,re.UNICODE)
print(pattern)
print(re.findall(pattern, data[4]))


'''
    data_dump=json.dumps(data)
    print(data_dump)
    json.loads(data_dump)

    with open('solr/book_data_test', 'w', encoding='utf8') as jsonf: 
        jsonString = yaml.safe_load(data_dump)
        jsonf.write(jsonString)
'''
    