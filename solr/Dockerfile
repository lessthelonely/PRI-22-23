FROM solr:8.10

COPY current_data.json /data/current_data.json

COPY simple_schema.json /data/simple_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
