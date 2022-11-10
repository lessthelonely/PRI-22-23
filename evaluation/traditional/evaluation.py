import json
from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.metrics import PrecisionRecallDisplay

QRELS_FILE = 'q4_rels.txt' # 7 --> 5
QUERY_URL_NO_SCHEMA = 'http://localhost:8983/solr/book_no_schema/query?q=nightwing%20OR%20batman&q.op=OR&defType=edismax&indent=true&qf=title%20description&wt=json' #nightwing
QUERY_URL_BOOST_NO_SCHEMA = 'http://localhost:8983/solr/book_no_schema/query?q=nightwing%20OR%20batman&q.op=OR&defType=edismax&indent=true&qf=title%20description&bq=title:batman*&wt=json'
QUERY_URL_SCHEMA = 'http://localhost:8983/solr/books_schema/query?q=nightwing%20OR%20batman&q.op=OR&defType=edismax&indent=true&qf=title%20description&wt=json' #nightwing
QUERY_URL_BOOST_SCHEMA = 'http://localhost:8983/solr/books_schema/query?q=nightwing%20OR%20batman&q.op=OR&defType=edismax&indent=true&qf=title%20description&bq=title:batman*&wt=json'
# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))

# Get query results from Solr instance
normalResults = requests.get(QUERY_URL_NO_SCHEMA).json()['response']['docs']
boostedResults = requests.get(QUERY_URL_BOOST_NO_SCHEMA).json()['response']['docs']
normalResultsSchema = requests.get(QUERY_URL_SCHEMA).json()['response']['docs']
boostedResultsSchema = requests.get(QUERY_URL_BOOST_SCHEMA).json()['response']['docs']

results = [normalResults,boostedResultsSchema, normalResultsSchema, boostedResults]

_, ax = plt.subplots(figsize=(7, 8))

colors = cycle(["purple", "red", "green",  "blue"])

i = 0
for results, color in zip(results, colors):

    # METRICS TABLE
    # Define custom decorator to automatically calculate metric based on key
    metrics = {}
    def metric(f): return metrics.setdefault(f.__name__, f)

    @metric
    def ap(results, relevant):
        """Average Precision"""

        relevant_index = []
        index = 0
        for res in results:
            if (i != 0 and res['id'] in relevant) or (i == 0 and res['id'][0] in relevant):
                relevant_index.append(index)
            index = index + 1

        if len(relevant_index) == 0:
            return 0

        precision_values = [
            len([
                doc
                for doc in results[:idx]
                if (i != 0 and doc['id'] in relevant) or (i == 0 and doc['id'][0] in relevant)
            ]) / idx
            for idx in range(1, len(results) + 1)
        ]
        
        precision_sum = 0
        for ind in relevant_index:
            precision_sum = precision_sum + precision_values[ind]

        return precision_sum/len(relevant_index)

    @metric
    def p10(results, relevant, n=10):
        """Precision at N"""
        return len([
            doc
            for doc in results[:n]
            if (i != 0 and doc['id'] in relevant) or (i == 0 and doc['id'][0] in relevant)
        ]) / n

    def calculate_metric(key, results, relevant):
        return metrics[key](results, relevant)

    # Define metrics to be calculated
    evaluation_metrics = {
        'ap': 'Average Precision',
        'p10': 'Precision at 10 (P@10)'
    }

    # Calculate all metrics and export results as LaTeX table
    df = pd.DataFrame([['Metric', 'Value']] +
                      [
        [evaluation_metrics[m], calculate_metric(m, results, relevant)]
        for m in evaluation_metrics
    ]
    )

    if i == 0:
        filename = 'results_normal_no_schema_q4.tex'
    elif i == 1:
        filename = 'results_boosted_no_schema_q4.tex'
    elif i==2:
        filename = 'results_normal_schema_q4.tex'
    else:
        filename = 'results_boosted_schema_q4.tex'

    with open(filename, 'w') as tf:
        tf.write(df.to_latex())

    # PRECISION-RECALL CURVE
    # Calculate precision and recall values as we move down the ranked list
    precision_values = [
        len([
            doc
            for doc in results[:idx]
            if (i != 0 and doc['id'] in relevant) or (i == 0 and doc['id'][0] in relevant)
        ]) / idx
        for idx, _ in enumerate(results, start=1)
    ]

    recall_values = [
        len([
            doc for doc in results[:idx]
            if (i != 0 and doc['id'] in relevant) or (i == 0 and doc['id'][0] in relevant)
        ]) / len(relevant)
        for idx, _ in enumerate(results, start=1)
    ]

    precision_recall_match = {k: v for k,
                              v in zip(recall_values, precision_values)}

    # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    recall_values.extend([step for step in np.arange(
        0.1, 1.1, 0.1) if step not in recall_values])
    recall_values = sorted(set(recall_values))

    # Extend matching dict to include these new intermediate steps
    for idx, step in enumerate(recall_values):
        if step not in precision_recall_match:
            if recall_values[idx-1] in precision_recall_match:
                precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
            else:
                precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

    disp = PrecisionRecallDisplay(
        [precision_recall_match.get(r) for r in recall_values], recall_values)
    if(i == 0):
        disp.plot(ax=ax, name=f"Precision-recall without schema or boosts",
                  color=color, linewidth=1)
    elif(i == 1):
        disp.plot(ax=ax, name=f"Precision-recall boosted without schema",
                  color=color, linewidth=1)
    elif(i == 2):
        disp.plot(ax=ax, name=f"Precision-recall with schema",
                  color=color, linewidth=1.5)
    else:
        disp.plot(ax=ax, name=f"Precision-recall boosted with schema",
                  color=color, linewidth=1.5)
    i += 1

# add the legend for the iso-f1 curves
handles, labels = disp.ax_.get_legend_handles_labels()

# set the legend and the axes
ax.legend(handles=handles, labels=labels, loc="best")
ax.set_title("Precision-Recall query 4")

plt.savefig('precision_recall_query_4.png')