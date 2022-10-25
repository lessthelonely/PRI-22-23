import csv
import json
import ast
import pandas as pd

def guess_type(x):
    attempt_fns = [ast.literal_eval,
                   float,
                   int,
                   str
                   ]
    for fn in attempt_fns:
        try:
            return fn(x)
        except (ValueError, SyntaxError):
            pass
    return x

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, delimiter=',', ) 
        i = 0

        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            for x in row.keys():
                if x == 'id':
                    row[x]=int(row[x])
            jsonArray.append(row)
            i = i + 1
            print(i)
                
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath = r'reviews_part_1.csv'
jsonFilePath = r'reviews_part_1.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_2.csv'
jsonFilePath = r'reviews_part_2.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_3.csv'
jsonFilePath = r'reviews_part_3.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_4.csv'
jsonFilePath = r'reviews_part_4.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_5.csv'
jsonFilePath = r'reviews_part_5.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_6.csv'
jsonFilePath = r'reviews_part_6.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_7.csv'
jsonFilePath = r'reviews_part_7.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_8.csv'
jsonFilePath = r'reviews_part_8.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_9.csv'
jsonFilePath = r'reviews_part_9.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_10.csv'
jsonFilePath = r'reviews_part_10.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_11.csv'
jsonFilePath = r'reviews_part_11.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_12.csv'
jsonFilePath = r'reviews_part_12.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_13.csv'
jsonFilePath = r'reviews_part_13.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_14.csv'
jsonFilePath = r'reviews_part_14.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_15.csv'
jsonFilePath = r'reviews_part_15.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_16.csv'
jsonFilePath = r'reviews_part_16.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_17.csv'
jsonFilePath = r'reviews_part_17.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'reviews_part_18.csv'
jsonFilePath = r'reviews_part_18.json'
csv_to_json(csvFilePath, jsonFilePath)


