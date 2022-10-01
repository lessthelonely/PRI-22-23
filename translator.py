from deep_translator import GoogleTranslator
import pandas as pd

df = pd.read_csv('data/goodreads_with_language.csv')
table=pd.read_csv('data/goodreads_with_prices.csv')
# print(df.to_string())

for index in df.index:
    #print(index)
    lang = df.loc[index,'language']
    if (lang != "English" and not (df.loc[index,'title'].isnumeric())):
        translated = GoogleTranslator(source='auto', target='en').translate(df.loc[index,'title'])
        table.loc[index,'title'] = translated
        print(str(index + 2) + " " + translated)

table.to_csv('data/goodreads_titles_translated.csv',encoding='utf-8')