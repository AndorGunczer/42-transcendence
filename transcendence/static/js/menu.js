// JAVASCRIPT CODE FOR MAIN MENU

playButton = document.getElementById("button-play");

// DYNAMIC PAGE LOAD WITH JSON

playButton.addEventListener("click", function () {
  load_playMenu();
});

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
}

function divLoader(parent, itemList) {
  // let currentElement = document.createElement(item.type);
  // if (item.class) currentElement.class = item.class;

  itemList.forEach((item) => {
    if (item.type == "div" || item.type == "form") {
      let subElement = document.createElement(item.type);
      elementCustomize(subElement, item);
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

function headerLoad(json) {
  json.headerItems.forEach((item) => {
    let parent = document.getElementsByClassName("header")[0];
    let element = document.createElement(item.type);
    if (item.type == "p") element.innerHTML = item.label;
    if (item.type == "div") {
      element.setAttribute("class", "menu-button");
    }
    if (item.type == "button") {
      let div = document.createElement("div");
      parent.appendChild(div);
      element.innerHTML = item.label;
      element.setAttribute("class", "menu-button");
      element.setAttribute("onclick", item.action);
    }
    parent.appendChild(element);
  });
}

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
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
    });
}

function load_login() {
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
        let element = document.createElement("div");
        elementCustomize(element, item);
        divLoader(element, item.content);
        parent.appendChild(element);
      });
    });
}