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