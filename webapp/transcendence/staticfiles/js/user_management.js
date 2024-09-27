async function submit_registration_form(event) {
  event.preventDefault(); // Prevent default form submission

  let validation = validate_registration_form();

  if (!validation) {
    return;
  }

  const csrfToken = await getCsrfToken();

  console.log(document.getElementById("username").value);

  let username = sanitizeInput(document.getElementById("username").value);
  let password = sanitizeInput(document.getElementById("password").value);
  let avatar = document.getElementById("Avatar").value;
  let email = sanitizeInput(document.getElementById('email').value);
  let twofa = document.getElementById('twofa').checked;

  console.log('twofa value: ' + twofa);

  // console.log(formData);

  fetch("/registration_check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ username, password, avatar, email, twofa }), // JSON.stringify({ username, password })
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json()
    })
    .then((json) => {
      load_next_step(json);
    })
    .catch((error) => {
      handleError(error);
    });
}

function validate_registration_form() {
  let email = document.getElementById('email').value;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(email)) {
    alert("Please provide a valid Email address");
    return false;
  }

  let username = document.getElementById('username').value;

  if (!username) {
    alert("Please provide a username");
    return false;
  }

  let password = document.getElementById('password').value;

  if (!password) {
    alert("Please provide a password");
    return false;
  }

  return true;
}

function load_next_step(json) {
  console.log("Next step:");
  deleteHeader();
  deleteMain();

  // CREATE HEADER

  headerLoad(json);

  // CREATE CONTAINER

  json.menuItems.forEach((item) => {
    let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
    let element = document.createElement(item.type);
    if (item.type == "div" || item.type == "form")
      divLoader(element, item.content);

    elementCustomize(element, item);
    parent.appendChild(element);
  });
}

async function submit_login_form(event) {
  event.preventDefault(); // Prevent default form submission

  let validation = validate_login_form();

  if (!validation)
    return;

  console.log('submit login form called');

  const csrfToken = await getCsrfToken();
  const username = sanitizeInput(document.getElementById("username").value);
  const password = sanitizeInput(document.getElementById("password").value);

  fetch("/login_check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ username, password }),
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      console.log(json.status);
      if (json.status === 'otp_sent') {
        // Show OTP popup
        document.getElementById("otpPopup").style.display = "block";
      } else {
        chatSocket = new ChatSocket();
        load_main();
      }

    })
    .catch((error) => handleError(error));
}

function validate_login_form() {
  const username = sanitizeInput(document.getElementById("username").value);

  if (!username) {
    alert("Please enter a username");
    return false;
  }

  const password = sanitizeInput(document.getElementById("password").value);

  if (!password) {
    alert("Please enter a password");
    return false;
  }

  return true;
}

async function verify_otp(event) {
  event.preventDefault(); // Prevent default form submission behavior

  const csrfToken = await getCsrfToken();
  const otp = document.getElementById("otp").value;

  fetch("/verify_otp", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ otp }),
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      } else return response.json()
    })
    .then((json) => {
      chatSocket = new ChatSocket();
      load_main()
    })
    .catch((error) => handleError(error));
}

async function logout(event) {
  const csrfToken = await getCsrfToken();

  fetch("/logout", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((data) => {
      console.log("Token Cookies Deleted Successfully.");
      chatSocket.closeWebSocket();
      chatSocket = null;
      load_main();
    })
    .catch((error) => handleError(error));
}

async function getCsrfToken() {
  const response = await fetch("/api/csrf-token/", {
    method: "GET",
    credentials: "include",
  });
  const data = await response.json();
  return data.csrfToken;
}

async function uploadAvatar(event) {
  event.preventDefault();
  const csrfToken = await getCsrfToken();

  const fileInput = document.getElementById('fileUpload');
  const file = fileInput.files[0];

  if (!file) {
    handleError("Please Select a File to Upload");
    return;
  }

  const base64File = await convertToBase64(file);

  let url = '/upload_file';

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      fileName: file.name,
      fileType: file.type,
      fileData: base64File
    }),
    credentials: "include"
  })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function convertToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => {
      resolve(reader.result.split(',')[1]); // Remove the "data:*/*;base64," part
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}
async function settings() {

  const csrfToken = await getCsrfToken();

  let url = '/settings';

  fetch(url, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    credentials: 'include',
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      } else return response.json();
    })
    .then(json => {
      LOAD_DATA(json)
    })
    .catch(error => handleError(error));
}

async function deleteUserStats(event) {
  event.preventDefault();

  const csrfToken = await getCsrfToken();

  let url = '/delete_user_stats';

  fetch(url, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    credentials: 'include'
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      } else return response.json();
    })
    .then(json => {
      deleteHeader();
      deleteMain();

      // CREATE HEADER

      headerLoad(json);

      // CREATE CONTAINER

      json.menuItems.forEach((item) => {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        let element = document.createElement(item.type);
        if (item.type == "div" || item.type == "form" || item.type == "select")
          divLoader(element, item.content);

        elementCustomize(element, item);
        parent.appendChild(element);

        // div.appendChild(element);
      });
    })
    .catch(error => handleError(error));
}

function applyMatchInvitation(event) {

  console.log("applyMatchInvitation");
  const button = event.currentTarget;
  const parent = button.parentElement.parentElement;
  const friendshipID = button.dataset.friendshipid;
  const sender = button.dataset.sender;
  const acceptor = button.dataset.receiver;

  const message = JSON.stringify({
    'type': 'apply_match_invitation',
    'sender': acceptor,
    'receiver': sender,
    'friendship_id': friendshipID,
  });
  chatSocket.socket.send(message);

  parent.remove();
  submit_local_pregame_invite(sender, acceptor);
}



function declineMatchInvitation(event) {

  console.log("declineMatchInvitation");
  const button = event.currentTarget;
  const parent = button.parentElement.parentElement;
  const friendshipID = button.dataset.friendshipid;
  const sender = button.dataset.sender;
  const acceptor = button.dataset.receiver;

  const message = JSON.stringify({
    'type': 'decline_match_invitation',
    'sender': acceptor,
    'receiver': sender,
    'friendship_id': friendshipID,
  });
  chatSocket.socket.send(message);
  parent.remove();
}


async function saveChanges() {
  event.preventDefault();

  const csrfToken = await getCsrfToken();

  let url = '/save_changes';

  let username = sanitizeInput(document.getElementById('username').value);
  let avatar = sanitizeInput(document.getElementById('avatar').value);

  console.log("selected avatar: " + avatar);

  fetch(url, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      'username': username,
      'avatar': avatar
    }),
    credentials: 'include'
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      } else {
        // send changes to the socket
        const message = JSON.stringify({
          type: "settings_save",
          new_username: username,
          new_avatarDirect: avatar,
        })
        chatSocket.socket.send(message);
        return response.json();
      }
    })
    .then(json => {
      deleteHeader();
      deleteMain();

      // CREATE HEADER
      console.log(json);
      headerLoad(json);

      // CREATE CONTAINER

      json.menuItems.forEach((item) => {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        let element = document.createElement(item.type);
        if (item.type == "div" || item.type == "form" || item.type == "select")
          divLoader(element, item.content);

        elementCustomize(element, item);
        parent.appendChild(element);

        // div.appendChild(element);
      });
    })
    .catch(error => handleError(error));
}



// async function submit_local_pregame(event) {
//   event.preventDefault()

//   let validation = validate_local_pregame();

//   if (!validation)
//     return;

//   player1 = sanitizeInput(document.getElementById('player1').value);
//   player2 = sanitizeInput(document.getElementById('player2').value);

//   console.log(player1);

//   const csrfToken = await getCsrfToken();

//   fetch('/local_check', {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrfToken,
//       Accept: "application/json",
//     },
//     body: JSON.stringify({ player1, player2 }),
//     credentials: "include",
//   })
//     .then(async (response) => {
//       if (!response.ok) {
//         const errorData = await response.json();
//         throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
//       }
//       else return response.json();
//     }).then((json) => {
//       console.log(json);
//       console.log(json.player1)
//       load_localGame(json);
//     }).catch((error) => {
//       handleError(error);
//     })
// }

async function inviteToLocalGame(profile_name) {
  const csrfToken = await getCsrfToken();
  const user_of_query = (document.getElementById("user").innerHTML).split(" ").pop();
  let url = "/profile";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      'user_of_profile': profile_name,
      'user_of_query': user_of_query,
    }),
    credentials: 'include'
  }).then(async (response) => {
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }
    else return response.json();
  })
    .then((json) => {
      LOAD_DATA(json, true);
    })
    .catch((error) => handleError(error));
}


async function checkProfile(profile_name) {
  const csrfToken = await getCsrfToken();
  const user_of_query = (document.getElementById("user").innerHTML).split(" ").pop();
  let url = "/profile";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      'user_of_profile': profile_name,
      'user_of_query': user_of_query,
    }),
    credentials: 'include'
  }).then(async (response) => {
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }
    else return response.json();
  })
    .then((json) => {
      LOAD_DATA(json, true);
    })
    .catch((error) => handleError(error));
}

function closeChatWindow(event) {
  console.log("TARGET IS:  ");
  console.log(event);
  const targetElement = event.target.parentElement.parentElement;

  targetElement.remove();
}

async function chat(target_friend) {
  console.log("chat has been called");
  const csrfToken = await getCsrfToken();
  const currentUser = (document.getElementById("user").innerHTML).split(" ").pop();
  let sender = "";
  let receiver = "";
  let friendship_id = 0;
  let messages = [];

  const url = '/open_chat';

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      'target_friend': target_friend,
      'source_friend': currentUser,
    }),
    credentials: 'include'
  }).then(async (response) => {
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }
    else return response.json();
  }).then((json) => {
    console.log(json);
    receiver = json.target_friend;
    sender = json.source_friend;
    friendship_id = json.friendship_id;
    messages = json.messages;
    console.log(friendship_id);

    if (document.getElementById(friendship_id))
      return;
    console.log("502");

    let chatWindows = document.getElementsByClassName('chat-window');
    if (chatWindows.length == 3)
      chatWindows[0].remove();


    // CREATE THE CHATWINDOW
    const parent = document.getElementById("chat-container");

    let chatWindow = document.createElement("div");
    chatWindow.setAttribute("class", "d-flex flex-column justify-content-between h-100 w-25 pe-auto chat-window rounded bg-secondary bg-gradient text-white");
    chatWindow.setAttribute("id", `${friendship_id}`);
    console.log("515");
    chatWindow.dataset.receiver = receiver;
    chatWindow.dataset.sender = sender;
    chatWindow.dataset.friendshipId = friendship_id;
    // create 3 divs to create chatwindow

    // Add identifier to chat window
    let chatNav = document.createElement("div");
    chatNav.setAttribute("class", "bg-chat-nav d-flex justify-content-between align-items-center");

    let navInvite = document.createElement("p");
    navInvite.setAttribute("id", target_friend);
    navInvite.setAttribute("onclick", "checkProfile(this.id)");
    navInvite.setAttribute("onclick", "inviteToLocalGame(this.id)");
    navInvite.innerText = "Invite";
    navInvite.classList.add("text-white");
    navInvite.style.cursor = "pointer";
    navInvite.setAttribute("onclick", "chatSocket.sendInviteMessage(event)");


    let navParagraph = document.createElement("p");
    navParagraph.setAttribute("id", target_friend);
    navParagraph.setAttribute("onclick", "checkProfile(this.id)");
    navParagraph.setAttribute("translate", "no");
    navParagraph.innerText = target_friend;
    navParagraph.classList.add("text-warning");
    navParagraph.style.cursor = "pointer";

    let flexGrowDiv = document.createElement("div");
    flexGrowDiv.setAttribute("class", "flex-grow-1 d-flex justify-content-center");

    flexGrowDiv.appendChild(navParagraph);

    let closeChatWindow = document.createElement("p");
    closeChatWindow.innerText = 'X';
    closeChatWindow.setAttribute("onclick", "closeChatWindow(event)");
    closeChatWindow.classList.add("text-danger");
    closeChatWindow.style.cursor = "pointer";
    chatNav.appendChild(navInvite);
    chatNav.appendChild(flexGrowDiv);
    chatNav.appendChild(closeChatWindow);



    // Add Message store to chat window
    let chatBody = document.createElement("div");
    chatBody.setAttribute("class", "bg-chat-body d-flex flex-column flex-grow-1 overflow-scroll");

    // Add HMI to chat window
    let chatInput = document.createElement("div");
    chatInput.setAttribute("class", "bg-warning d-flex flex-row");

    let inputField = document.createElement("input");
    inputField.setAttribute("type", "text");
    inputField.setAttribute("class", "w-75 bg-secondary bg-gradient text-white");
    chatInput.appendChild(inputField);
    let inputButton = document.createElement("button");
    inputButton.innerHTML = "Send";
    inputButton.setAttribute("class", "w-25 bg-secondary text-white");
    inputButton.setAttribute("onclick", "chatSocket.sendMessage(event)");
    chatInput.appendChild(inputButton);
    console.log("545");


    chatWindow.appendChild(chatNav);
    chatWindow.appendChild(chatBody);
    chatWindow.appendChild(chatInput);
    parent.appendChild(chatWindow);

    messages.forEach((message) => {
      if (message.message == "")
        return;
      let messageDiv = document.createElement("div");
      console.log(`receiver: ${receiver} - currentUser: ${currentUser}`);
      if (message.receiver == currentUser)
        messageDiv.setAttribute("class", "align-self-start w-25 p-1 m-1 bg-chat-message border-primary rounded");
      else
        messageDiv.setAttribute("class", "align-self-end w-25 p-1 m-1 bg-chat-message border-primary rounded");
      let messageParagraph = document.createElement("p");
      messageParagraph.setAttribute("class", "text-white");
      messageParagraph.setAttribute("translate", "no");
      messageParagraph.innerHTML = message.message;
      messageDiv.appendChild(messageParagraph);
      chatBody.appendChild(messageDiv);
    })
  })
    .catch((error) => {
      console.error(error);
      handleError(error)
    });

}

async function block(event) {
  const targetElement = event.target;
  const blocker = (document.getElementById("user").innerHTML).split(" ").pop();
  const blocked = event.target.id;

  console.log("BLOCK CALLED");
  console.log(blocked);
  console.log("BLOCK DONE");

  const csrfToken = await getCsrfToken();

  fetch("/block_user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ blocker, blocked }),
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      targetElement.setAttribute('onclick', 'unblock(event)');
      targetElement.innerText = "UNBLOCK";
    })
    .catch((error) => handleError(error));
}

async function unblock(event) {
  const targetElement = event.target;
  const unblocker = (document.getElementById("user").innerHTML).split(" ").pop();
  const unblocked = event.target.id;

  console.log("BLOCK CALLED");
  console.log(unblocked);
  console.log("BLOCK DONE");

  const csrfToken = await getCsrfToken();

  fetch("/unblock_user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ unblocker, unblocked }),
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      targetElement.setAttribute('onclick', 'block(event)');
      targetElement.innerText = "BLOCK";
    })
    .catch((error) => handleError(error));
}