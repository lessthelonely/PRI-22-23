import pandas as pd
from langdetect import detect


df=pd.read_csv('processed/translated_description.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas


data=[]
for index in df.index:
    print(len(df.loc[index,'desc']))
    if(len(df.loc[index,'desc'])>5000 and detect(df.loc[index,'desc']) != 'en'):
        data.append(index)

print("Above 5000")
df.drop(data, axis=0, inplace=True)

for i in df.index:
    if('�' in df.loc[i,'description']):
        df=df.drop(i)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('processed/cleaned_desc.csv')

