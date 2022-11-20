import json
import os

def clean_json(jsonFilePath):
    data=[]

    if os.stat(jsonFilePath).st_size != 0:
        file= open(jsonFilePath)
        data=json.load(file)

    with open(jsonFilePath, 'w', encoding='utf8') as jsonf: 
        jsonString = json.dumps(data, indent=4,ensure_ascii=False)
        jsonf.write(jsonString)
        print(jsonFilePath)


clean_json('solr/everything_part_1.json')
'''
clean_json('solr/everything_part_2.json')
clean_json('solr/everything_part_3.json')
clean_json('solr/everything_part_4.json')
clean_json('solr/everything_part_5.json')
clean_json('solr/everything_part_6.json')
clean_json('solr/everything_part_7.json')
clean_json('solr/everything_part_8.json')
clean_json('solr/everything_part_9.json')
clean_json('solr/everything_part_10.json')
clean_json('solr/everything_part_11.json')
clean_json('solr/everything_part_12.json')
clean_json('solr/everything_part_13.json')
clean_json('solr/everything_part_14.json')
clean_json('solr/everything_part_15.json')
clean_json('solr/everything_part_16.json')
clean_json('solr/everything_part_17.json')
clean_json('solr/everything_part_18.json')
'''
'''
clean_json('solr/reviews_part_2.json')
clean_json('solr/reviews_part_3.json')
clean_json('solr/reviews_part_4.json')
clean_json('solr/reviews_part_5.json')
clean_json('solr/reviews_part_6.json')
clean_json('solr/reviews_part_7.json')
clean_json('solr/reviews_part_8.json')
clean_json('solr/reviews_part_9.json')
clean_json('solr/reviews_part_10.json')
clean_json('solr/reviews_part_11.json')
clean_json('solr/reviews_part_12.json')
clean_json('solr/reviews_part_13.json')
clean_json('solr/reviews_part_14.json')
clean_json('solr/reviews_part_15.json')
clean_json('solr/reviews_part_16.json')
clean_json('solr/reviews_part_17.json')
clean_json('solr/reviews_part_18.json')
'''

