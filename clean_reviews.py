import pandas as pd

df=pd.read_csv('data/goodreads_with_reviews_translated.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas


data=[]
for index in df.index:
    print(len(df.review))
    if(len(df.review)>5000):
        data.append(index)

for i in data:
    df.drop(i)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('./data/cleaned_reviews.csv',encoding='utf-8')

