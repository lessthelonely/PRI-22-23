import math
import nltk
nltk.download('punkt')
from operator import itemgetter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

stop_words= set(stopwords.words('english'))

example = "I absolutely loved the issue where Superman comes to Bludhaven. The book does dovetail with what was happening in No Man's Land over in the Batman books. Dick joining the police force was really inspired. Overall, these are just fun stories. I love how acrobatic Scott McDaniel draws Nightwing and his rogues. They're always flying across rooftops and up the sides of buildings."

word_list = example.split()
num_words=word_tokenize(example)
print(len(num_words))
num_sentences=sent_tokenize(example)
print(len(num_sentences))

tf_score={}
for word in word_list:
    word=word.replace('.','')
    if word not in stop_words:
        if word in tf_score:
            tf_score[word]+=1
        else:
            tf_score[word]=1

tf_score.update((x,y/int(len(num_words))) for x,y in tf_score.items())
print('TF-SCORE')
print(tf_score)

def check_sent(word, sentences):
    final=[all([w in x for w in word]) for x in sentences]
    sent_len =[sentences[i] for i in range(0,len(final)) if final[i]]
    return int(len(sent_len))

idf_score={}
for word in word_list:
    word=word.replace('.','')
    if word not in stop_words:
        if word in idf_score:
            idf_score[word]=check_sent(word, num_sentences)
        else:
            idf_score[word]=1

idf_score.update((x, math.log(int(len(num_sentences)/y))) for x,y in idf_score.items())
print('IDF-SCORE:')
print(idf_score)
tf_idf_score = {key:tf_score[key]*idf_score.get(key,0) for key in tf_score.keys()}
print('TF-IDF-SCORE:')
print(tf_idf_score)

def get_top_n(dict_elem, n):
    result=dict(sorted(dict_elem.items(), key=itemgetter(1), reverse=True)[:n])
    return result

print('Find the top-5 words of importance in a sentence')
print(get_top_n(tf_idf_score,5))