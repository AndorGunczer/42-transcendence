// JAVASCRIPT CODE FOR MAIN MENU

// HELPER FUNCTIONS

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
  return function(event) {
    callback(event);
  };
}


const changeSelect = changeSelectFunction((event) => {
  document.getElementById('avatarPic').setAttribute("src", `https://127.0.0.1:8000/static/images/${event.target.value}`);
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

function load_main() {
  let url = "/indexPost";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
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
    });
}

function load_playMenu() {
  let url = "/play";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      deleteHeader();
      deleteMain();

      // CREATE HEADER

      headerLoad(json);

      // CREATE CONTAINER

      json.menuItems.forEach((item) => {
        let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
        let element = document.createElement(item.type);
        if (item.type == "div" || item.type == "form")
          divLoader(element, item.content);

        elementCustomize(element, item);
        parent.appendChild(element);

        // div.appendChild(element);
      });
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
      .then((response) => {
        if (!response.ok) console.log("yeaah");
        else return response.json();
      })
      .then((json) => {
        deleteHeader();
        deleteMain();
  
        // CREATE HEADER
        // console.log(json)
  
        headerLoad(json);
  
        // CREATE CONTAINER
  
        json.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form" || item.type == "table")
            divLoader(element, item.content);
  
          elementCustomize(element, item);
          parent.appendChild(element);
        });
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
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
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
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
    });
}

//CONTINUE

async function submit_local_pregame(event) {
  event.preventDefault()

  let validation = validate_local_pregame();

  if (!validation)
    return ;

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
    .then((response) => {
      if (!response.ok) console.log("okay");
      else return response.json();
    }).then((json) => {
      console.log(json);
      console.log(json.player1)
      load_localGame(json);
    })
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
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
    });
}

function load_register() {
  let url = "/register";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      deleteHeader();
      deleteMain();
      headerLoad(json);
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
        .addEventListener("submit", submit_registration_form, {once: true});
      document.getElementById("Avatar").addEventListener("change", changeSelect);
    });
}

function load_login() {
  let url = "/login";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
      document
        .getElementById("login_form")
        .addEventListener("submit", jwt_kriegen, {once: true});
    }, {once: true});
}

function load_singleGame() {
  let url = "/singleplayer_game";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      console.log(json);
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement(item.type);
        elementCustomize(element, item);
        parent.appendChild(element);
      });
      startSingleGame();
    });
}

function load_localGame(state_json) {
  let url = "/local_game";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      console.log(json);
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement(item.type);
        elementCustomize(element, item);
        parent.appendChild(element);
      });
      startLocalGame(state_json);
    });
}

function load_onlineGame() {
  let url = "/online_game";

  fetch(url)
    .then((response) => {
      if (!response.ok) console.log("yeaah");
      else return response.json();
    })
    .then((json) => {
      console.log(json);
      deleteHeader();
      deleteMain();
      headerLoad(json);
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement(item.type);
        elementCustomize(element, item);
        parent.appendChild(element);
      });
      startOnlineGame();
    });
}

  // TOURNAMENT

  function load_tournament_main() {
    let url = "/tournament_main";
  
    fetch(url)
      .then((response) => {
        if (!response.ok) console.log("yeaah");
        else return response.json();
      })
      .then((json) => {
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
      });
  }

  function load_tournament_create() {
    let url = "/tournament_create";
  
    fetch(url)
      .then((response) => {
        if (!response.ok) console.log("yeaah");
        else return response.json();
      })
      .then((json) => {
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
      });
  }

    let player_list = [];

    function tournament_player_add(event) {
      event.preventDefault();
      console.log("tournament_player_add called");
      let player_list_dom = document.getElementById("tournament_ul");
      let player_input = document.getElementById('player');

      let new_li = document.createElement('li');
      new_li.textContent = player_input.value; // Make sure to set the text content of the new list item

      if (player_list.includes(player_input.value)) {
        alert("Player already in the tournament");
        return ;
      }

      player_list.push(sanitizeInput(player_input.value));
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
        return ;
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
      }).then((response) => {
        if (response.ok)
          player_list = [];
        console.log('tournament created');
        return response.json();
      }).then((json) => {
        load_next_step(json);
      }).catch((error) => {
        console.log(error);
      })

      console.log('submit_tournament_create(event) called');
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

let gameId;

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
      .then((response) => {
        if (!response.ok) console.log("yeaah");
        else return response.json();
      })
      .then((json) => {
        deleteHeader();
        deleteMain();
  
        // CREATE HEADER
  
        headerLoad(json.menu);
        gameId = json.game;
  
        // CREATE CONTAINER
  
        json.menu.menuItems.forEach((item) => {
          let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
          let element = document.createElement(item.type);
          if (item.type == "div" || item.type == "form" || item.type == "table")
            divLoader(element, item.content);
  
          elementCustomize(element, item);
          parent.appendChild(element);
        });
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
    .then((response) => {
      if (!response.ok) console.log("yeaah");
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
    });
}