# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd

QRELS_FILE = 'information_systems_qrels.txt'
QUERY_URL = 'http://localhost:8983/solr/courses/select?q=title%3Ainforma%C3%A7%C3%A3o&wt=json'

# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance
results = requests.get(QUERY_URL).json()['response']['docs']

print(results)
