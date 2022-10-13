import spacy
import re
import pandas as pd

reviews= pd.read_csv('data/reviews_test.csv')
#reviews=pd.read_csv('data/reviews_merged_no_nulls.csv')
#book_profiles=pd.read_csv('data/book_profiles.csv')

reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
links=reviews.url.unique()

NER = spacy.load("en_core_web_sm")

#doc = NER("Apple is looking at buying U.K. startup for $1 billion")

#entities = [ent for ent in doc.ents if ent.label_ == "ORG" or ent.label_=='PERSON' or ent.label_=='LOCATION' or ent.label_=='"WORK_OF_ART' or ent.label_=='GPE']
#print(entities)

def map_ner(i):

            r=[reviews.loc[reviews.url==i, 'review'].values[0]]
            new_str = re.sub(r'[^a-zA-Z]', ' ', r[0])
            doc=NER(new_str)
            entities = [ent for ent in doc.ents if ent.label_ == "ORG" or ent.label_=='PERSON' or ent.label_=='LOCATION' or ent.label_=='"WORK_OF_ART' or ent.label_=='GPE']
            entity=', '.join(entities)
            print(entity)
            #book_profiles.loc[book_profiles.link==i, 'entities']=entity
            return entity


entities_list=list(map(map_ner,links))
reviews.to_csv('data/ner_test.csv')

