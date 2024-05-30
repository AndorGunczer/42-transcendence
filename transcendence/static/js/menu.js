// JAVASCRIPT CODE FOR MAIN MENU

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
}

function divLoader(parent, itemList) {
  // let currentElement = document.createElement(item.type);
  // if (item.class) currentElement.class = item.class;

  itemList.forEach((item) => {
    if (item.type == "div" || item.type == "form") {
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

  // function autoLoader(parent, fullList) {
  //   fullList.for
  // }

  // parent.appendChild(currentElement);
}

// if (item.type == "div" || item.type == "form") {
//   let subElement = document.createElement(item.type);
//   elementCustomize(subElement, item);
//   divLoader(subElement, item.content);
//   parent.appendChild(subElement);
// } else {
//   let subElement = document.createElement(item.type);
//   elementCustomize(subElement, item);
//   parent.appendChild(subElement);
// }

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

function load_main() {
  let url = "/indexPost";
  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie
  console.log(accessToken);

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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
  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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

function single_pregame() {
  let url = "/singleplayer_menu";

  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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

  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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

  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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

  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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
        .getElementById("registration_form")
        .addEventListener("submit", submit_registration_form);
    });
}

function load_login() {
  let url = "/login";

  let accessToken = localStorage.getItem("access_token"); // or sessionStorage, or document.cookie

  // Create headers object and conditionally add the Authorization header
  let headers = new Headers();
  if (accessToken) {
    headers.append("Authorization", "Bearer " + accessToken);
  }

  fetch(url, {
    method: "GET", // or 'POST', depending on your needs
    headers: headers,
  })
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
        .addEventListener("submit", jwt_kriegen);
    });
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
