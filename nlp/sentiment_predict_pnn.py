import pandas as pd
from transformers import pipeline

df = pd.read_csv('../data/cleaned_reviews_sentiment.csv')

classifier = pipeline("text-classification", model='cardiffnlp/twitter-roberta-base-sentiment', top_k=1)

for index in df.index:
    if (type(df.loc[index, 'review_sentiment']) != float):  # review was already evaluated
        print("review already evaluated")
        continue
    to_analyse = df.loc[index, 'review']
    try:
        prediction = classifier(to_analyse, )
    except:
        continue
    if (prediction[0][0]['label'] == "LABEL_2"):
        print("positive" + str(index))
        df.loc[index, 'review_sentiment'] = "positive"
        
    elif (prediction[0][0]['label'] == "LABEL_1"):
        print("neutral" + str(index))
        df.loc[index, 'review_sentiment'] = "neutral"
        
    else :
        print("negative" + str(index))
        df.loc[index, 'review_sentiment'] = "negative"
        
df.to_csv('./data/cleaned_reviews_sentiment_2.csv',encoding='utf-8')

