import pandas as pd

clean_book=pd.read_csv('processed/cleaned_prices.csv')
reviews=pd.read_csv('processed/cleaned_reviews.csv')

links=list(clean_book['link'])
data=[]
for i in reviews.index:
    if(reviews.loc[i,'url'] not in links):
        print(i)
        data.append(i)

reviews.drop(data, axis=0, inplace=True)
reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
reviews.to_csv('processed/current_reviews.csv')