console.log('wss://' + window.location.host + '/ws/communication/');

const socket = new WebSocket('wss://' + window.location.host + '/ws/communication/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    switch (data.type) {
        case 'chat_message':
            handleChatMessage(data);
            break;
        case 'friend_request':
            handleFriendRequest(data);
            break;
        case 'notification':
            handleNotification(data);
            break;
        default:
            console.error('Unknown message type:', data.type);
    }
};


socket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
};

function handleChatMessage(message) {
    console.log('New chat message:', message);
}

function handleFriendRequest(message) {
    console.log('New friend request:', message);
}

function handleNotification(message) {
    console.log('New notification:', message);
    alert(message.message);
}

// Onclick Functions

function send_friend_request(event) {
    event.preventDefault();
    console.log("SEND FRIEND REQUEST CLIENT SIDE CALL");

    const receiver = document.getElementById("friend-name").value;
    const sender = (document.getElementById("user").innerHTML).split(" ").pop();

    const message = JSON.stringify({
        receiver: receiver,
        sender: sender,
        type: "friend_request",
    });

    socket.send(message);
}