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

  // Optional: send a welcome message to the client
  ws.send(JSON.stringify({
    type: 'server_hello',
    content: 'Welcome to the WebSocket server!'
  }));

  ws.on('message', (message) => {
    console.log('Received:', message);
    try {
      const data = JSON.parse(message);

      // Handle chat messages
      if (data.type === 'chat') {
        const response = {
          type: 'acknowledgement',
          id: data.id,
          content: `Server received: ${data.content}`
        };
        ws.send(JSON.stringify(response));
      }

      // Handle login broadcast
      else if (data.type === 'all_login_info') {
        console.log("Received login info:", data.content);

        const broadcastMessage = {
          type: 'acknowledgement',
          id: data.id,
          content: `Login: ${data.content[0]}, Password: ${data.content[1]}`
        };

        let count = 0;
        wss.clients.forEach((client) => {
          if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(broadcastMessage));
            count++;
          }
        });
        console.log(`Broadcast sent to ${count} client(s).`);
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
