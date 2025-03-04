import pandas as pd
clean_book = pd.read_csv('processed/cleaned_prices.csv')

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
    elif '漫画' in genre_list:
        genre_list.remove('漫画')
        genre_list.append('Manga')
    elif 'Bande Dessinée' in genre_list:
        genre_list.remove('Bande Dessinée')
        genre_list.append('Comics')
    elif 'Komik' in genre_list:
        genre_list.remove('Komik')
        genre_list.append('Comics')
    elif 'Comics Manga' in genre_list:
        genre_list.remove('Comics Manga')
        genre_list.append('Manga')
    elif 'Comic Book' in genre_list:
        genre_list.remove('Comic Book')
        genre_list.append('Comics')
    elif 'Comics Bd' in genre_list:
        genre_list.remove('Comics Bd')
        genre_list.append('Comics')
    elif 'Comic Book' in genre_list:
        genre_list.remove('Comic Book')
        genre_list.append('Comics')
    elif 'Spider Man' in genre_list:
        genre_list.remove('Spider Man')
        genre_list.append('Spider-Man')
    elif 'X Men' in genre_list:
        genre_list.remove('X Men')
        genre_list.append('X-Men')
    return ','.join(genre_list)

clean_book['genre'] = clean_book['genre'].apply(map_genre)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

def delete_duplicates(genre):
    genre_list = genre.split(',')
    genre_list = list(dict.fromkeys(genre_list))
    return ','.join(genre_list)

clean_book['genre'] = clean_book['genre'].apply(delete_duplicates)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas

clean_book.to_csv('processed/cleaned_genres.csv')