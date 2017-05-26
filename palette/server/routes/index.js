var express = require('express');
var router = express.Router();

router.use(function(req, res, next) {
  console.log('Received an API request at ' + req.url + '.');
  next();
});

router.use(require('./image'));

module.exports = router;
