// creating a socket
const socket = new WebSocket('wss://'+ window.location.host + '/chat');

//message is received by a client and added to dialog history
socket.onmessage = function(event)
{
	console.log("I got message");
	jason = JSON.parse(event.data);
	msg_string = jason['message'];
	receiver = jason['receiver'];
	sender = jason['sender'];
	console.log("receiver", receiver);
	//message is added to dialog history
	appendMsg(msg_string, 'to me');
}

socket.onclose = function(event)
{
	console.error('Socket closed unexpectedly');
}

socket.onerror = function(event)
{
	console.error('WebSocket error occurred:', event);
    console.log(event);
}

socket.onopen = function(event)
{
	console.log('Socket is open');
}


function openDialog(username, sender)
{
	
	const opt = `name=${username}, width=500, height=500, top=${window.screenY}, left=${window.screenX}`;
	// saveJson({lala: 'la'}, username);
	win = window.open(username, username, opt);
	document.getElementById("test").innerHTML = 'ws://'+ window.location.host + '/chat';
	if (win)
		win.focus();
	// document.getElementsById("test").innerHTML = cat;
	// console.log(win.name);
}

// function saveJson(data, name)
// {
// 	const jsonString = JSON.stringify(data, null, 2);
// 	const blob = new Blob([jsonString], {type: 'application/json'});
// 	const a = document.createElement('a');
// 	const url = URL.createObjectURL(blob);

// 	a.href = url;
// 	a.download = `data/${name}.json`;
// 	a.click();
// 	URL.revokeObjectURL(url);
// }

// message is saved to msg history
// function sendMsg(username)
// {
// 	//sending the msg through the socket
// 	//for now sending it to the server

// 	//appending the message to the list
// 	msg = document.getElementById("msg").value; //we are taking the message
// 	parent = document.getElementsByClassName("list-group")[0];
// 	console.log(parent);
// 	element = document.createElement('li');
// 	//creating a list item containing the message
// 	text = document.createTextNode(msg);
// 	element.appendChild(text);
// 	element.setAttribute("class", "list-group-item user-item");
// 	parent.appendChild(element); //appending the item with the message to the list
// 	// document.getElementById('send').submit();
// 	// fetch(`/chat/sendMsg?receiver=${username}&msg=${msg}`)
// 		// .then(response => response.json())
// 		// .then(data => console.log(data))
// 		// .catch(error('Error:', error));
// 	// return(response.JSON())
// }

function sendMsg(receiver, sender)
{
	// console.log("sending msg");
	msg = document.getElementById("msg").value; //we are taking the message
	// console.log(msg);

	// message is sent to the server using socket
	socket.send(JSON.stringify({
        'message': msg, 'receiver': receiver, 'sender': sender,
    }));
	console.log("msg is send", sender);

	//message is appended to dialog
	appendMsg(msg, 'from me');
}

function appendMsg(msg, whereto)
{
	//sending the msg through the socket
	//for now sending it to the server

	//appending the message to the list
	parent = document.getElementsByClassName("list-group")[0];
	console.log(parent);
	element = document.createElement('li');
	//creating a list item containing the message
	text = document.createTextNode(whereto + ': ' + msg);
	element.appendChild(text);
	if (whereto == 'from me')
		element.setAttribute("class", "ms-5 list-group-item user-item1");
	else
		element.setAttribute("class", "me-5 list-group-item user-item");
	parent.appendChild(element); //appending the item with the message to the list
}
