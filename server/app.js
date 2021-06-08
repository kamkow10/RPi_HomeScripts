const express = require('express');
const child_process = require('child_process');
const app = express();
var cors = require('cors');
const port = 3000;
let currentPythonProcess;
let isCurrentPythonProcessClosed;

app.use(cors());

async function killLastPythonProcess() {
    if (currentPythonProcess) {
        currentPythonProcess.kill();
        while (!isCurrentPythonProcessClosed) {
            await new Promise(r => setTimeout(r, 100));
        }
    }
}

app.post('/forward', async (req, res) => {
    await killLastPythonProcess();
    console.log('forward');
    currentPythonProcess = child_process.spawn('python3', ['../robot-moves/move_forward.py']);
    isCurrentPythonProcessClosed = false;
    currentPythonProcess.on('close', (code) => {
        isCurrentPythonProcessClosed = true;
    });
    res.end()
});

app.post('/back', async (req, res) => {
    await killLastPythonProcess();
    console.log('back');
    currentPythonProcess = child_process.spawn('python3', ['../robot-moves/move_back.py']);
    isCurrentPythonProcessClosed = false;
    currentPythonProcess.on('close', (code) => {
        isCurrentPythonProcessClosed = true;
    });
    res.end()
});

app.post('/left', async (req, res) => {
    await killLastPythonProcess();
    console.log('left');
    currentPythonProcess = child_process.spawn('python3', ['../robot-moves/move_left.py']);
    isCurrentPythonProcessClosed = false;
    currentPythonProcess.on('close', (code) => {
        isCurrentPythonProcessClosed = true;
    });
    res.end()
});

app.post('/right', async (req, res) => {
    await killLastPythonProcess();
    console.log('right');
    currentPythonProcess = child_process.spawn('python3', ['../robot-moves/move_right.py']);
    isCurrentPythonProcessClosed = false;
    currentPythonProcess.on('close', (code) => {
        isCurrentPythonProcessClosed = true;
    });
    res.end()
});

app.post('/stop', async (req, res) => {
    await killLastPythonProcess();
    console.log('stop');
    currentPythonProcess = child_process.spawn('python3', ['../robot-moves/move_stop.py']);
    isCurrentPythonProcessClosed = false;
    currentPythonProcess.on('close', (code) => {
        isCurrentPythonProcessClosed = true;
    });
    res.end()
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});