import pandas as pd

df=pd.read_csv('processed/translated_title.csv')
table=pd.read_csv('dataset/goodreads_with_prices.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

df=df[df.language!='English']
print(df)

def map_title(isbn):
    table.loc[table.isbn == isbn,'title']=df.loc[df.isbn == isbn,'title'].values[0]
    print(df.loc[df.isbn == isbn,'title'].values[0])
    return True

df[df['isbn'].apply(map_title)]
table = table.loc[:, ~table.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
table.to_csv('processed/clean_titles.csv')        