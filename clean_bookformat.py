
import pandas as pd
clean_book = pd.read_csv('data/current_data.csv')

def map_bookformat(bookformat):
    if bookformat=='Hardback' or bookformat=='Pasta Dura' or bookformat=='Capa Dura' or bookformat=='Relié' or bookformat=='Hardcover In Dust Jacket' or bookformat=='Hardcover in dust jacket' or bookformat=='Cloth Hardcover' or bookformat=='Cloth' or bookformat=='cloth' or bookformat=='Hardcover, Slipcased' or bookformat=='Over-Sized 12"W X 16"H Hardcover' or bookformat=='Gebunden' or bookformat== 'Hardcover ' or bookformat=='Gebundene Ausgabe' or bookformat=='単行本' or bookformat=='Inbunden' or bookformat=='Casebound' or bookformat=='Slipcased Hardcover' or bookformat=='Pasta dura' or bookformat=='hardcover' or bookformat=='Capa dura' or bookformat=='Over-Sized 12"W x 16"H Hardcover' or bookformat=='hardback':
        return 'Hardcover'
    elif bookformat=='Broschiert' or  bookformat== 'Broché' or bookformat=='文庫' or bookformat=='Capa Comum' or bookformat == 'Sewn Paperback With Dust Jacket' or bookformat == 'Pasta Blanda' or bookformat == 'Saddle-Stitched Paperback == 120 X 190 Mm' or bookformat=='paperback' or bookformat=='Capa comum' or bookformat=='Sewn paperback with dust jacket' or bookformat=='Pasta blanda' or bookformat=='Saddle-stitched paperback' or bookformat=='120 x 190 mm':
        return 'Paperback'
    elif bookformat=='Hardcover, Paperback':
        return 'Paperback And Deluxe Hardcover'
    elif bookformat=='Mass_Market' or bookformat=='Mass Market' or bookformat=='mass_market' or bookformat=='Perfect Paperback' or bookformat=='perfect' or bookformat=='Perfect' or bookformat=='Taschenbuch' or bookformat == 'Poche' or bookformat == 'Softcover' or bookformat== 'Soft Cover' or bookformat=='pocket' or bookformat=='soft cover' or bookformat=='softcover' or bookformat=='Pocket':
        return 'Mass Market Paperback'
    elif bookformat=='Textbook Binding':
        return 'Textbook'
    elif bookformat=='Board Book' or bookformat=='Board' or bookformat=='Board book':
        return 'Board Books'
    elif bookformat=='Nook' or bookformat=='Kindle Edition' or bookformat=='ebook':
        return 'Ebook'
    elif bookformat=='Audio Cd' or bookformat=='Audio' or bookformat=='Audio Cassette' or bookformat == 'Mp3 Book' or bookformat== 'Mp3 Cd' or bookformat == 'Audio Play' or bookformat == 'Audible Audio' or bookformat == 'Audiocd' or bookformat== 'Cd-Rom' or bookformat == 'Kindle Edition With Audio/Video' or bookformat=='Dvd' or bookformat== 'Dvd (Ntsc)' or bookformat=='Audio CD' or bookformat=='DVD (NTSC)' or bookformat=='MP3 Book' or bookformat=='MP3 CD' or bookformat=='DVD' or bookformat=='Kindle Edition with Audio/Video' or bookformat=='CD-ROM':
        return 'Audiobook'
    elif bookformat=='Spiral' or bookformat=='Spiral=Bound' or bookformat=='spiral=bound':
        return 'Spiral-Bound'
    elif bookformat=='Boxed Set - Hardcover' or bookformat== 'Bookprint' or bookformat == 'Boxed Collection' or bookformat=='Boxed set':
        return 'Boxed Set'
    elif bookformat=='Library':
        return 'Library Binding'
    elif bookformat=='Comic' or bookformat=='コミック':
        return 'Comics'
    elif bookformat=='Brochura':
        return 'Pamphlet'
    elif bookformat== '78 Card Tarot Deck':
        return 'Deck of 78 Tarot Cards'
    elif bookformat=='Paperback W/Cd' or bookformat=='Paperback with Cd Rom' or bookformat=='Paperback w/ CD' or bookformat=='Paperback with CD Rom':
        return 'Paperback with CD'
    elif bookformat=='Loose Leaf' or bookformat=='Looseleaf' or bookformat=='paper':
        return 'Paper'
    elif bookformat=='3-Ring Binder' or bookformat=='3-ring Binder':
        return 'Ringbound'
    elif bookformat=='Tarot Cards & Book' or bookformat=='Tarot Deck And Booklet' or bookformat== 'Tarot Deck & Booklet' or bookformat=='Tarot Deck and Booklet':
        return 'Tarot Deck & Book'
    elif bookformat=='Paperback with deck of cards':
        return 'Paperback with Deck of Cards'
    else:
        return bookformat

clean_book['bookformat'] = clean_book['bookformat'].apply(map_bookformat)
clean_book = clean_book.loc[:, ~clean_book.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
clean_book.to_csv('data/current_data_after.csv')