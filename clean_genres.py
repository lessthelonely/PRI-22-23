import pandas as pd
clean_book = pd.read_csv('data/after_encoding/clean_book_data.csv')

def map_genre(genre):
    genre_list = genre.split(',')
    genre_list = list(dict.fromkeys(genre_list))
    return ','.join(genre_list)

clean_book['genre'] = clean_book['genre'].apply(map_genre)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('data/after_encoding/clean_book_data.csv', encoding='utf-8')