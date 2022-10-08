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
	python3 collect_scripts/book_depository.py #get prices from book depository
	python3 collect_scripts/goodreads.py #get missing pages from goodreads
	python3 collect_scripts/book_depository_pages.py #further complete missing pages with book depository scraping
	python3 collect_scripts/goodreads_reviews_multithread.py #get reviews from goodreads
	python3 collect_scripts/goodreads_language_multithread.py #get books' languages from goodreads

process:
	#Translate titles, descriptions and reviews
    #Clean descriptions, titles, reviews, genres and book formats
	mkdir processed
	python3 processing_scripts/translator_review.py #translates reviews
	python3 processing_scripts/clean_reviews.py #deletes reviews that were unable to be translated due to them being over 5k characters
	python3 processing_scripts/translator.py #translates titles
	python3 processing_scripts/cleaning_titles.py #puts titles in their correct cells
	python3 processing_scripts/remove_spaces.py #removes extra spaces present in descriptions, mainly
	python3 processing_scripts/translator_description.py #translates descriptions
	python3 processing_scripts/clean_desc.py #deletes book entries of books with descriptions that were unable to be translated due to them being over 5k characters
	python3 processing_scripts/join_tables.py #adds table with the extra column "price" to the table were we have been cleaning data
	sh processing_scripts/clean_bookformat.sh #cleans column "bookformat"
	python3 processing_scripts/clean_prices.py #cleans column "price"
	python3 processing_scripts/clean_genres.py #cleans column "genre"
	python3 processing_scripts/remove_old_reviews.py #removes reviews from books that were removed during the cleaning process
	python3 processing_scripts/change_column_names.py #change column names for more descriptive ones

analyze:   
	mkdir analysis
	mv "notebook.ipynb" "analysis"
	jupyter nbconvert --to python analysis/notebook.ipynb

