import pandas as pd

df=pd.read_csv('data/goodreads_with_reviews_translated.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas


data=[]
for index in df.index:
    print(len(df.loc[index,'review']))
    if(len(df.loc[index,'review'])>5000):
        data.append(index)

print("Above 5000")
for i in data:
    print(i)
    
df.drop(data, axis=0, inplace=True)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('./data/cleaned_reviews.csv',encoding='utf-8')

