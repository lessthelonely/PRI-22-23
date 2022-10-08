import pandas as pd
clean_book = pd.read_csv('processed/cleaned_genres.csv')

clean_book=clean_book.rename(columns={"bookformat":"book_format"})
clean_book=clean_book.rename(columns={"desc":"description"})
clean_book=clean_book.rename(columns={"img":"cover_img"})
clean_book=clean_book.rename(columns={"pages":"page_count"})
clean_book=clean_book.rename(columns={"reviews":"review_count"})
clean_book=clean_book.rename(columns={"totalratings":"rating_count"})

clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('processed/current_data.csv')
