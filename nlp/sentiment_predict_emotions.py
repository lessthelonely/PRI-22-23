import pandas as pd
from transformers import pipeline

reviews=pd.read_csv('../data/reviews_merged_no_nulls.csv')
book_profiles=pd.read_csv('../data/buzzwords.csv')

reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
book_profiles = book_profiles.loc[:, ~book_profiles.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

links=reviews.url.unique()

classifier = pipeline("text-classification", model='j-hartmann/emotion-english-distilroberta-base', top_k=7)

def map_moods(i):
    sentiments=[]
    sentiments_dict = {'neutral': 0, 'joy': 0, 'disgust': 0, 'sadness':0, 'anger': 0, 'surprise': 0, 'fear': 0}
    count = 0
    labels = ['neutral', 'joy', 'disgust', 'sadness', 'anger', 'surprise', 'fear']
    for r in reviews.loc[reviews.url==i,'review'].values:
        to_analyse = r 
        try:
            predict=classifier(to_analyse, )
            dataList = predict[0]
        except:
            continue
        for dic in dataList:
            if (len(dataList) != 0):
                label = ""
                percent = ""
                for key, value in dic.items():
                    if(label == ""):
                        label += str(value)
                    else:
                        percent += str(value)
                if (percent != ""):
                    sentiments_dict[label] += float(percent)
        count += 1
                
    if (count > 0):
        for j in labels:
            sentiments_dict[j] = sentiments_dict[j] / count
    print(i)
    if (count > 0):
        sentiments_list = str(sentiments_dict).replace("{", "[")
        sentiments_list = sentiments_list.replace("}", "]")
        book_profiles.loc[book_profiles.link==i,'mood']=str(sentiments_list)
        return sentiments_dict
    else:
        book_profiles.loc[book_profiles.link==i,'mood']=str(sentiments)
        return sentiments

list(map(map_moods,links))
book_profiles.to_csv('moods_remastered.csv')

