import pandas as pd
#clean_book = pd.read_csv('data/after_encoding/clean_book_data.csv')
clean_book = pd.read_csv('data/no_extra_space.csv')

def delete_duplicates(genre):
    genre_list = genre.split(',')
    genre_list = list(dict.fromkeys(genre_list))
    return ','.join(genre_list)

clean_book['genre'] = clean_book['genre'].apply(delete_duplicates)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

def map_genre(genre):
    genre_list = genre.split(',')
    print(genre_list)
    genre_list = list(dict.fromkeys(genre_list))
    if 'North American Hi...' in genre_list:
        genre_list.remove('North American Hi...')
        genre_list.append('North American History')
    elif 'Scandinavian Lite...' in genre_list:
        genre_list.remove('Scandinavian Lite...')
        genre_list.append('Scandinavian Literature')
    elif 'International Rel...' in genre_list:
        genre_list.remove('International Rel...')
        genre_list.append('International Relations')
    elif 'International Dev...' in genre_list:
        genre_list.remove('International Dev...')
        genre_list.append('International Development')
    elif 'Science Fiction R...' in genre_list:
        genre_list.remove('Science Fiction R...')
        genre_list.append('Science Fiction Romance')
    elif 'Democratic Republic Of The ...' in genre_list:
        genre_list.remove( 'Democratic Republic Of The ...')
        genre_list.append('Democratic Republic of the Congo')
    elif 'Complementary Med...' in genre_list:
        genre_list.remove('Complementary Med...')
        genre_list.append('Complementary Medicine')
    return ','.join(genre_list)

clean_book['genre'] = clean_book['genre'].apply(map_genre)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('data/no_extra_space_clean.csv', encoding='utf-8')