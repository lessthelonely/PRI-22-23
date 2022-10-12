import pandas as pd
from textblob import TextBlob

df = pd.read_csv('..//data//books_with_blurbs.csv')

df = df['Blurb']

def get_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]

df['adjectives'] = df['Blurb'].apply(get_adjectives)

df['adjectives'].to_csv('buzzwords.csv', encoding='utf-8')