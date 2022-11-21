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
}' http://localhost:8983/solr/goodreads/config

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