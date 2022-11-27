const express = require('express');
const router = express.Router();
const controller = require('../controllers/book');

router.get('/:id', controller.getBookByID);

module.exports = router;