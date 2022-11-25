#!/bin/bash

precreate-core books_schema

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Wait for Solr to start
sleep 10

cp /data/synonyms.txt /var/solr/data/books_schema/conf

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
     --data-binary @/data/books_schema.json \
     http://localhost:8983/solr/books_schema/schema

curl -X POST -H 'Content-type:application/json'  -d '{
  "add-searchcomponent": {
    "name": "suggest",
    "class": "solr.SuggestComponent",
    "suggester": {
        "name": "mySuggester",
        "lookupImpl": "FuzzyLookupFactory",
        "dictionaryImpl": "DocumentDictionaryFactory",
        "field": "title_suggest",
        "suggestAnalyzerFieldType": "text_general",
        "exactMatchFirst": "true",
        "buildOnStartup": "true"
    }
  }
}' http://localhost:8983/solr/books_schema/config

curl -X POST -H 'Content-type:application/json'  -d '{
  "add-requesthandler": {
    "name": "/suggest",
        "class": "solr.SearchHandler",
        "startup": "lazy",
        "defaults": {
            "suggest": true,
            "suggest.count": 20,
            "suggest.dictionary": "mySuggester"
        },
        "components": [
            "suggest"
        ]
  }
}' http://localhost:8983/solr/books_schema/config

curl -X POST -H 'Content-type:application/json'  -d '{
  "update-requesthandler": {
      "name": "/select",
      "class": "solr.SearchHandler",
      "defaults": {
        "wt": "json", 
        "indent": true,
        "df": "search",
        "rows": 10,
        "spellcheck": "on",
        "spellcheck.collate": "true"
      },
      "last-components": [
        "spellcheck"
      ]
    }
}' http://localhost:8983/solr/books_schema/config

curl -X POST -H 'Content-type:application/json'  -d '{
   "update-searchcomponent": {
      "name": "spellcheck",
      "class": "solr.SpellCheckComponent",
      "spellchecker": {
        "classname": "solr.IndexBasedSpellChecker",
        "spellcheckIndexDir": "./spellchecker",
        "field": "spell",
        "buildOnCommit": "true"
      }
    }
}' http://localhost:8983/solr/books_schema/config

# Populate collection
bin/post -c books_schema everything_part_1_mood.json
bin/post -c books_schema everything_part_2_mood.json
bin/post -c books_schema everything_part_3_mood.json
bin/post -c books_schema everything_part_4_mood.json
bin/post -c books_schema everything_part_5_mood.json
bin/post -c books_schema everything_part_6_mood.json
bin/post -c books_schema everything_part_7_mood.json
bin/post -c books_schema everything_part_8_mood.json
bin/post -c books_schema everything_part_9_mood.json
bin/post -c books_schema everything_part_10_mood.json
bin/post -c books_schema everything_part_11_mood.json
bin/post -c books_schema everything_part_12_mood.json
bin/post -c books_schema everything_part_13_mood.json
bin/post -c books_schema everything_part_14_mood.json
bin/post -c books_schema everything_part_15_mood.json
bin/post -c books_schema everything_part_16_mood.json
bin/post -c books_schema everything_part_17_mood.json
bin/post -c books_schema everything_part_18_mood.json

# Restart in foreground mode so we can access the interface
solr restart -f
