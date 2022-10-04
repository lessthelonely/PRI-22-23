# Makefile

# Run ``make`` to execute pipeline
# Run ``make clean`` to delete data files

# Data destination folder
path := data 
og_data := path/GoodReads_100k_books.csv

# Starting target rule 'all'
# Processes all programmes defined
all: setup data/cleaned_reviews.csv data/clean_book_data.csv

setup:
	pip install requests
	pip install pandas
	pip install langdetect
	pip install regex
	pip install beautifulsoup4
	pip install urllib3
	pip install googletrans
	pip install html5lib
	pip install future

data/goodreads_with_prices.csv: og_data
	python book_depository.py

data/goodreads_with_pages.csv: og_data
	python goodreads.py

data/book_depository_pages.csv: data/goodreads_with_pages.csv
	python book_depository_pages.py

data/goodreads_with_review.csv: data/goodreads_with_prices.csv
	python goodreads_reviews_multithread.py

data/translated_review.csv: data/goodreads_with_review.csv
	python translator_review.py

data/cleaned_reviews.csv: data/translated_review.csv
	python clean_reviews.py

data/goodreads_with_language.csv: data/goodreads_with_prices.csv
	python goodreads_language_multithread.py

data/goodreads_titles_translated.csv: data/goodreads_with_language.csv
	python translator.py

data/clean_titles.csv: data/goodreads_titles_translated.csv data/goodreads_with_prices.csv
	python cleaning_titles.py

data/translate_description.csv: data/clean_titles.csv
	python translator_description.py

data/cleaned_desc: data/translate_description.csv
	python clean_desc.py

data/joined_book_data.csv: data/cleaned_desc.csv data/book_depository_pages.csv
	python join_tables.py

data/clean_book_data.csv: data/joined_book_data.csv
	python clean_data.py

# Create data folder.
$(path):
	mkdir $(path)
	echo "Created '$(path)' folder"

# Clean all, remove all folders.
clean:
	rm -Rf $(path)
	echo "Deleted '$(path)' folder"

# EOF

