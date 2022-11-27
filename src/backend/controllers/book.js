const solr = require('../config');

async function getAllBooks(req, res) {
    let params = new URLSearchParams();
    params.append("q", "*:*");
    params.append("qt", "");
    params.append("indent", "true");
    params.append("q.op", "OR");
    //params.append("defType", "lucene");
    //params.append("wt", "json");
    //params.append("rows", "10");
    //params.append("start", "0");
    //params.append("qf", "id,title,author,genre,price,description");
   
  
    solr
      .get("/select", { params: params })
      .then(function (resp) {
        const result = [];
        
        resp.data.response.docs.forEach((item) => {
          result.push(item);
        })
        return res.status(200).send(result);
      })
      .catch((error) => {
        console.log(error);
        return res.status(400).json("Something went wrong!");
      });
}

async function getBookByID(req, res) {
    const id = req.params.id;
    const params = {
      q: `id:${id}`,
      indent: "true",
      "q.op": "AND",
    };
  
    solr
      .get("/select", { params: params })
      .then(function (resp) {
        return res.status(200).send(resp.data.response.docs[0]);
      })
      .catch((error) => {
        console.log(error);
        return res.status(400).json("Something went wrong!");
      });
}

module.exports = {
    getAllBooks,
    getBookByID
};