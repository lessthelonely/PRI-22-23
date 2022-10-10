import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")
example = "I absolutely loved the issue where Superman comes to Bludhaven. The book does dovetail with what was happening in No Man's Land over in the Batman books. Dick joining the police force was really inspired. Overall, these are just fun stories. I love how acrobatic Scott McDaniel draws Nightwing and his rogues. They're always flying across rooftops and up the sides of buildings."

text1=NER(example)
for word in text1.ents:
    print(word.text, word.label_)

displacy.render(text1,style="ent",jupyter=True)