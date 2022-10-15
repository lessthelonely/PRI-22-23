import pandas as pd
from transformers import pipeline

df = pd.read_csv('../data/cleaned_reviews_sentiment_2.csv')

classifier = pipeline("text-classification", model='j-hartmann/emotion-english-distilroberta-base', top_k=1)

"""
to_analyse = df.loc[1, 'review']
print(to_analyse)

try:
    predict = classifier(to_analyse, )
    print(predict[0][0]['label'])
except:
    print("failed")

"""

for index in df.index:

    to_analyse = df.loc[index, 'review']
    try:
        prediction = classifier(to_analyse, )
    except:
        continue
    print(str(index) + " : " + prediction[0][0]['label'])
    df.loc[index, 'review_mood'] = prediction[0][0]['label']


df.to_csv('../data/cleaned_reviews_sentiment_3.csv',encoding='utf-8')
