const express = require('express');
const { hellow } = require('../controller/hellow');
const router = express.Router();

router.get('/main',hellow);

module.exports = router;