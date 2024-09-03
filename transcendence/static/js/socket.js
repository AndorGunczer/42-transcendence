console.log('wss://' + window.location.host + '/ws/communication/');

const socket = new WebSocket('wss://' + window.location.host + '/ws/communication/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    switch (data.type) {
        case 'chat_message':
            handleChatMessage(data);
            break;
        case 'friend_request':
            console.log("friend request received");
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

function handleChatMessage(data) {
    console.log('New chat message:', data);
}

function new_friend_request(friend) {
    let newNode;

    newNode = document.createElement('div');
    newNode.setAttribute('class', 'd-flex flex-column');
    // appendChild

    let p = (document.createElement('p')).innerHTML(`new friend request from ${friend}`);
    newNode.appendChild(p);

    let buttonDiv = (document.createElement('div')).setAttribute('class', 'd-flex flex-column');
    newNode.appendChild(buttonDiv);

    let accept = (document.createElement('button')).setAttribute('onclick', 'accept_friend_request()');
    accept.innerHTML('Accept');
    buttonDiv.appendChild(accept);

    let decline = (document.createElement('button')).setAttribute('onclick', 'decline_friend_request()');
    decline.innerHTML('Decline');
    buttonDiv.appendChild(decline);

    return newNode;
}

function handleFriendRequest(data) {
    console.log('New friend request:', data);

    const friend_request_list = document.getElementById('friend-requests');
    let newNode = new_friend_request(data.sender);

    friend_request_list.appendChild(newNode);

}

function handleNotification(data) {
    console.log('New notification:', data.message);
    alert(data.message);
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