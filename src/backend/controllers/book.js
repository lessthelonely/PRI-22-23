const solr = require('../config');

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
    getBookByID
};