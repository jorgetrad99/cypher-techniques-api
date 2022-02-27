/* const PythonShell = require('python-shell');

let options = {
  scriptPath: 'path',
};

PythonShell.run('vigenere.py', options, (err, res) => {
  if (err) console.err;
  if (res) console.res;
}); */
const { spawn } = require('child_process');

const actionHandler = (/* actionFlag */) => {
  const process = spawn('python', ['./handler.py' /* , actionFlag */]);

  process.stdout.on('data', (data) => {
    console.log(data.toString());
  });
};

module.exports = actionHandler;
