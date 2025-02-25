import re
import pandas as pd

#reviews= pd.read_csv('data/reviews_test.csv')
reviews=pd.read_csv('data/reviews_merged_no_nulls.csv')
book_profiles=pd.read_csv('data/trigger.csv')

pacings=['fast','slow']

reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
book_profiles = book_profiles.loc[:, ~book_profiles.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

links=reviews.url.unique()

def map_pacing(i):
    r_str=""
    for r in reviews.loc[reviews.url==i,'review'].values:
        if(not (re.match('^[0-9*#+.,> -/]+$',r))):
            r_str+=r
    new_str = re.sub(r'[^a-zA-Z]', ' ', r_str)
    re_low=[x.lower() for x in new_str.split()]
    pacing=', '.join(list(set(re_low).intersection(pacings)))
    print(len(pacing))
    if(len(pacing)==0 or len(pacing)>4):
        pacing='medium'
    print(pacing)
    book_profiles.loc[book_profiles.link==i, 'pacing']=pacing
    return pacing 
 
   
pacing_list=list(map(map_pacing,links))
book_profiles.to_csv('data/pacing.csv')
