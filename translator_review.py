from deep_translator import GoogleTranslator
import emojis
from langdetect import detect
import pandas as pd
import re

def is_not_blank(s):
    return bool(s and not s.isspace())

df = pd.read_csv('data/goodreads_with_review.csv').dropna()



for index in df.index:
    if(is_not_blank(df.loc[index,'review'])):
       if(re.match('^(?=.*[a-zA-Z])',df.loc[index,'review'])): #and df.loc[index,'review'][0] not in emojis.get(df.loc[index,'review'])):
         print(df.loc[index, 'Unnamed: 0'])
         try:
          lang = detect(df.loc[index,'review'])
          if (lang != "en" and len(df.loc[index,'review']) <= 5000):
           print(df.loc[index,'url'] + " " + lang)
        # check if it really isn't english
           translated = GoogleTranslator(source='auto', target='en').translate(df.loc[index,'review']) # later check if language != english and translate only then
           df.loc[index,'review'] = translated
          #print(str(index + 2) + " " + translated)
         except:
           continue

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('data/translate_review.csv')


