FROM solr:8.10

COPY ./data/current_book_data_25_10.json /data/current_book_data_25_10.json
COPY ./data/book_profiles_17_10.json /data/book_profiles_17_10.json
COPY ./data/reviews_part_1.json /data/reviews_part_1.json
COPY ./data/reviews_part_2.json /data/reviews_part_2.json
COPY ./data/reviews_part_3.json /data/reviews_part_3.json
COPY ./data/reviews_part_4.json /data/reviews_part_4.json
COPY ./data/reviews_part_5.json /data/reviews_part_5.json
COPY ./data/reviews_part_6.json /data/reviews_part_6.json
COPY ./data/reviews_part_7.json /data/reviews_part_7.json
COPY ./data/reviews_part_8.json /data/reviews_part_8.json
COPY ./data/reviews_part_9.json /data/reviews_part_9.json
COPY ./data/reviews_part_10.json /data/reviews_part_10.json
COPY ./data/reviews_part_11.json /data/reviews_part_11.json
COPY ./data/reviews_part_12.json /data/reviews_part_12.json
COPY ./data/reviews_part_13.json /data/reviews_part_13.json
COPY ./data/reviews_part_14.json /data/reviews_part_14.json
COPY ./data/reviews_part_15.json /data/reviews_part_15.json
COPY ./data/reviews_part_16.json /data/reviews_part_16.json
COPY ./data/reviews_part_17.json /data/reviews_part_17.json
COPY ./data/reviews_part_18.json /data/reviews_part_18.json

# COPY simple_schema.json /data/simple_schema.json

COPY ./startup.sh ./scripts/startup.sh

ENTRYPOINT ["./scripts/startup.sh"]
