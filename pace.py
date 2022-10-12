import re
import pandas as pd

#reviews= pd.read_csv('data/reviews_test.csv')
reviews=pd.read_csv('data/reviews_merged.csv')
book_profiles=pd.read_csv('data/book_profiles.csv')

pacings=['fast','slow']

reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
book_profiles = book_profiles.loc[:, ~book_profiles.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

links=reviews.url.unique()

def map_pacing(i):
    r=[reviews.loc[reviews.url==i, 'review'].values[0]]
    new_str = re.sub(r'[^a-zA-Z]', ' ', r[0])
    re_low=[x.lower() for x in new_str.split()]
    pacing=', '.join(list(set(re_low).intersection(pacings)))
    print(len(pacing))
    if(len(pacing)==0 or len(pacing)>4):
        pacing='medium'
    print(pacing)
    book_profiles.loc[book_profiles.link==i, 'pacing']=pacing
    return pacing 
   
pacing_list=list(map(map_pacing,links))
reviews.to_csv('data/pacing.csv')
