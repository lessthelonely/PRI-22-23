import pandas as pd

df=pd.read_csv('data/cleaned_desc.csv')
table=pd.read_csv('data/book_depository_pages.csv')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
table = table.loc[:, ~table.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

def map_pages(isbn):
    df.loc[df.isbn == isbn,'pages']=table.loc[table.isbn == isbn,'pages'].values[0]
    print(table.loc[table.isbn == isbn,'pages'].values[0])
    return True


df[df['isbn'].apply(map_pages)]
df = df.drop('isbn13', axis=1)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('data/clean_book_data.csv',encoding='utf-8')   