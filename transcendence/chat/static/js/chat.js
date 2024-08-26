// const bootstrap = require('bootstrap');

// document.getElementById("user-item").onclick = openDialog("yoyo");

function openDialog(username)
{
	
	const opt = `name=${username}, width=500, height=500, top=${window.screenY}, left=${window.screenX}`;
	// saveJson({lala: 'la'}, username);
	win = window.open(username, username, opt);
	// document.getElementById("test").innerHTML = opt;
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
function sendMsg(username)
{
	msg = document.getElementById("msg").value;
	parent = document.getElementsByClassName("list-group")[0];
	console.log(parent);
	element = document.createElement('li');
	text = document.createTextNode(msg);
	element.appendChild(text);
	element.setAttribute("class", "list-group-item user-item");
	// element.setAttribute("class", "user-item");
	parent.appendChild(element);
	// document.getElementById('send').submit();
	// fetch(`/chat/sendMsg?receiver=${username}&msg=${msg}`)
		// .then(response => response.json())
		// .then(data => console.log(data))
		// .catch(error('Error:', error));
	// return(response.JSON())
}
