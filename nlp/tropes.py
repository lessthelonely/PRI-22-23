import re
import pandas as pd

#reviews= pd.read_csv('data/reviews_test.csv')
reviews=pd.read_csv('data/reviews_merged_no_nulls.csv')
book_profiles=pd.read_csv('data/book_profiles.csv')
#book_profiles = pd.read_csv('data/book_profiles_test.csv')


tropes_list=[
    'age difference',
 'alien',
 'amnesia',
 'antihero',
 'arranged marriage',
 'banter',
 'bdsm',
 "best friend's ex",
 "best friend's sibling",
 'bet',
 'blackmail',
 'blind date',
 'childhood sweethearts',
 'circus',
 'class differences',
 'coming of age',
 'coming out',
 'dark',
 'diversity',
 'enemies to lovers',
 'epistolary',
 'fairytale',
 'fake dating',
 'fake relationship',
 'fated mates',
 'femme fatale',
 'fish out of water',
 'forbidden romance',
 'forced proximity',
 'found family',
 'frenemies',
 'friends to lovers',
 'girl next door',
 'gothic',
 'holiday romance',
 'i hate everyone but you',
 'identical twins',
 'insta love',
 'instalove',
 'interracial',
 'interspecies romance',
 'kidnapping',
 'large families',
 'love at first sight',
 'love potion',
 'love triangle',
 'mafia',
 'magic',
 'magical realism',
 'makeover',
 'man eater',
 'marriage in trouble',
 'marriage of convenience',
 'miscommunication',
 'mistaken identity',
 'morally gray villain',
 'mythology',
 'office',
 'one bed',
 'one night stand',
 'online romance',
 'opposites attract',
 'orphan',
 'pets',
 'post apocalyptic',
 'psychic',
 'redemption',
 'revenge',
 'right person wrong time',
 'rivals',
 'romantic comedy',
 'roommates to lovers',
 'runaway bride',
 'second chance',
 'secret baby',
 "sibling's best friend",
 "sibling's ex",
 'single parent',
 'slow burn',
 'snowbound',
 'soul mates',
 'soulmates',
 'star-crossed lovers',
 'stuck together',
 'student/teacher',
 'superpowers',
 'taboo',
 'the heroes quest',
 'the one that got away',
 'time travel',
 'two person love triangle',
 'ugly duckling',
 'unrequited love',
 'vegas wedding',
 'virgin',
 'wallflower',
 'widow',
 'widower',
 'the chosen one',
 'royalty'
]

reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
book_profiles = book_profiles.loc[:, ~book_profiles.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

links=reviews.url.unique()

def map_tropes(i):
    r_str=""
    for r in reviews.loc[reviews.url==i,'review'].values:
        if(not (re.match('^[0-9*#+.,> -/]+$',r))):
            r_str+=r
    new_str = re.sub(r'[^a-zA-Z]', ' ', r_str)
    re_low=[x.lower() for x in new_str.split()]
    tropes=', '.join(list(set(re_low).intersection(tropes_list)))
    print(tropes)
    book_profiles.loc[book_profiles.link==i, 'tropes']=tropes
    return tropes 

list(map(map_tropes, links))
#book_profiles.to_csv('data/tropes_test.csv')
book_profiles.to_csv('data/tropes.csv')
