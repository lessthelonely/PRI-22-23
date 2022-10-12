import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import pandas as pd

reviews=pd.read_csv('data/reviews_test.csv')
nlp=spacy.load("en_core_web_sm")

#NLTK Stop words
from nltk.corpus import stopwords
stop_words=stopwords.words('english')

def map_summary(review):
    doc=nlp(review)

    # create dictionary
    word_dict = {}
    # loop through every sentence and give it a weight
    for word in doc:
        word = word.text.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # create a list of tuple (sentence text, score, index)
    sents = []
    # score sentences
    sent_score = 0
    for index, sent in enumerate(doc.sents):
        for word in sent:
            word = word.text.lower()
            sent_score += word_dict[word]
        sents.append((sent.text.replace("\n", " "), sent_score/len(sent), index))

    # sort sentence by word occurrences
    sents = sorted(sents, key=lambda x: -x[1])
    # return top 3
    sents = sorted(sents[:3], key=lambda x: x[2])

    # compile them into text
    summary_text = ""
    for sent in sents:
        summary_text += sent[0] + " "
 
    print(summary_text)
    return summary_text

reviews['summary']=reviews['review'].apply(map_summary)
reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
reviews.to_csv('data/summary_test2.csv')
