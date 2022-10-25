import pandas as pd
from transformers import pipeline

#reviews= pd.read_csv('data/reviews_test.csv')
reviews=pd.read_csv('data/reviews_merged_no_nulls.csv')
book_profiles=pd.read_csv('data/buzzwords.csv')
#book_profiles = pd.read_csv('data/book_profiles_test.csv')

reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
book_profiles = book_profiles.loc[:, ~book_profiles.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

links=reviews.url.unique()


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

def map_moods(i):
    sentiments=[]
    for r in reviews.loc[reviews.url==i,'review'].values:
        to_analyse = r 
        try:
            prediction=classifier(to_analyse, )
        except:
            continue
        sentiments.append(prediction[0][0]['label'])
    sentiments=', '.join(list(set(sentiments)))
    print(sentiments)
    book_profiles.loc[book_profiles.link==i,'mood']=sentiments
    return sentiments

list(map(map_moods,links))
book_profiles.to_csv('data/mood.csv')
