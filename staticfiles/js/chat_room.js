'use strict'


// logic for auto scroll to bottom 
let chatLog=document.querySelector('.chat-log');
chatLog.scrollTop = chatLog.scrollHeight;
// logic end

const roomName = JSON.parse(document.getElementById('room-name').textContent);
const sender = JSON.parse(document.getElementById('sender').textContent);
const receiver = JSON.parse(document.getElementById('receiver').textContent);
const user = JSON.parse(document.getElementById('user').textContent);


const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if(data.sender==user)
    {
        document.querySelector('#chat-log').innerHTML+=`<div class="sent"><div class="chat sent-chat">${data.message}</div></div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    }
    else{
        document.querySelector('#chat-log').innerHTML+=`<div class="recieved "><div class="chat recieved-chat">${data.message}</div></div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    }
    document.querySelector('#chat-message-input').focus();
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly and error is:',e);
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').addEventListener('click',function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    if(message!=''){
        chatSocket.send(JSON.stringify({
            'sender':sender,
            'receiver':receiver,
            'message': message,
            'roomname':roomName,
        }));
        messageInputDom.value = '';
    }
});

