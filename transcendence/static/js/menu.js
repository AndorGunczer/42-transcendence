// JAVASCRIPT CODE FOR MAIN MENU

// HELPER FUNCTIONS

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
  let main = document.getElementsByClassName("container")[0];

  main.replaceChildren();
}

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
  // if (item.text && item.text != "") element.textContent = item.text;
}

function divLoader(parent, itemList) {
  itemList.forEach((item) => {
    if (item.type == "div" || item.type == "form" || item.type == "select") {
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
        let parent = document.getElementsByClassName("container")[0];
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
        let parent = document.getElementsByClassName("container")[0];
        let element = document.createElement(item.type);
        if (item.type == "div" || item.type == "form")
          divLoader(element, item.content);

        elementCustomize(element, item);
        parent.appendChild(element);

        // div.appendChild(element);
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
      let parent = document.getElementsByClassName("container")[0];
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
      let parent = document.getElementsByClassName("container")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
    });
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
      let parent = document.getElementsByClassName("container")[0];
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
      let parent = document.getElementsByClassName("container")[0];
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
      let parent = document.getElementsByClassName("container")[0];
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
      let parent = document.getElementsByClassName("container")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement(item.type);
        elementCustomize(element, item);
        parent.appendChild(element);
      });
      startSingleGame();
    });
}

function load_localGame() {
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
      let parent = document.getElementsByClassName("container")[0];
      json.menuItems.forEach((item) => {
        let element = document.createElement(item.type);
        elementCustomize(element, item);
        parent.appendChild(element);
      });
      startLocalGame();
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
      let parent = document.getElementsByClassName("container")[0];
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
          let parent = document.getElementsByClassName("container")[0];
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
          let parent = document.getElementsByClassName("container")[0];
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

      player_list.push(player_input.value);
      player_input.value = "";
      player_list_dom.appendChild(new_li);

      console.log(player_list);

      return false;
    }

    async function submit_tournament_create(event) {
      event.preventDefault();

      const csrfToken = await getCsrfToken();

      fetch("https://127.0.0.1:8000/tournament_create_check", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
          tournament_name: 'test_tournament',
          players: player_list
        }),
        credentials: "include",
      }).then((response) => {
        console.log('tournament created');
        return response.json();
      }).then((json) => {
        load_next_step(json);
      }).catch((error) => {
        console.log(error);
      })

      console.log('submit_tournament_create(event) called');
      player_list = [];
    }