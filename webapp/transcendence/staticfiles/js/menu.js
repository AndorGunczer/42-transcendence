// JAVASCRIPT CODE FOR MAIN MENU

// HELPER FUNCTIONS

let gameId;

function sanitizeInput(input) {
  return input.replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function changeSelectFunction(callback, dependencies) {
  // This is a placeholder function. Adjust as necessary for your actual use case.
  // It should return a function that handles events as per the requirements.
  return function (event) {
    callback(event);
  };
}

function closeError(event) {
  const targetElement = event.target;
  const containerElement = targetElement.closest("#error-notification-container");
  containerElement.remove();
}

function handleError(errorMsg) {
  let parent = document.getElementById("error-layer");
  const errorPopup = document.createElement("div");
  errorPopup.setAttribute("class", "d-flex flex-row bg-danger m-2 p-2 rounded-pill pe-auto");
  errorPopup.setAttribute("id", "error-notification-container");

  // First section of error window
  const messageDisplayWindow = document.createElement("div");
  messageDisplayWindow.setAttribute("class", "flex-grow-1 align-self-center");
  const messageDisplay = document.createElement("p");
  messageDisplay.setAttribute("class", "text-white m-0");
  messageDisplay.innerHTML = errorMsg;
  messageDisplayWindow.appendChild(messageDisplay);
  errorPopup.appendChild(messageDisplayWindow);

  // Second section of error window
  const closePopupDiv = document.createElement("div");
  const closePopupButton = document.createElement("button");
  closePopupButton.innerHTML = "X";
  closePopupButton.setAttribute("class", "text-white bg-danger border-0");
  closePopupButton.setAttribute("onclick", "closeError(event)");
  closePopupDiv.appendChild(closePopupButton);
  errorPopup.append(closePopupDiv);

  // Add element to DOM
  parent.appendChild(errorPopup);
}


function handleMatchInvitationApply(inviteData) {
  console.log("handleMatchInvitationApply");
  let parent = document.getElementById("error-layer");
  const errorPopup = document.createElement("div");
  errorPopup.setAttribute("class", "d-flex flex-row bg-info m-2 p-2 rounded-pill pe-auto");
  errorPopup.setAttribute("id", "error-notification-container");

  const messageDisplayWindow = document.createElement("div");
  messageDisplayWindow.setAttribute("class", "flex-grow-1 align-self-center");
  const messageDisplay = document.createElement("span");
  messageDisplay.setAttribute("class", "text-success m-0");
  messageDisplay.innerHTML = innerText = inviteData.sender + " applied for a match. Come to him!";
  messageDisplayWindow.appendChild(messageDisplay);
  errorPopup.appendChild(messageDisplayWindow);

  // Close section of error window
  const closePopupDiv = document.createElement("div");
  const closePopupButton = document.createElement("button");
  closePopupButton.innerHTML = "X";
  closePopupButton.setAttribute("class", "text-white bg-info border-0");
  closePopupButton.setAttribute("onclick", "closeError(event)");
  closePopupDiv.appendChild(closePopupButton);

  errorPopup.append(closePopupDiv);
  parent.appendChild(errorPopup);
}

function handleMatchInvitationDecline(inviteData) {
  console.log("handleMatchInvitationDecline");
  let parent = document.getElementById("error-layer");
  const errorPopup = document.createElement("div");
  errorPopup.setAttribute("class", "d-flex flex-row bg-info m-2 p-2 rounded-pill pe-auto");
  errorPopup.setAttribute("id", "error-notification-container");

  const messageDisplayWindow = document.createElement("div");
  messageDisplayWindow.setAttribute("class", "flex-grow-1 align-self-center");
  const messageDisplay = document.createElement("span");
  messageDisplay.setAttribute("class", "text-danger m-0");
  messageDisplay.innerHTML = innerText = inviteData.sender + " declined your match request :(";
  messageDisplayWindow.appendChild(messageDisplay);
  errorPopup.appendChild(messageDisplayWindow);

  // Close section of error window
  const closePopupDiv = document.createElement("div");
  const closePopupButton = document.createElement("button");
  closePopupButton.innerHTML = "X";
  closePopupButton.setAttribute("class", "text-white bg-info border-0");
  closePopupButton.setAttribute("onclick", "closeError(event)");
  closePopupDiv.appendChild(closePopupButton);

  errorPopup.append(closePopupDiv);
  parent.appendChild(errorPopup);
}


function inviteNotification(inviteData) {
  let parent = document.getElementById("error-layer");
  const errorPopup = document.createElement("div");
  errorPopup.setAttribute("class", "d-flex flex-row bg-info m-2 p-2 rounded-pill pe-auto");
  errorPopup.setAttribute("id", "error-notification-container");
  // (document.getElementById("user").innerHTML).split(" ").pop();
  if (inviteData.receiver === (document.getElementById("user").innerHTML).split(" ").pop()) {
    // First section of error window
    const messageDisplayWindow = document.createElement("div");
    messageDisplayWindow.setAttribute("class", "flex-grow-1 align-self-center");
    const messageDisplay = document.createElement("span");
    messageDisplay.setAttribute("class", "text-white m-0");
    messageDisplay.innerHTML = innerText = "You have been challenged to a game by " + inviteData.sender;
    messageDisplayWindow.appendChild(messageDisplay);
    errorPopup.appendChild(messageDisplayWindow);

    // Apply section of error window
    const applyPopupDiv = document.createElement("div");
    const applyPopupButton = document.createElement("button");
    applyPopupButton.innerHTML = "Accept";
    applyPopupButton.setAttribute('data-sender', inviteData.sender);
    applyPopupButton.setAttribute('data-receiver', inviteData.receiver);
    applyPopupButton.setAttribute('data-friendshipid', inviteData.friendship_id);
    applyPopupButton.setAttribute("class", "text-success bg-info border-0 fw-bold");
    applyPopupButton.setAttribute("onclick", "applyMatchInvitation(event)");
    applyPopupDiv.appendChild(applyPopupButton);


    // Decline section of error window
    const declinePopupDiv = document.createElement("div");
    const declinePopupButton = document.createElement("button");
    declinePopupButton.innerHTML = "Decline";
    declinePopupButton.setAttribute('data-sender', inviteData.sender);
    declinePopupButton.setAttribute('data-receiver', inviteData.receiver);
    declinePopupButton.setAttribute('data-friendshipid', inviteData.friendship_id);
    declinePopupButton.setAttribute("class", "text-danger bg-info border-0 fw-bold");
    declinePopupButton.setAttribute("onclick", "declineMatchInvitation(event)");
    declinePopupDiv.appendChild(declinePopupButton);
    // errorPopup.append(playerNameDiv);
    errorPopup.append(applyPopupDiv);
    errorPopup.append(declinePopupDiv);
  }
  else {

    // First section of error window
    const messageDisplayWindow = document.createElement("div");
    messageDisplayWindow.setAttribute("class", "flex-grow-1 align-self-center");
    const messageDisplay = document.createElement("span");
    messageDisplay.setAttribute("class", "text-white m-0");
    messageDisplay.innerHTML = innerText = "You have challanged " + inviteData.receiver + " to a match. Wait for " + inviteData.receiver + " ...";
    messageDisplayWindow.appendChild(messageDisplay);
    errorPopup.appendChild(messageDisplayWindow);


    // Close section of error window
    const closePopupDiv = document.createElement("div");
    const closePopupButton = document.createElement("button");
    closePopupButton.innerHTML = "X";
    closePopupButton.setAttribute("class", "text-white bg-info border-0");
    closePopupButton.setAttribute("onclick", "closeError(event)");
    closePopupDiv.appendChild(closePopupButton);

    errorPopup.append(closePopupDiv);
  }



  // Add element to DOM
  parent.appendChild(errorPopup);
}


function greenNotification(errorMsg) {
  let parent = document.getElementById("error-layer");
  const errorPopup = document.createElement("div");
  errorPopup.setAttribute("class", "d-flex flex-row bg-success m-2 p-2 rounded-pill pe-auto");
  errorPopup.setAttribute("id", "error-notification-container");

  // First section of error window
  const messageDisplayWindow = document.createElement("div");
  messageDisplayWindow.setAttribute("class", "flex-grow-1 align-self-center");
  const messageDisplay = document.createElement("p");
  messageDisplay.setAttribute("class", "text-white m-0");
  messageDisplay.innerHTML = errorMsg;
  messageDisplayWindow.appendChild(messageDisplay);
  errorPopup.appendChild(messageDisplayWindow);

  // Second section of error window
  const closePopupDiv = document.createElement("div");
  const closePopupButton = document.createElement("button");
  closePopupButton.innerHTML = "X";
  closePopupButton.setAttribute("class", "text-white bg-success border-0");
  closePopupButton.setAttribute("onclick", "closeError(event)");
  closePopupDiv.appendChild(closePopupButton);
  errorPopup.append(closePopupDiv);

  // Add element to DOM
  parent.appendChild(errorPopup);
}

async function simulateError() {
  const url = "/simulate_error"

  fetch(url).then(async (response) => {
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }
  }).catch((error) => {
    handleError(error);
  });
}


const changeSelect = changeSelectFunction((event) => {
  document.getElementById('avatarPic').setAttribute("src", `https://localhost/static/images/${event.target.value}`);
}, []);

function deleteHeader() {
  let header = document.getElementsByClassName("header")[0];

  header.replaceChildren();
}

function deleteMain() {
  let main = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
  console.log(main)

  main.replaceChildren();
}

// 'id': 1,
// 'type': 'canvas',
// 'identifier': 'pongCanvas',
// 'width': 800,
// 'height': 400

function elementCustomize(element, item) {
  if (item.class && item.class != "") element.setAttribute("class", item.class);
  if (item.identifier && item.identifier != "")
    element.setAttribute("id", item.identifier);
  if (item.text && item.text != "") element.innerHTML = item.text;
  if (item.for && item.for != "") element.setAttribute("for", item.for);
  if (item.inputType && item.inputType != "")
    element.setAttribute("type", item.inputType);
  if (item.action && item.action != "")
    element.setAttribute("action", item.action);
  if (item.onclick && item.onclick != "")
    element.setAttribute("onclick", item.onclick);
  if (item.width) element.setAttribute("width", item.width);
  if (item.height) element.setAttribute("height", item.height);
  if (item.method && item.method != "")
    element.setAttribute("method", item.method);
  if (item.name && item.name != "") element.setAttribute("name", item.name);
  if (item.form && item.form != "") element.setAttribute("form", item.form);
  if (item.src && item.src != "") element.setAttribute("src", item.src);
  if (item.value && item.value != "") element.setAttribute("value", item.value);
  if (item.onsubmit && item.onsubmit != "") element.setAttribute("onsubmit", item.onsubmit);
  if (item.selected && item.selected != "") element.setAttribute("selected", item.selected);
  if (item.placeholder && item.placeholder != "") element.setAttribute("placeholder", item.placeholder)
  // if ()
  // if (item.text && item.text != "") element.textContent = item.text;
}

function divLoader(parent, itemList) {
  itemList.forEach((item) => {
    if (item.type == "div" || item.type == "form" || item.type == "select" || item.type == "table" || item.type == "thead" || item.type == "tr") {
      let subElement = document.createElement(item.type);
      elementCustomize(subElement, item);
      if (item.content && item.content != "")
        divLoader(subElement, item.content);
      parent.appendChild(subElement);
    } else {
      let subElement = document.createElement(item.type);
      elementCustomize(subElement, item);
      parent.appendChild(subElement);
    }
  });
}

function headerLoad(json) {
  json.headerItems.forEach((item) => {
    console.log(item.type);
    let parent = document.getElementsByClassName("header")[0];
    let element = document.createElement(item.type);
    if (item.type == "div" || item.type == "form")
      if (item.content && item.content != "") divLoader(element, item.content);

    elementCustomize(element, item);
    parent.appendChild(element);
  });
}

// LOAD FUNCTIONS
// MAIN

window.onpopstate = function (event) {

  console.log("RELATED TO HISTORY");
  const buffer = JSON.stringify(event.state);
  if (buffer == null) {
    console.log("Buffer ist NULL");
    return;
  }
  const json = JSON.parse(buffer);
  if (json == null) {
    console.log("Json ist NULL");
    return;
  }
  console.log(json);

  LOAD_DATA(json, false);
};

function LOAD_DATA(json, shouldPush, state_json = null) {
  console.log("state_json is: " + state_json);
  if (shouldPush)
    history.pushState(json, null);
  deleteHeader();
  deleteMain();

  // CREATE HEADER

  headerLoad(json);

  // CREATE CONTAINER

  switch (json.id) {
    case "main":
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form")
            divLoader(element, item.content);
          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case "play_menu":
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form")
            divLoader(element, item.content);
          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case 'match_history':
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form" || item.type == "table")
            divLoader(element, item.content);

          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case "profile":
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form" || item.type == "table")
            divLoader(element, item.content);

          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case "tournament_main":
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form")
            divLoader(element, item.content);

          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case "tournament_create":
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form")
            divLoader(element, item.content);

          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case "tournament_select":
      {
        console.log(json.menuItems);
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form" || item.type == "table")
            divLoader(element, item.content);

          elementCustomize(element, item);
          parent.appendChild(element);
        });
      }
      break;
    case "singleplayer_menu":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement("div");
          elementCustomize(element, item);
          divLoader(element, item.content);
          parent.appendChild(element);
        });
      }
      break;
    case "online_menu":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement("div");
          elementCustomize(element, item);
          divLoader(element, item.content);
          parent.appendChild(element);
        });
      }
      break;
    case "local_menu":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement("div");
          elementCustomize(element, item);
          divLoader(element, item.content);
          parent.appendChild(element);
        });
      }
      break;
    case "register":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element;
          if (item.type == "div")
            element = document.createElement("div");
          else if (item.type == "select")
            element = document.createElement("select")
          elementCustomize(element, item);
          divLoader(element, item.content);
          parent.appendChild(element);
        });
        document
          .getElementById("registration_form")
          .addEventListener("submit", submit_registration_form, { once: true });
        document.getElementById("Avatar").addEventListener("change", changeSelect);

      }
      break;
    case "login":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement("div");
          elementCustomize(element, item);
          divLoader(element, item.content);
          parent.appendChild(element);
        });
        document.getElementById("login_form");
      }
      break;
    case "settings":
      {
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          console.log(parent);
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form" || item.type == "select")
            divLoader(element, item.content);

          elementCustomize(element, item);
          parent.appendChild(element);

        });
      }
      break;
    case "singleplayer_game":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement(item.type);
          elementCustomize(element, item);
          parent.appendChild(element);
        });
        startSingleGame();
      }
      break;
    case "local_game":
      {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement(item.type);
          elementCustomize(element, item);
          parent.appendChild(element);
        });
        startLocalGame(state_json);
      }
      break;
    case "online_game":
      {

        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        json.menuItems.forEach((item) => {
          let element = document.createElement(item.type);
          elementCustomize(element, item);
          parent.appendChild(element);
        });
        startOnlineGame();
      }
      break;
  }

}


async function load_main() {
  let url = "/indexPost";

  const csrfToken = await getCsrfToken();

  fetch(url, {
    method: "GET",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    // body: JSON.stringify({
    //   tournament_name: document.getElementById('Avatar').value
    // }),
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
      LOAD_DATA(json, true);
      // history.pushState(json, null);
      // deleteHeader();
      // deleteMain();

      // // CREATE HEADER

      // headerLoad(json);

      // // CREATE CONTAINER

      // json.menuItems.forEach((item) => {
      //   let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      //   let element = document.createElement(item.type);
      //   if (item.type == "div" || item.type == "form")
      //     divLoader(element, item.content);

      //   elementCustomize(element, item);
      //   parent.appendChild(element);
      // });
    })
    .catch((error) => {
      handleError(error);
    });
}

window.onload = function () {
  let url = "/indexPost";
  console.log("ONLOAD FUNCTION CALLED");
  console.log(url);
  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      history.replaceState(json, null);
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

      // function to replace top of the History stack
    })
    .catch((error) => {
      handleError(error);
    });
};

function load_playMenu() {
  let url = "/play";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);
      // history.pushState(json, null);
      // deleteHeader();
      // deleteMain();

      // // CREATE HEADER

      // headerLoad(json);

      // // CREATE CONTAINER

      // json.menuItems.forEach((item) => {
      //   let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      //   let element = document.createElement(item.type);
      //   if (item.type == "div" || item.type == "form")
      //     divLoader(element, item.content);

      //   elementCustomize(element, item);
      //   parent.appendChild(element);

      //   // div.appendChild(element);
      // });
    })
    .catch((error) => {
      handleError(error);
    });
}

async function loadHistory() {
  let url = "/match_history";

  const csrfToken = await getCsrfToken();


  fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    // body: JSON.stringify({
    //   tournament_name: document.getElementById('Avatar').value
    // }),
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
      LOAD_DATA(json, true);
      // history.pushState(json, null);
      // deleteHeader();
      // deleteMain();

      // // CREATE HEADER
      // // console.log(json)

      // headerLoad(json);

      // // CREATE CONTAINER

      // json.menuItems.forEach((item) => {
      //   let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      //   let element = document.createElement(item.type);
      //   if (item.type == "div" || item.type == "form" || item.type == "table")
      //     divLoader(element, item.content);

      //   elementCustomize(element, item);
      //   parent.appendChild(element);
      // });
    })
    .catch((error) => {
      handleError(error);
    });
}

// GAMES

function single_pregame() {
  let url = "/singleplayer_menu";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);


      // let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      // json.menuItems.forEach((item) => {
      //   let element = document.createElement("div");
      //   elementCustomize(element, item);
      //   divLoader(element, item.content);
      //   parent.appendChild(element);
      // });
    });

  console.log("single pregame called");
}

function local_pregame() {
  let url = "/local_menu";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);
    });
}

//CONTINUE


async function submit_local_pregame_invite(player1, player2) {
  
  let validation = validate_local_pregame_invite();

  if (!validation)
    return;

  const csrfToken = await getCsrfToken();

  fetch('/local_check', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
      Accept: "application/json",
    },
    body: JSON.stringify({ player1, player2 }),
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    }).then((json) => {
      console.log(json);
      console.log(json.player1)
      load_localGame(json);
    }).catch((error) => {
      handleError(error);
    })
}


async function submit_local_pregame(event) {
  event.preventDefault()

  let validation = validate_local_pregame();

  if (!validation)
    return;

  player1 = sanitizeInput(document.getElementById('player1').value);
  player2 = sanitizeInput(document.getElementById('player2').value);

  console.log(player1);

  const csrfToken = await getCsrfToken();

  fetch('/local_check', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
      Accept: "application/json",
    },
    body: JSON.stringify({ player1, player2 }),
    credentials: "include",
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    }).then((json) => {
      console.log(json);
      console.log(json.player1)
      load_localGame(json);
    }).catch((error) => {
      handleError(error);
    })
}

function validate_local_pregame_invite(player1, player2) {
  if (player1 == "") {
    alert("Player1 must be filled out");
    return false;
  }
  else if (player2 == "") {
    alert("Player2 must be filled out");
    return false;
  }

  return true
}


function validate_local_pregame() {
  player1 = document.getElementById('player1').value;
  player2 = document.getElementById('player2').value;

  if (player1 == "") {
    alert("Player1 must be filled out");
    return false;
  }
  else if (player2 == "") {
    alert("Player2 must be filled out");
    return false;
  }

  return true
}

function online_pregame() {
  let url = "/online_menu";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);
    })
    .catch((error) => {
      handleError(error);
    });
}

function load_register() {
  let url = "/register";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);


    })
    .catch((error) => {
      handleError(error);
    });
}

function load_login() {
  let url = "/login";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);


    }, { once: true })
    .catch((error) => {
      handleError(error);
    });
}

function load_singleGame() {
  let url = "/singleplayer_game";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, false);


    })
    .catch((error) => {
      handleError(error);
    });
}

function load_localGame(state_json) {
  let url = "/local_game";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, false, state_json);


    })
    .catch((error) => {
      handleError(error);
    });
}

function load_onlineGame() {
  let url = "/online_game";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, false);
    })
    .catch((error) => {
      handleError(error);
    });
}

// TOURNAMENT

function load_tournament_main() {
  let url = "/tournament_main";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {
      LOAD_DATA(json, true);
    })
    .catch((error) => {
      handleError(error);
    });
}

function load_tournament_create() {
  let url = "/tournament_create";

  fetch(url)
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      else return response.json();
    })
    .then((json) => {

      LOAD_DATA(json, true);
    })
    .catch((error) => {
      handleError(error);
    });
}

let player_list = [];

function tournament_player_add(event) {
  event.preventDefault();
  console.log("tournament_player_add called");
  let player_list_dom = document.getElementById("tournament_ul");
  let player_input = document.getElementById('player');
  let player_input_value = sanitizeInput(player_input.value);

  let new_li = document.createElement('li');
  new_li.textContent = player_input_value; // Make sure to set the text content of the new list item

  if (!player_input_value) {
    alert("Wrong Input");
    return;
  }

  if (player_list.includes(player_input_value)) {
    alert("Player already in the tournament");
    return;
  }

  player_list.push(sanitizeInput(player_input_value));
  player_input.value = "";
  player_list_dom.appendChild(new_li);

  console.log(player_list);

  return false;
}

async function submit_tournament_create(event) {
  event.preventDefault();

  let validation = validate_tournament_create();

  if (!validation) {
    // player_list = [];
    return;
  }

  let tournament_name = document.getElementById('tournament_name').value;

  const csrfToken = await getCsrfToken();

  fetch("/tournament_create_check", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      tournament_name: tournament_name,
      players: player_list
    }),
    credentials: "include",
  }).then(async (response) => {
    if (response.ok)
      player_list = [];
    else if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }
    console.log('tournament created');
    return response.json();
  }).then((json) => {
    load_next_step(json);
  }).catch((error) => {
    handleError(error);
  })
}

function validate_tournament_create() {
  let tournament_name = document.getElementById('tournament_name').value;

  if (!tournament_name) {
    alert("Please give tournament name");
    return false;
  }

  if (player_list.length < 3) {
    alert("Please add at least 3 players to your tournament");
    return false;
  }

  return true;
}

async function load_tournament_select() {
  let url = "/tournament_select";

  const csrfToken = await getCsrfToken();


  fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      tournament_name: document.getElementById('Avatar').value
    }),
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
      gameId = json.game
      LOAD_DATA(json, true);
    })
    .catch((error) => {
      handleError(error);
    });
}

async function load_tournament_localGame() {
  console.log("load_tournament_localGame() is called");
  console.log("Game_id = " + gameId);

  let url = "/tournament_game_check";

  const csrfToken = await getCsrfToken();


  fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      'game_id': gameId
    }),
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
      console.log(json);
      deleteHeader();
      deleteMain();
      headerLoad(json.menu);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menu.menuItems.forEach((item) => {
        let element = document.createElement(item.type);
        elementCustomize(element, item);
        parent.appendChild(element);
      });
      startTournamentGame(json);
    })
    .catch((error) => {
      handleError(error);
    });
}

function inviteToTournament(playerName) {
  let listElement = document.getElementById("tournament_ul");

  const newParticipant = document.createElement("li");
  newParticipant.innerHTML = playerName;
  player_list.push(playerName);

  listElement.append(newParticipant);

}