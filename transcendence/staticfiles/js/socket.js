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
        case 'friend_duplication_notification':
            handleFriendDuplicateNotification(data);
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
    console.log(data.friendship_id);
    let chatWindow = document.getElementById(data.friendship_id);
    let chatBox = chatWindow.children[1];
    let thisUser = (document.getElementById("user").innerHTML).split(" ").pop();
    let messageDiv = document.createElement("div");

    if (thisUser == data.receiver) {
        messageDiv.setAttribute("class", "align-self-start w-25 p-1 mt-1 bg-warning border-primary rounded");
    } else {
        messageDiv.setAttribute("class", "align-self-end w-25 p-1 mt-1 bg-warning border-primary rounded");
    }

    let messageParagraph = document.createElement("p");
    messageParagraph.innerHTML = data.message;
    messageDiv.appendChild(messageParagraph);
    chatBox.appendChild(messageDiv);
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
    accept.innerHTML = 'ACCEPT';
    buttonDiv.appendChild(accept);

    let decline = document.createElement('button');
    decline.setAttribute('onclick', 'decline_friend_request(this.id)');
    decline.setAttribute('id', `${friend}`);
    decline.innerHTML = 'DECLINE';
    buttonDiv.appendChild(decline);

    console.log(newNode);

    return newNode;
}

function new_friend(friend) {
    let newNode;

    newNode = document.createElement('div');
    newNode.setAttribute('class', 'd-flex flex-column');
    // appendChild

    let p = document.createElement('p');
    p.setAttribute('class', 'text-white');
    p.innerHTML = `${friend}`;
    newNode.appendChild(p);

    let buttonDiv = document.createElement('div');
    buttonDiv.setAttribute('class', 'd-flex flex-column');
    newNode.appendChild(buttonDiv);

    let accept = document.createElement('button');
    accept.setAttribute('onclick', `chat(this.id)`);
    accept.setAttribute('id', `${friend}`);
    accept.innerHTML = 'CHAT';
    buttonDiv.appendChild(accept);

    let decline = document.createElement('button');
    decline.setAttribute('onclick', 'checkProfile(this.id)');
    decline.setAttribute('id', `${friend}`);
    decline.innerHTML = 'PROFILE';
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
    
    try {
        // if fails then its the sender
        console.log('Looking for element with ID:', data.accepted);
        const elementToRemove = (document.getElementById(data.accepted).parentElement).parentElement;
        elementToRemove.remove();
        console.log('receiver');
        const parent = document.getElementById('friends');
        const newNode = new_friend(data.accepted);
        parent.appendChild(newNode);
    } catch (error) {
        console.log(error);
        console.log('sender');
        const parent = document.getElementById('friends');
        const newNode = new_friend(data.acceptor);
        parent.appendChild(newNode);

    }
    // alert(data.message);
}

function handleFriendDeclinationNotification(data) {
    console.log('New notification:', data.message);
    alert(data.message);
}

function handleFriendDuplicateNotification(data) {
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


    // Move to after ack function
    // const elementToRemove = document.getElementById(accepted_user).parentElement.parentElement;
    // elementToRemove.remove();

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

    // Move to after ack function
    // const elementToRemove = document.getElementById(declined_user).parentElement.parentElement;
    // elementToRemove.remove();

    const message = JSON.stringify({
        decliner: decliner_user,
        declined: declined_user,
        type: 'friend_declination',
    })

    socket.send(message);
}

function send_message(event) {
    // Get the button element that triggered the function
    const buttonElement = event.target;

    // Get the chat window element by navigating from the button
    const chatWindow = buttonElement.closest('.chat-window'); // Assuming the chat window has a class like 'chat-window'
    
    // Access the necessary data from the chat window's dataset
    const receiver = chatWindow.dataset.receiver;
    const sender = chatWindow.dataset.sender;
    const friendship_id = chatWindow.dataset.friendshipId;

    // Get the message from the input field in the chat window
    const inputField = chatWindow.querySelector('input[type="text"]');
    const message = inputField.value;

    if (message.trim() === "") {
        console.log("Message cannot be empty!");
        return;
    }

    // Construct the message data to send
    const messageData = JSON.stringify({
        type: "chat_message",
        sender: sender,
        receiver: receiver,
        friendship_id: friendship_id,
        message: message
    });

    // Clear the input field after sending
    inputField.value = "";

    // Here you would send the message data to the server, for example using fetch or WebSocket
    // For demonstration, let's log it to the console
    console.log("Sending message:", messageData);

    // Example: Sending the message via fetch
    socket.send(messageData);
}