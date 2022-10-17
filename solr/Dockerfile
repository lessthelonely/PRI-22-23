FROM solr:8.10

COPY current_data_13_10.json /data/current_data_13_10.json

COPY simple_schema.json /data/simple_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
