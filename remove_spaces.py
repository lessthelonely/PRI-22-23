import pandas as pd
clean_book = pd.read_csv('data/after_encoding/clean_book_data.csv')


def remove_extra_space(url):
    try:
        title = clean_book.loc[clean_book.link == url, 'title'].values[0]
        clean_book.loc[clean_book.link == url, 'title'] = " ".join(title.split())
        desc = clean_book.loc[clean_book.link == url, 'desc'].values[0]
        clean_book.loc[clean_book.link == url, 'desc'] = " ".join(desc.split())
        author = clean_book.loc[clean_book.link == url, 'author'].values[0]
        clean_book.loc[clean_book.link == url, 'author'] = " ".join(author.split())
    except:
        print(url)

clean_book['link'].apply(remove_extra_space)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('data/after_encoding/clean_book_data.csv', encoding='utf-8')