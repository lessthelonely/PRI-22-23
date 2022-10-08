# Makefile

# Run ``make`` to execute pipeline
# Run ``make clean`` to delete data files

# Clean all, remove all folders.
clean:
	rm -rf dataset processed analysis #eliminate the folders created

all: clean setup collect process analyze

# Install all dependencies in order to run the scripts
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
	pip install numpy
	pip install jupyter

collect:
    # Data Collection using web scraping
	mkdir dataset
	python3 book_depository.py #get prices from book depository
	python3 goodreads.py #get missing pages from goodreads
	python3 book_depository_pages.py #further complete missing pages with book depository scraping
	python3 goodreads_reviews_multithread.py #get reviews from goodreads
	python3 goodreads_language_multithread.py #get books' languages from goodreads

process:
	#Translate titles, descriptions and reviews
    #Clean descriptions, titles, reviews, genres and book formats
	mkdir processed
	python3 translator_review.py #translates reviews
	python3 clean_reviews.py #deletes reviews that were unable to be translated due to them being over 5k characters
	python3 remove_spaces.py #removes extra spaces present in descriptions, mainly
	python3 translator.py #translates titles
	python3 cleaning_titles.py #puts titles in their correct cells
	python3 translator_description.py #translates descriptions
	python3 clean_desc.py #deletes book entries of books with descriptions that were unable to be translated due to them being over 5k characters
	python3 join_tables.py #adds table with the extra column "price" to the table were we have been cleaning data
	sh clean_bookformat.sh #cleans column "bookformat"
	python3 clean_prices.py #cleans column "price"
	python3 clean_genres.py #cleans column "genre"
	python3 remove_old_reviews.py #removes reviews from books that were removed during the cleaning process

analyze:   
	mkdir analysis
	mv "notebook.ipynb" "analysis"
	jupyter nbconvert --to python analysis/notebook.ipynb
	

