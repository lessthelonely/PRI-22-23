from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd
import re

df = pd.read_csv('dataset/goodreads_with_language.csv')

for index in df.index:
    if(pd.notna(df.loc[index,'title'])):
       if(re.match('^(?=.*[a-zA-Z])',df.loc[index,'title'])): #and df.loc[index,'review'][0] not in emojis.get(df.loc[index,'review'])):
         print(df.loc[index, 'Unnamed: 0'])
         try:
          lang = detect(df.loc[index,'title'])
          if (lang != "en" and len(df.loc[index,'title']) <= 5000):
           print(df.loc[index,'title'] + " " + lang)
        # check if it really isn't english
           translated = GoogleTranslator(source='auto', target='en').translate(df.loc[index,'title']) # later check if language != english and translate only then
           print(translated)
           df.loc[index,'title'] = translated
          #print(str(index + 2) + " " + translated)
         except:
           continue

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('processed/translated_title.csv')
