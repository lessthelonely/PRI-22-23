from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd
import re

clean_book = pd.read_csv('processed/data_without_extra_spaces.csv')

for i in clean_book.index:
       if(pd.notna(clean_book.loc[i,'desc']) and not (clean_book.loc[i,'desc'][:4]=='http' and len(clean_book.loc[i,'desc']) == 40) and not (re.match('^[0-9*#+.,> -]+$',clean_book.loc[i,'desc']))):
           lang = detect(clean_book.loc[i,'desc'])
           print(str(i) + " " + lang)
           if (lang != "en" and len(clean_book.loc[i,'desc']) <= 5000):
             print(str(i) + " " + lang)
             translated = GoogleTranslator(source='auto', target='en').translate(clean_book.loc[i,'desc']) # later check if language != english and translate only then
             clean_book.loc[i,'desc'] = translated
          #print(str(index + 2) + " " + translated)

clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('processed/translated_description.csv')

