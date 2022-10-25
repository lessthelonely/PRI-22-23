import csv
import json
import ast

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
    with open(csvFilePath, encoding='ansi') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, delimiter=';', ) 
        i = 0

        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            for x in row.keys():
                if (x == 'author' or x == 'genre'):
                    row[x] = list(row[x].split(','))
                else:
                    row[x] = guess_type(row[x])
            jsonArray.append(row)
            i = i + 1
            print(i)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'./solr/current_data_13_10.csv'
jsonFilePath = r'./solr/current_data_13_10.json'
csv_to_json(csvFilePath, jsonFilePath)