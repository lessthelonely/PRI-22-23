const axios = require('axios');

const solr = axios.create({
    baseURL: 'http://localhost:8983/solr/books_schema',
    timeout: 1000
})

module.exports = solr;