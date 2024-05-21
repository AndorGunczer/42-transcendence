// JAVASCRIPT CODE FOR MAIN MENU

playButton = document.getElementById("button-play");
loginButton = document.getElementById("button-login");
registerButton = document.getElementById("button-register");

// STATIC PAGE LOAD

// playButton.addEventListener("click", () => {
//   // Define the URL of the Django server endpoint
//   const url = "/play";

//   // Redirect the browser to the specified URL
//   window.location.href = url;
// });

// DYNAMIC PAGE LOAD WITH JSON

playButton.addEventListener("click", function () {
  // Define the URL of the Django server endpoint
  const url = "/play";

  // Make an asynchronous GET request to the server
  fetch(url)
    .then((response) => {
      // Check if the response status is ok (status code 200-299)
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      // Return the response as text (HTML)
      console.log(response);
      return response.json();
    })
    .then((json) => {
      console.log(json);
      // Find the target element to update
      buttonsToReplace = Array.from(
        document.getElementsByClassName("menu-button")
      );
      for (let i = 0; i < buttonsToReplace.length; i++) {
        let parent = buttonsToReplace[i].parentElement;
        let newButton = document.createElement("button");

        buttonsToReplace[i].remove();
        newButton.setAttribute("class", "menu-button");
        newButton.setAttribute("onclick", json.menuItems[i].action);
        newButton.innerHTML = json.menuItems[i].label;

        parent.appendChild(newButton);
      }
      // buttonsToReplace.forEach((button) => {
      //   button.innerHTML = json.menuItems[0].label;
      // });
    })
    .catch((error) => {
      // Handle any errors that occurred during the request
      console.error("Error:", error);
    });
});

function deleteHeader() {
  let header = document.getElementsByClassName("header")[0];

  header.replaceChildren();
}

function deleteMain() {
  let main = document.getElementsByClassName("container")[0];

  main.replaceChildren();
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

      json.headerItems.forEach((item) => {
        let parent = document.getElementsByClassName("header")[0];
        let element = document.createElement(item.type);
        if (item.type == "p") element.innerHTML = item.label;
        if (item.type == "div") {
          element.setAttribute("class", "menu-button");
        }
        parent.appendChild(element);
      });

      // CREATE CONTAINER

      json.menuItems.forEach((item) => {
        let parent = document.getElementsByClassName("container")[0];
        let element = document.createElement(item.type);
        if (item.type == "div") {
          if (item.class != "") element.setAttribute("class", item.class);
          if (item.identifier != "")
            element.setAttribute("id", item.identifier);
          if (item.content.length != 0) {
            item.content.forEach((subItem) => {
              if (subItem.type == "h1" || subItem.type == "p") {
                let subElement = document.createElement(subItem.type);
                subElement.innerHTML = subItem.label;
                element.appendChild(subElement);
              } else if (subItem.type == "button") {
                let subElement = document.createElement(subItem.type);
                subElement.innerHTML = subItem.label;
                if (subItem.class != "")
                  subElement.setAttribute("class", subItem.class);
                if (subItem.identifier != "")
                  subElement.setAttribute("id", subItem.identifier);
                subElement.setAttribute("onclick", subItem.action);
                element.appendChild(subElement);
              }
            });
          }
          parent.appendChild(element);
        }
        if (item.type == "button") {
          let div = document.createElement("div");
          parent.appendChild(div);
          element.innerHTML = item.label;
          element.setAttribute("class", "menu-button");
          element.setAttribute("onclick", item.action);

          div.appendChild(element);
        }
      });
    });
}

function single_pregame() {
  console.log("single pregame called");
}

function local_pregame() {
  console.log("local pregame called");
}

function online_pregame() {
  console.log("online pregame called");
}
