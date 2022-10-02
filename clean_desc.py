import pandas as pd

df=pd.read_csv('data/translate_description.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas


data=[]
for index in df.index:
    print(len(df.loc[index,'desc']))
    if(len(df.loc[index,'desc'])>5000):
        data.append(index)

for i in data:
    df.drop(i)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('./data/cleaned_desc.csv',encoding='utf-8')

