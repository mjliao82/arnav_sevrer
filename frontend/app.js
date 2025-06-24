const ws = new WebSocket(`ws://${window.location.host}`);


ws.onopen = () => {
  console.log('Connected to WebSocket server');
};

ws.onmessage = (event) => {
  const msgDiv = document.getElementById('messages');
  const data = JSON.parse(event.data);
  msgDiv.innerHTML += `<p><strong>${data.type}</strong>: ${data.content}</p>`;
};

function sendMessage() {
  const input = document.getElementById('msgInput');
  const message = {
    type: 'chat',
    id: Date.now(),
    content: input.value,
  };
  ws.send(JSON.stringify(message));
  input.value = '';
}

function sendName() {
  const name = document.getElementById('nameInput');
  const send_button = document.getElementById('send_button')
  const game_tag = {
    type: 'login',
    id: Date.now(),
    content: name.value

  };    
  ws.send(JSON.stringify(game_tag));
  hide(name);
  hide(send_button);
  document.addEventListener('keydown', function(event) {
    // Access the key that was pressed
    //const key = event.key;
    const keyCode = event.code;
  
    // Check for specific keys
    // if (key === 'Enter') {
    //   console.log('Enter key pressed!');
    // }
    if (keyCode === 'ArrowUp') {
      const input = {
        type: 'keypressed',
        id: Date.now(),
        key: keyCode,
        name: name.value
      };
      ws.send(JSON.stringify(input))
    }
    if (keyCode === 'ArrowDown') {
      const input = {
        type: 'keypressed',
        id: Date.now(),
        key: keyCode,
        name: name.value
      };
      ws.send(JSON.stringify(input))
    }
    if (keyCode === 'ArrowLeft') {
      const input = {
        type: 'keypressed',
        id: Date.now(),
        key: keyCode,
        name: name.value
      };
      ws.send(JSON.stringify(input))
    }
    if (keyCode === 'ArrowRight') {
      const input = {
        type: 'keypressed',
        id: Date.now(),
        key: keyCode,
        name: name.value
      };
      ws.send(JSON.stringify(input))
    }
    if (keyCode === 'Space') {
      const input = {
        type: 'keypressed',
        id: Date.now(),
        key: keyCode,
        name: name.value
      };
      ws.send(JSON.stringify(input))
    }
  });
}


function hide(object) {
  object.style.display = 'none'
}

function sendAll() {
  const name  = document.getElementById('nameInput');
  const passwordInput = document.getElementById('passwordInput')
  const buttonInput = document.getElementById('controlInput')
  const login_info = {
    type: 'all_login_info',
    id: Date.now(),
    content: [name.value, passwordInput.value, buttonInput.value]
  }
  ws.send(JSON.stringify(login_info));
  name.value = '';
  passwordInput.value = '';
  buttonInput.value = '';
}

