from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd

df = pd.read_csv('data/goodreads_with_review.csv')

for index in df.index:
    lang = detect(df.loc[index,'review'])
    if (lang != "en"):
        # check if it really isn't english
        translated = GoogleTranslator(source='auto', target='en').translate(df.loc[index,'review']) # later check if language != english and translate only then
        df.loc[index,'review'] = translated
        print(str(index + 2) + " " + translated)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('data/goodreads_with_review.csv')

