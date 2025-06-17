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
    content: input.value
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
  hide(send_button)
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

window.addEventListener("keydown", function (event) {
  if (event.keyCode === 37) {
    const left_key = {
      type: 'control',
      id: Date.now(),
      content: "Left Arrow Key",


    }
    ws.send(JSON.stringify(left_key));
  }
});