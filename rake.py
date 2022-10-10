import spacy
from rake_nltk import Rake
import en_core_web_sm
from  spacy.lang.en.stop_words import STOP_WORDS
nlp = en_core_web_sm.load()
#nlp = spacy.load('en_core_web_sm')

# To build a list of stop words for filtering
stopwords = list(STOP_WORDS)
rake_nltk_var = Rake()
example = "I absolutely loved the issue where Superman comes to Bludhaven. The book does dovetail with what was happening in No Man's Land over in the Batman books. Dick joining the police force was really inspired. Overall, these are just fun stories. I love how acrobatic Scott McDaniel draws Nightwing and his rogues. They're always flying across rooftops and up the sides of buildings."

#pat = r'\b(?:{})\b'.format('|'.join(stopwords))
#example_no_stopwords = example.replace(pat, '')
#example_no_stopwords = example_no_stopwords.replace(r'\s+', ' ')

rake_nltk_var.extract_keywords_from_text(example)
keyword_extracted=rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)