const express = require('express');
const router = express.Router();
const controller = require('../controllers/book');

router.get('/:id', controller.getBookByID);
router.get('/', controller.getAllBooks);

module.exports = router;