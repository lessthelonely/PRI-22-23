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
    doc= nlp(review)
    tokens=[token for token in doc]
    print(tokens)
    word_frequencies={}
    for word in doc:
        if str(word).lower() not in stop_words:
            if str(word).lower() not in punctuation:
                if str(word) not in word_frequencies.keys():
                    word_frequencies[str(word)] = 1
                else:
                    word_frequencies[str(word)] += 1

    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if str(word).lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[str(word).lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[str(word).lower()]
    select_length=int(len(sentence_tokens)*0.75)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[str(word) for word in summary]
    summary=''.join(final_summary)
    print(summary)
    return summary

reviews['summary']=reviews['review'].apply(map_summary)
reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
reviews.to_csv('data/summary_test.csv')

