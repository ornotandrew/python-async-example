const express = require('express');
const users = require('./users.json');

const app = express();

const pageSize = 10;

app.get('/users', (req, res) => {
  const { page } = req.query;
  res.status(200).json(users.slice((page - 1) * pageSize, page * pageSize));
});

app.listen(3000);
