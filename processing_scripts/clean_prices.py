import pandas as pd
clean_book = pd.read_csv('processed/cleaned_bookformat.csv')

for i in clean_book.index:
    clean_book.loc[i,'price']=str(clean_book.loc[i,'price']).replace('�','€')

for i in clean_book.index:
    if('$' in str(clean_book.loc[i,'price'])):
        ind = str(clean_book.loc[i,'price']).index('$')
        clean_book.loc[i,'price']=str(clean_book.loc[i,'price'])[ind+1:] + ' €'

clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('processed/cleaned_prices.csv')