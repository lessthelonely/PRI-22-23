FROM solr:8.10

# Copy synonyms file
COPY synonyms.txt /data/synonyms.txt

# Copy files
COPY everything_part_1_mood.json /data/everything_part_1_mood.json
COPY everything_part_2_mood.json /data/everything_part_2_mood.json
COPY everything_part_3_mood.json /data/everything_part_3_mood.json
COPY everything_part_4_mood.json /data/everything_part_4_mood.json
COPY everything_part_5_mood.json /data/everything_part_5_mood.json
COPY everything_part_6_mood.json /data/everything_part_6_mood.json
COPY everything_part_7_mood.json /data/everything_part_7_mood.json
COPY everything_part_8_mood.json /data/everything_part_8_mood.json
COPY everything_part_9_mood.json /data/everything_part_9_mood.json
COPY everything_part_10_mood.json /data/everything_part_10_mood.json
COPY everything_part_11_mood.json /data/everything_part_11_mood.json
COPY everything_part_12_mood.json /data/everything_part_12_mood.json
COPY everything_part_13_mood.json /data/everything_part_13_mood.json
COPY everything_part_14_mood.json /data/everything_part_14_mood.json
COPY everything_part_15_mood.json /data/everything_part_15_mood.json
COPY everything_part_16_mood.json /data/everything_part_16_mood.json
COPY everything_part_17_mood.json /data/everything_part_17_mood.json
COPY everything_part_18_mood.json /data/everything_part_18_mood.json


# Copy schema file
COPY books_schema.json /data/books_schema.json

COPY startup.sh ./scripts/startup.sh

ENTRYPOINT ["./scripts/startup.sh"]
