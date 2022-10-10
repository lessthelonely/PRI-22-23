import spacy
from rake_nltk import Rake
import en_core_web_sm
from  spacy.lang.en.stop_words import STOP_WORDS
nlp = en_core_web_sm.load()
#nlp = spacy.load('en_core_web_sm')

# To build a list of stop words for filtering
stopwords = list(STOP_WORDS)
rake_nltk_var = Rake()
example = " I loved this book! I found it hard to tear myself away at times but I would force myself in the name of sleep. While I enjoyed the writing and the story itself, I did get annoyed at times during some of Lucy's internal dialogue. I mean, I get it, she was conflicted but it seemed like she took WAY too long to realize what was going on. Even still, that's how we all can be in life sometimes so I get the reasoning for it and didn't feel it took away from the reading experience. Ultimately, this was one of those books that I wished wouldn't end. Maybe I am more of a romance reader than I thought! "

#pat = r'\b(?:{})\b'.format('|'.join(stopwords))
#example_no_stopwords = example.replace(pat, '')
#example_no_stopwords = example_no_stopwords.replace(r'\s+', ' ')

rake_nltk_var.extract_keywords_from_text(example)
keyword_extracted=rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)