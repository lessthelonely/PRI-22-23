const express = require('express');
const cookieParser = require('cookie-parser');
const cors = require('cors');

const port = 3001;

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(cors());
/*
var xml2js = require('xml2js');
var parser = new xml2js.Parser();

axios = require('axios');



app.get('/', (req, res) => {
    axios.get('https://lookup.dbpedia.org/api/search?query=Barack%20Obama').then((res) => {
       var xmlfile = res.data;
         parser.parseString(xmlfile, function (err, result) {
            var description = result;
            console.log(description);  
            //res.send(description);
         });
});
});
*/
const book_routes = require('./routes/book');
app.use('/book', book_routes);

app.use((req, res, next) => {
    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', '*');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});