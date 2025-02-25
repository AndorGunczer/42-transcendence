

let chatSocket = null;

class InvitePlayer {
    invitedID = 0;
    challangerID = 0;
    invitedName = "";
    challangerName = "";

    constructor(invitedID, challangerID, invitedName, challangerName) {
        this.invitedID = invitedID;
        this.challangerID = challangerID;
        this.invitedName = invitedName;
        this.challangerName = challangerName;
    }
};

class ChatSocket {
    constructor() {
        this.socket = new WebSocket('wss://' + window.location.host + '/ws/communication/');
        this.initializeSocket();
    }

    initializeSocket() {
        this.socket.onmessage = this.handleMessage.bind(this);
        this.socket.onclose = this.handleClose.bind(this);
    }

    handleMessage(event) {
        const data = JSON.parse(event.data);
        console.log(data.type);
        switch (data.type) {
            case 'apply_match_invitation':
                handleMatchInvitationApply(data);
                break;
            case 'decline_match_invitation':
                handleMatchInvitationDecline(data);
                break;
            case 'chat_invite':
                inviteNotification(data);
                break;
            case 'chat_message':
                this.handleChatMessage(data);
                break;
            case 'set_user_to_online':
                this.handleSetUserOnlineStatus(data, "Online");
                break;
            case 'set_user_to_offline':
                this.handleSetUserOnlineStatus(data, "Offline");
                break;
            case 'friend_request':
                this.handleFriendRequest(data);
                break;
            case 'notification':
                this.handleNotification(data);
                break;
            case 'friend_acceptance_notification':
                this.handleFriendAcceptanceNotification(data);
                break;
            case 'friend_declination_notification':
                this.handleFriendDeclinationNotification(data);
                break;
            case 'friend_duplication_notification':
                this.handleFriendDuplicateNotification(data);
                break;
            case 'tournament_broadcast':
                greenNotification(data.message);
                break;
            default:
                console.error('Unknown message type:', data.type);
        }
    }


    handleClose(e) {
        console.error('WebSocket closed unexpectedly');
    }

    closeWebSocket() {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            this.socket.close();
            console.log('WebSocket connection closed');
        }
    }


    handleChatMessage(data) {
        let chatWindow = document.getElementById(data.friendship_id);

        if (!chatWindow)
            return;

        let chatBox = chatWindow.children[1];
        let thisUser = (document.getElementById("user").innerHTML).split(" ").pop();
        let messageDiv = document.createElement("div");

        if (thisUser == data.receiver) {
            messageDiv.setAttribute("class", "align-self-start w-25 p-1 mt-1 bg-chat-message border-primary rounded");
        } else {
            messageDiv.setAttribute("class", "align-self-end w-25 p-1 mt-1 bg-chat-message border-primary rounded");
        }

        let messageParagraph = document.createElement("p");
        messageParagraph.setAttribute("class", "text-white");
        messageParagraph.innerHTML = data.message;
        messageDiv.appendChild(messageParagraph);
        chatBox.appendChild(messageDiv);
    }

    handleSetUserOnlineStatus(data, onlineStatus) {
        const currentUser = (document.getElementById("user").innerHTML).split(" ").pop();
        const targetUser = data.target_user_name

        if (currentUser != targetUser) {
            // Find the button element
            const button = document.getElementById(targetUser);

            // Use closest to find the nearest ancestor div with class d-flex (container)
            const container = button.parentElement.parentElement;

            // Use querySelector to find the element with class .is_online within the container
            const isOnline = container.querySelector('.is_online');

            // Check if the element exists and log the content or do something with it
            if (isOnline) {
                console.log(isOnline.textContent); // Logs "Online"
            } else {
                console.log('No .is_online element found');
            }

            isOnline.innerText = onlineStatus;
        }
    }

    // handleSetUserOffline(data) {
    //     const currentUser = (document.getElementById("user").innerHTML).split(" ").pop();
    //     const targetUser = data.target_user_name

    //     if (currentUser != targetUser) {
    //         // Find the button element
    //         const button = document.getElementById(targetUser);

    //         // Use closest to find the nearest ancestor div with class d-flex (container)
    //         const container = button.parentElement.parentElement;

    //         // Use querySelector to find the element with class .is_online within the container
    //         const isOnline = container.querySelector('.is_online');

    //         // Check if the element exists and log the content or do something with it
    //         if (isOnline) {
    //             console.log(isOnline.textContent); // Logs "Online"
    //         } else {
    //             console.log('No .is_online element found');
    //         }

    //         isOnline.innerText = "Offline";
    //     }
    // }

    handleFriendRequest(data) {
        // if (data.)
        console.log('New friend request:', data);
        const friendRequestList = document.getElementById('friend-requests');
        let newNode = this.newFriendRequest(data.sender);
        friendRequestList.appendChild(newNode);
    }

    handleNotification(data) {
        console.log('New notification:', data.message);
        alert(data.message);
    }

    handleFriendAcceptanceNotification(data) {
        console.log('New notification:', data.message);

        try {
            // if fails then its the sender
            console.log('Looking for element with ID:', data.accepted);
            const elementToRemove = (document.getElementById(data.accepted).parentElement).parentElement;
            if (elementToRemove)
                elementToRemove.remove();
            console.log('Receiver');
            const parent = document.getElementById('friends').parentElement;
            const newNode = this.newFriend(data.accepted);
            parent.appendChild(newNode);
        } catch (error) {
            console.log(error);
            console.log('Sender');
            const parent = document.getElementById('friends').parentElement;
            const newNode = this.newFriend(data.acceptor);
            parent.appendChild(newNode);
        }
    }

    handleFriendDeclinationNotification(data) {
        try {
            // if fails then its the sender
            console.log('Looking for element with ID:', data.declined);
            const elementToRemove = (document.getElementById(data.declined).parentElement).parentElement;
            if (elementToRemove)
                elementToRemove.remove();
        } catch (error) {
            console.log(error);
        }
        console.log('New notification:', data.message);
        alert(data.message);
    }

    handleFriendDuplicateNotification(data) {
        console.log('New notification:', data.message);
        alert(data.message);
    }

    newFriendRequest(friend) {
        let newNode = document.createElement('div');
        newNode.setAttribute('class', 'd-flex flex-column');

        let p = document.createElement('p');
        p.setAttribute('class', 'text-white');
        p.innerHTML = `New friend request from ${friend}`;
        newNode.appendChild(p);

        let buttonDiv = document.createElement('div');
        buttonDiv.setAttribute('class', 'd-flex flex-column');
        newNode.appendChild(buttonDiv);

        let accept = document.createElement('button');
        accept.setAttribute('onclick', `chatSocket.acceptFriendRequest(this.id)`);
        accept.setAttribute('id', `${friend}`);
        accept.innerHTML = 'ACCEPT';
        buttonDiv.appendChild(accept);

        let decline = document.createElement('button');
        decline.setAttribute('onclick', 'chatSocket.declineFriendRequest(this.id)');
        decline.setAttribute('id', `${friend}`);
        decline.innerHTML = 'DECLINE';
        buttonDiv.appendChild(decline);

        console.log(newNode);

        return newNode;
    }

    newFriend(friend) {
        let newNode = document.createElement('div');
        newNode.setAttribute('class', 'd-flex flex-column');

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

    sendFriendRequest(event) {
        event.preventDefault();
        console.log("SEND FRIEND REQUEST CLIENT SIDE CALL");

        const receiver = sanitizeInput(document.getElementById("friend-name").value);
        const sender = (document.getElementById("user").innerHTML).split(" ").pop();

        const message = JSON.stringify({
            receiver: receiver,
            sender: sender,
            type: "friend_request",
        });

        this.socket.send(message);
    }

    acceptFriendRequest(accepted_user) {
        console.log(accepted_user);

        const acceptor_user = (document.getElementById("user").innerHTML).split(" ").pop();

        const message = JSON.stringify({
            acceptor: acceptor_user,
            accepted: accepted_user,
            type: 'friend_acceptance',
        });

        this.socket.send(message);
    }

    declineFriendRequest(declined_user) {
        console.log(declined_user);

        const decliner_user = (document.getElementById("user").innerHTML).split(" ").pop();

        const message = JSON.stringify({
            decliner: decliner_user,
            declined: declined_user,
            type: 'friend_declination',
        });

        this.socket.send(message);
    }

    sendMessage(event) {
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
        const message = sanitizeInput(inputField.value);

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

        // Send the message via WebSocket
        this.socket.send(messageData);
    }

    sendInviteMessage(event) {
        // Get the button element that triggered the function
        const buttonElement = event.target;

        // Get the chat window element by navigating from the button
        const chatWindow = buttonElement.closest('.chat-window'); // Assuming the chat window has a class like 'chat-window'

        // Access the necessary data from the chat window's dataset
        const receiver = chatWindow.dataset.receiver;
        const sender = chatWindow.dataset.sender;
        const friendship_id = chatWindow.dataset.friendshipId;
        {
            const message = "A challenge has been opened. Check your notifications!";
            const messageData = JSON.stringify({
                type: "chat_message",
                sender: sender,
                receiver: receiver,
                friendship_id: friendship_id,
                message: message
            });

            this.socket.send(messageData);
        }

        {
            // let _invitePlayer = new InvitePlayer(receiver, sender, "Steven", "Andor");

            const messageData = JSON.stringify({
                type: "chat_invite",
                sender: sender,
                receiver: receiver,
                friendship_id: friendship_id,
                message: ""
            });
            this.socket.send(messageData);
        }
    }
}

// const chatSocket = new ChatSocket();

