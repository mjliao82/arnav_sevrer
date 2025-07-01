const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');

// === Setup Express ===
const app = express();
const port = 3000;
app.use(express.static(path.join(__dirname, '../frontend')));
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// === Connect to Python WebSocket Server ===
const pythonSocket = new WebSocket('ws://localhost:3000');

pythonSocket.on('open', () => {
  console.log("Connected to Python WebSocket server");
});

pythonSocket.on('error', (err) => {
  console.error("Failed to connect to Python WebSocket server:", err.message);
});

// === Handle incoming frontend connections ===
wss.on('connection', (ws) => {
  console.log('New frontend client connected');

  ws.send(JSON.stringify({
    type: 'server_hello',
    content: 'Welcome to the WebSocket server!'
  }));

  ws.on('message', (message) => {
    console.log('Received from frontend:', message);
    try {
      const data = JSON.parse(message);

      // Handle chat
      if (data.type === 'chat') {
        const response = {
          type: 'acknowledgement',
          id: data.id,
          content: `Server received: ${data.content}`
        };
        ws.send(JSON.stringify(response));
      }

      // Forward login to Python
      else if (data.type === 'login') {
        console.log("Login:", data.content);

        const toPython = {
          type: 'login',
          id: data.id,
          content: data.content
        };

        if (pythonSocket.readyState === WebSocket.OPEN) {
          pythonSocket.send(JSON.stringify(toPython));
        }
      }

      // Forward keypress to Python
      else if (data.type === 'keypressed') {
        console.log("Keypress:", data.key);

        const toPython = {
          type: 'keypressed',
          id: data.id,
          key: data.key,
          name: data.name
        };

        if (pythonSocket.readyState === WebSocket.OPEN) {
          pythonSocket.send(JSON.stringify(toPython));
        }
      }

    } catch (e) {
      console.error('Invalid JSON:', e);
      ws.send(JSON.stringify({ type: 'error', content: 'Invalid JSON format' }));
    }
  });

  ws.on('close', () => {
    console.log('Frontend client disconnected');
  });
});

server.listen(port, () => {
  console.log(`WebSocket server listening at http://localhost:${port}`);
});
