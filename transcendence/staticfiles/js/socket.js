console.log('wss://' + window.location.host + '/wss/communication/');

const socket = new WebSocket('wss://' + window.location.host + '/wss/communication/');

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
}

// Onclick Functions

async function send_friend_request(event) {
    event.preventDefault()

    const csrfToken = await getCsrfToken();

    const friendName = document.getElementById("friend-name").value;
    const url = "/wss/communication/"

    fetch(url, {
        method: "POST",
        headers: {
            "content-type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            receiver: friendName,
            type: "friend_request",
        }),
        credentials: "include",
    }).then((response) => {
        if (response.ok)
            alert("Friend Request Sent");
    })
}