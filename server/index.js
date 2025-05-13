const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the frontend directory
app.use(express.static(path.join(__dirname, '../frontend')));

const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

wss.on('connection', (ws) => {
  console.log('New client connected');

  ws.on('message', (message) => {
    console.log('received:', message);
    try {
      const data = JSON.parse(message);
      if (data.type === 'chat') {
        const response = {
          type: 'acknowledgement',
          id: data.id,
          content: `Server received: ${data.content}`
        };
        ws.send(JSON.stringify(response));
      }
      else if (data.type == 'all_login_info') {
        console.log("Recieved Info")
        const check = {
          type: 'acknowledgement',
          id: data.id,
          content: data.content,
        };
        wss.clients.forEach((client) => {
          if (client.readyState === WebSocket.OPEN) {
              client.send(JSON.stringify(check));
          }
        });
        console.log(`New user:`, data.content)
      }
    } catch (e) {
      console.error('Error parsing message:', e);
      ws.send(JSON.stringify({ type: 'error', content: 'Invalid JSON format' }));
    }
  });

  ws.on('close', () => {
    console.log('Client disconnected');
  });
});

server.listen(port, () => {
  console.log(`Server is listening on http://localhost:${port}`);
});