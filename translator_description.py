from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd
import re

df = pd.read_csv('data/clean_titles.csv')

for index in df.index:
    if(pd.notna(df.loc[index,'desc'])):
       if(re.match('^(?=.*[a-zA-Z])',df.loc[index,'desc'])): #and df.loc[index,'review'][0] not in emojis.get(df.loc[index,'review'])):
         print(df.loc[index, 'Unnamed: 0'])
         try:
          lang = detect(df.loc[index,'desc'])
          if (lang != "en" and len(df.loc[index,'desc']) <= 5000):
           print(df.loc[index,'link'] + " " + lang)
        # check if it really isn't english
           translated = GoogleTranslator(source='auto', target='en').translate(df.loc[index,'desc']) # later check if language != english and translate only then
           df.loc[index,'desc'] = translated
          #print(str(index + 2) + " " + translated)
         except:
           continue

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('data/translate_description.csv',encoding='utf-8')

