import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")
example = "Debut author Sally Thorne bursts on the scene with a hilarious and sexy workplace comedy all about that thin, fine line between hate and love.Nemesis (n.) 1) An opponent or rival whom a person cannot best or overcome.2) A person’s undoing 3) Joshua TemplemanLucy Hutton has always been certain that the nice girl can get the corner office. She’s charming and accommodating and prides herself on being loved by everyone at Bexley & Gamin. Everyone except for coldly efficient, impeccably attired, physically intimidating Joshua Templeman. And the feeling is mutual.Trapped in a shared office together 40 (OK, 50 or 60) hours a week, they’ve become entrenched in an addictive, ridiculous never-ending game of one-upmanship. There’s the Staring Game. The Mirror Game. The HR Game. Lucy can’t let Joshua beat her at anything—especially when a huge new promotion goes up for the taking.If Lucy wins this game, she’ll be Joshua’s boss. If she loses, she’ll resign. So why is she suddenly having steamy dreams about Joshua, and dressing for work like she’s got a hot date? After a perfectly innocent elevator ride ends with an earth shattering kiss, Lucy starts to wonder whether she’s got Joshua Templeman all wrong.Maybe Lucy Hutton doesn’t hate Joshua Templeman. And maybe, he doesn’t hate her either. Or maybe this is just another game. ​​"

text1=NER(example)
for word in text1.ents:
    print(word.text, word.label_)

displacy.render(text1,style="ent",jupyter=True)