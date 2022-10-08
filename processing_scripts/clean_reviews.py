import pandas as pd
from langdetect import detect

df=pd.read_csv('processed/translated_review.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas


data=[]
for index in df.index:
    if(type(df.loc[index,'review'])==str):
        print(len(df.loc[index,'review']))
        if(len(df.loc[index,'review'])>5000 and detect(df.loc[index,'review']) != 'en'):
          print(index)
          data.append(index)

print("Above 5000")
for i in data:
    print(i)

df.drop(data, axis=0, inplace=True)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('processed/cleaned_review.csv')

