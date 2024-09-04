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
        case 'friend_acceptance_notification':
            handleFriendAcceptanceNotification(data);
            break;
        case 'friend_declination_notification':
            handleFriendDeclinationNotification(data);
            break;
        default:
            console.error('Unknown message type:', data.type);
    }
};


socket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
};



// Handle Incoming 

function handleChatMessage(data) {
    console.log('New chat message:', data);
}

function new_friend_request(friend) {
    let newNode;

    newNode = document.createElement('div');
    newNode.setAttribute('class', 'd-flex flex-column');
    // appendChild

    let p = document.createElement('p');
    p.setAttribute('class', 'text-white');
    p.innerHTML = `new friend request from ${friend}`;
    newNode.appendChild(p);

    let buttonDiv = document.createElement('div');
    buttonDiv.setAttribute('class', 'd-flex flex-column');
    newNode.appendChild(buttonDiv);

    let accept = document.createElement('button');
    accept.setAttribute('onclick', `accept_friend_request(this.id)`);
    accept.setAttribute('id', `${friend}`);
    accept.innerHTML = 'Accept';
    buttonDiv.appendChild(accept);

    let decline = document.createElement('button');
    decline.setAttribute('onclick', 'decline_friend_request(this.id)');
    decline.setAttribute('id', `${friend}`);
    decline.innerHTML = 'Decline';
    buttonDiv.appendChild(decline);

    console.log(newNode);

    return newNode;
}

function handleFriendRequest(data) {
    console.log('New friend request:', data);

    const friend_request_list = document.getElementById('friend-requests');
    console.log(data.sender);
    let newNode = new_friend_request(data.sender);

    friend_request_list.appendChild(newNode);

}

function handleNotification(data) {
    console.log('New notification:', data.message);
    alert(data.message);
}

function handleFriendAcceptanceNotification(data) {
    console.log('New notification:', data.message);
    alert(data.message);
}

function handleFriendDeclinationNotification(data) {
    console.log('New notification:', data.message);
    alert(data.message);
}


// Handle Outgoing
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

function accept_friend_request(accepted_user) {
    console.log(accepted_user);

    const acceptor_user = (document.getElementById("user").innerHTML).split(" ").pop();
    accepted_user = accepted_user;

    const message = JSON.stringify({
        acceptor: acceptor_user,
        accepted: accepted_user,
        type: 'friend_acceptance',
    })

    socket.send(message);
}

function decline_friend_request(declined_user) {
    console.log(declined_user);

    const decliner_user = (document.getElementById("user").innerHTML).split(" ").pop();
    declined_user = declined_user;

    const message = JSON.stringify({
        decliner: decliner_user,
        declined: declined_user,
        type: 'friend_declination',
    })

    socket.send(message);
}