#!/bin/bash

precreate-core books
precreate-core reviews
precreate-core profiles

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
# curl -X POST -H 'Content-type:application/json' \
#     --data-binary @/data/simple_schema.json \
#     http://localhost:8983/solr/courses/schema

# Populate collection
bin/post -c books /data/current_book_data_25_10.json
bin/post -c reviews /data/reviews_part_1.json
bin/post -c reviews /data/reviews_part_2.json
bin/post -c reviews /data/reviews_part_3.json
bin/post -c reviews /data/reviews_part_4.json
bin/post -c reviews /data/reviews_part_5.json
bin/post -c reviews /data/reviews_part_6.json
bin/post -c reviews /data/reviews_part_7.json
bin/post -c reviews /data/reviews_part_8.json
bin/post -c reviews /data/reviews_part_9.json
bin/post -c reviews /data/reviews_part_10.json
bin/post -c reviews /data/reviews_part_11.json
bin/post -c reviews /data/reviews_part_12.json
bin/post -c reviews /data/reviews_part_13.json
bin/post -c reviews /data/reviews_part_14.json
bin/post -c reviews /data/reviews_part_15.json
bin/post -c reviews /data/reviews_part_16.json
bin/post -c reviews /data/reviews_part_17.json
bin/post -c reviews /data/reviews_part_18.json
bin/post -c profiles /data/book_profiles_17_10.json

# Restart in foreground mode so we can access the interface
solr restart -f
