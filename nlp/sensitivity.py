import re
import pandas as pd

#reviews= pd.read_csv('data/reviews_test.csv')
reviews=pd.read_csv('data/reviews_merged_no_nulls.csv')
book_profiles=pd.read_csv('data/book_profiles.csv')

trigger_warnings=['Abandonment', 
'Ableism', 'Abortion', 'Acephobia', 
'Arophobia', 'Addiction', 'Adult/minor relationship', 
'Alcohol', 'Alcoholism', 'Animal cruelty', 'Animal death',
'Antisemitism', 'Biphobia', 'Blood', 'Body horror', 'Body shaming', 
'Bullying', 'Cancer', 'Cannibalism', 'Car accident', 'Child abuse', 
'Child death', 'Chronic illness', 'Classism', 'Colonisation', 'Confinement', 
'Cultural appropriation', 'Cursing', 'Deadnaming', 'Death', 'Death of parent', 
'Dementia', 'Deportation', 'Domestic abuse', 'Drug abuse', 'Drug use', 'Dysphoria',
'Eating disorder', 'Emotional abuse', 'Excrement', 'Fatphobia', 'Fire', 'Fire injury',
'Forced institutionalization', 'Gaslighting', 'Genocide', 'Gore', 'Grief', 
'Gun violence', 'Hate crime', 'Homophobia', 'Incest', 'Infertility', 'Infidelity', 
'Injury', 'Injury detail', 'Islamophobia', 'Kidnapping', 'Lesbophobia', 
'Mass school shootings', 'Medical content', 'Medical trauma', 'Mental illness', 
'Miscarriage', 'Misogyny', 'Murder', 'Outing', 'Panic attacks', 'Panic disorders', 
'Pedophilia', 'Physical abuse', 'Police brutality', 'Pregnancy', 'Racial slurs', 
'Racism', 'Rape', 'Religious bigotry', 'Schizophrenia', 'Psychosis', 'Self harm', 
'Sexism', 'Sexual assault', 'Sexual content', 'Sexual harassment', 'Sexual violence', 
'Slavery', 'Stalking', 'Suicidal thoughts', 'Suicide', 'Suicide attempt', 'Terminal illness', 
'Torture', 'Toxic friendship', 'Toxic relationship', 'Trafficking', 'Transphobia', 'Violence', 
'Vomit', 'War', 'Xenophobia', 'Abusive relationship', 'Abuse', 'Ageism', 'Amputation', 
'Anxiety', 'Assault', 'Attempted murder', 'Attempted rape', 'Bestiality', 'Bones', 'Branding', 
'Cheating', 'Childbirth', 'Conversion therapy', 'Cults', 'Decapitation', 'Demons', 'Depression', 
'Divorce', 'Drugs', 'Emesis', 'Eugenics', 'Famine', 'Hallucinations', 'Homomisia', 'Hospitalisation', 
'Hostages', 'Harry Potter References', 'Lesbiphobia', 'Misgendering', 'Micro-Aggressions', 'Needles', 
'Occult', 'Plague', 'Poisoning', 'Profanity', 'Prostitution', 'PTSD', 'Queerphobia', 'Religion', 
'Satan/The Devil', 'School shooting', 'Self-harm', 'Sexual abuse', 'Skeletons', 'Slut shaming',
'Snakes', 'Spiders', 'Starvation', 'Terrorism', 'Transmisia', 'Trauma']

trigger_low=[x.lower() for x in trigger_warnings]


reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
book_profiles = book_profiles.loc[:, ~book_profiles.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

links=reviews.url.unique()

def map_triggers(i):
    r_str=""
    for r in reviews.loc[reviews.url==i,'review'].values:
        if(not (re.match('^[0-9*#+.,> -/]+$',r))):
            r_str+=r
    new_str = re.sub(r'[^a-zA-Z]', ' ', r_str)
    re_low=[x.lower() for x in new_str.split()]
    triggers=', '.join(list(set(re_low).intersection(trigger_low)))
    print(triggers)
    book_profiles.loc[book_profiles.link==i, 'sensitivity']=triggers
    return triggers 
   
list(map(map_triggers,links))
book_profiles.to_csv('data/trigger.csv')
#example="This took me approximately a million years to listen to the audiobook, but that's not the book's fault that's just me being not lazy.Despite taking me a long time to read, I think that the pacing did seem consistent as there was pretty much constant action, even in moments of inaction.It dealt with grief and trauma very well, in a way I'd never seen before.The start of a super cool series I think!"
#new_str = re.sub(r'[^a-zA-Z]', ' ', example)
#review_str=[]
#new_str=new_str.split()

'''
review_str=[]
for i in reviews['review']:
    new_str = re.sub(r'[^a-zA-Z]', ' ', i)
    print(new_str.split())
    print('\n')
    review_str+=new_str.split()

re_low=[x.lower() for x in review_str]
trigger_low=[x.lower() for x in trigger_warnings]

print(list(set(re_low).intersection(trigger_low)))
print(', '.join(list(set(re_low).intersection(trigger_low))))
'''