storygraph=[
'Abandonment',
'Ableism',
'Abortion',
'Acephobia',
'Arophobia',
'Addiction',
'Adult/minor relationship',
'Alcohol',
'Alcoholism',
'Animal cruelty',
'Animal death',
'Antisemitism',
'Biphobia',
'Blood',
'Body horror',
'Body shaming',
'Bullying',
'Cancer',
'Cannibalism',
'Car accident',
'Child abuse',
'Child death',
'Chronic illness',
'Classism',
'Colonisation',
'Confinement',
'Cultural appropriation',
'Cursing',
'Deadnaming',
'Death',
'Death of parent',
'Dementia',
'Deportation',
'Domestic abuse',
'Drug abuse',
'Drug use',
'Dysphoria',
'Eating disorder',
'Emotional abuse',
'Excrement',
'Fatphobia',
'Fire',
'Fire injury',
'Forced institutionalization',
'Gaslighting',
'Genocide',
'Gore',
'Grief',
'Gun violence',
'Hate crime',
'Homophobia',
'Incest',
'Infertility',
'Infidelity',
'Injury',
'injury detail',
'Islamophobia',
'Kidnapping',
'Lesbophobia',
'Mass school shootings',
'Medical content',
'Medical trauma',
'Mental illness',
'Miscarriage',
'Misogyny',
'Murder',
'Outing',
'Panic attacks',
'Panic disorders',
'Pedophilia',
'Physical abuse',
'Police brutality',
'Pregnancy',
'Racial slurs',
'Racism',
'Rape',
'Religious bigotry',
'Schizophrenia',
'Psychosis',
'Self harm',
'Sexism',
'Sexual assault',
'Sexual content',
'Sexual harassment',
'Sexual violence',
'Slavery',
'Stalking',
'Suicidal thoughts',
'Suicide',
'Suicide attempt',
'Terminal illness',
'Torture',
'Toxic friendship',
'Toxic relationship',
'Trafficking',
'Transphobia',
'Violence',
'Vomit',
'War',
'Xenophobia'

]


trigger_words= ['Ableism','Abortion',
'Abusive relationship',
'Abuse',
'Acephobia',
'Ageism',
'Alcohol',
'Alcoholism',
'Amputation',
'Animal abuse',
'Animal death',
'Antisemitism',
'Anxiety',
'Assault',
'Attempted murder',
'Attempted rape',
'Bestiality',
'Blood',
'Bones',
'Branding',
'Bullying',
'Cancer',
'Cannibalism',
'Car accident',
'Cheating',
'Child abuse',
'Child death',
'Childbirth',
'Conversion therapy',
'Cults',
'Death',
'Decapitation',
'Demons',
'Depression',
'Divorce',
'Drugs',
'Eating disorder',
'Emesis',
'Emotional abuse',
'Eugenics',
'Famine',
'Fatphobia',
'Fire',
'Genocide',
'Gore',
'Grief',
'Gun violence',
'Hallucinations',
'Homomisia',
'Homophobia',
'Hospitalisation',
'Hostages',
'Harry Potter References',
'Incest',
'Infertility',
'Kidnapping',
'Lesbiphobia',
'Miscarriage',
'Misgendering',
'Micro-Aggressions',
'Misogyny',
'Murder',
'Needles',
'Occult',
'Pedophilia',
'Physical abuse',
'Plague',
'Poisoning',
'Police brutality',
'Pregnancy',
'Profanity',
'Prostitution',
'PTSD',
'Queerphobia',
'Racism',
'Rape',
'Religion',
'Satan/The Devil',
'School shooting',
'Self-harm',
'Sexism',
'Sexual abuse',
'Sexual assault',
'Sexual harassment',
'Sexually explicit scenes',
'Skeletons',
'Slavery',
'Slut shaming',
'Snakes',
'Spiders',
'Stalking',
'Starvation',
'Suicide',
'Terminal illness',
'Terrorism',
'Torture',
'Transmisia',
'Trauma',
'Transphobia',
'Violence',
'War']

for i in trigger_words:
    if i not in storygraph:
        storygraph.append(i)

trigger_warnings=[['Abandonment', 
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
'Snakes', 'Spiders', 'Starvation', 'Terrorism', 'Transmisia', 'Trauma']]