from deep_translator import GoogleTranslator
import pandas as pd

df = pd.read_csv('test/goodreads_with_prices.csv')
# print(df.to_string())

for index in df.index:
    #print(index)
    translated = GoogleTranslator(source='auto', target='en').translate(df.loc[index,'title']) # later check if language != english and translate only then
    #df.loc[index,'title'] = translated
    print(str(index + 2) + " " + translated)

print(translated)
