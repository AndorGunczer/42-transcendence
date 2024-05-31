function submit_registration_form(event) {
  event.preventDefault(); // Prevent default form submission

  console.log(document.getElementById("username").value);

  let formData = new FormData();
  formData.append("username", document.getElementById("username").value);
  formData.append("password", document.getElementById("password").value);

  console.log(formData);

  fetch("/registration_check", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((json) => {
      load_next_step(json);
    })
    .catch((error) =>
      console.error("Error submitting registration form:", error)
    );
}

function load_next_step(json) {
  // Implement this function to handle the next step after successful registration
  console.log("Next step:");
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
  // For example, load another part of your SPA based on the next step
}

function submit_login_form(event) {
  event.preventDefault(); // Prevent default form submission

  console.log(document.getElementById("username").value);

  let formData = new FormData();
  formData.append("username", document.getElementById("username").value);
  formData.append("password", document.getElementById("password").value);

  console.log(formData);

  fetch("/login_check", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((json) => {
      load_next_step(json);
    })
    .catch((error) =>
      console.error("Error submitting registration form:", error)
    );
}

function jwt_kriegen(event) {
  event.preventDefault(); // Prevent default form submission behavior

  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;

  console.log("Starting fetch request...");

  fetch("https://127.0.0.1:8000/api/token/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({ username, password }),
  })
    .then((response) => {
      console.log("response from Javascript Token process: " + response.ok);
      console.log("response from Javascript Token process: " + response.status);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      console.log("Got to response");
      return response.json();
    })
    .then((data) => {
      console.log("Response data:", data);
      if (data.message === "Token created") {
        console.log("Tokens stored successfully in cookies.");
        load_main();
      } else {
        console.error("Unexpected response:", data);
      }
    })
    .catch((error) => {
      console.error("There was an error:", error);
    });
}
