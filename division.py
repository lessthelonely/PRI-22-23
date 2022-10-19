import numpy as np
import pandas as pd 

reviews=pd.read_csv('solr/reviews_merged_no_nulls.csv')
reviews = reviews.loc[:, ~reviews.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
groups=np.array_split(reviews, 18)

g1=groups[0]
g2=groups[1]
g3=groups[2]
g4=groups[3]
g5=groups[4]
g6=groups[5]
g7=groups[6]
g8=groups[7]
g9=groups[8]
g10=groups[9]
g11=groups[10]
g12=groups[11]
g13=groups[12]
g14=groups[13]
g15=groups[14]
g16=groups[15]
g17=groups[16]
g18=groups[17]

g1 = g1.loc[:, ~g1.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g1.to_csv('solr/reviews_part_1.csv')

g2 = g2.loc[:, ~g2.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g2.to_csv('solr/reviews_part_2.csv')

g3 = g3.loc[:, ~g3.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g3.to_csv('solr/reviews_part_3.csv')

g4 = g4.loc[:, ~g4.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g4.to_csv('solr/reviews_part_4.csv')

g5 = g5.loc[:, ~g5.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g5.to_csv('solr/reviews_part_5.csv')

g6 = g6.loc[:, ~g6.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g6.to_csv('solr/reviews_part_6.csv')

g7 = g7.loc[:, ~g7.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g7.to_csv('solr/reviews_part_7.csv')

g8 = g8.loc[:, ~g8.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g8.to_csv('solr/reviews_part_8.csv')

g9 = g9.loc[:, ~g9.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g9.to_csv('solr/reviews_part_9.csv')

g10 = g10.loc[:, ~g10.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g10.to_csv('solr/reviews_part_10.csv')

g11 = g11.loc[:, ~g11.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g11.to_csv('solr/reviews_part_11.csv')

g12 = g12.loc[:, ~g12.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g12.to_csv('solr/reviews_part_12.csv')

g13 = g13.loc[:, ~g13.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g13.to_csv('solr/reviews_part_13.csv')

g14 = g14.loc[:, ~g14.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g14.to_csv('solr/reviews_part_14.csv')

g15 = g15.loc[:, ~g15.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g15.to_csv('solr/reviews_part_15.csv')

g16 = g16.loc[:, ~g16.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g16.to_csv('solr/reviews_part_16.csv')

g17 = g17.loc[:, ~g17.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g17.to_csv('solr/reviews_part_17.csv')

g18 = g18.loc[:, ~g18.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
g18.to_csv('solr/reviews_part_18.csv')