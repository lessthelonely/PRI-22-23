from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd
import re

reviews=pd.read_csv('data/more_reviews.csv')

for i in reviews.index:
       if(pd.notna(reviews.loc[i,'review']) and not (re.match('^[0-9*#+.,> -/]+$',reviews.loc[i,'review']))):
           try:
            lang = detect(reviews.loc[i,'review'])
            print(str(i) + " " + lang)
            if (lang != "en" and len(reviews.loc[i,'review']) <= 5000):
             print(str(i) + " " + lang)
             translated = GoogleTranslator(source='auto', target='en').translate(reviews.loc[i,'review']) # later check if language != english and translate only then
             reviews.loc[i,'review'] = translated
           except:
            print(str(i)+" "+"EXCEPTION")  


reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
reviews.to_csv('data/translated_more_reviews.csv')

