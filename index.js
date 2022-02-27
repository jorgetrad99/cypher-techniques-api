const express = require('express');
/* const actionHandler = require('./utils/actionHandler'); */
const { spawn } = require('child_process');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello, this is the server');
});

app.get('/vigenere/:message&:key', (req, res) => {
  const { message, key } = req.params;

  const process = spawn('python', [
    'utils/cypher_techniques/vigenere.py',
    message,
    key,
  ]);
  process.stdout.on('data', (data) => {
    res.json(JSON.parse(data.toString()));
  });

  process.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
});

app.listen(port, () => {
  console.log('Mi port' + port);
});