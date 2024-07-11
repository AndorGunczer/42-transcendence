async function submit_registration_form(event) {
  event.preventDefault(); // Prevent default form submission

  const csrfToken = await getCsrfToken();

  console.log(document.getElementById("username").value);

  // let formData = new FormData();
  // formData.append("username", document.getElementById("username").value);
  // formData.append("password", document.getElementById("password").value);

  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  let avatar = document.getElementById("Avatar").value;

  // console.log(formData);

  fetch("/registration_check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ username, password, avatar }), // JSON.stringify({ username, password })
    credentials: "include",
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

// 'id': 1,
// 'type': 'canvas',
// 'identifier': 'pongCanvas',
// 'width': 800,
// 'height': 400

// function load_game(json) {
//   console.log("Next step:");
//   deleteHeader();
//   deleteMain();

//   // CREATE HEADER

//   // headerLoad(json);

//   // CREATE CONTAINER

//   json.menuItems.forEach((item) => {
//     let parent = document.getElementsByClassName("container")[0];
//     let element = document.createElement(item.type);
//     if (item.type == "div" || item.type == "form")
//       divLoader(element, item.content);

//     elementCustomize(element, item);
//     parent.appendChild(element);
//   })
// };

async function submit_login_form(event) {
  event.preventDefault(); // Prevent default form submission

  const csrfToken = await getCsrfToken();


  console.log(document.getElementById("username").value);

  // let formData = new FormData();
  // formData.append("username", document.getElementById("username").value);
  // formData.append("password", document.getElementById("password").value);

  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;

  // console.log(formData);

  fetch("/login_check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ username, password }), // JSON.stringify({ username, password })
    credentials: "include",
  })
    .then((response) => {
      console.log("step 1");
      return response.json()
    })
    .then((json) => {
      console.log("step 2")
      load_next_step(json);
    })
    .catch((error) =>
      console.error("Error submitting login form:", error)
    );
}

async function jwt_kriegen(event) {
  event.preventDefault(); // Prevent default form submission behavior

  const csrfToken = await getCsrfToken();

  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;

  console.log("Starting fetch request...");

  fetch("/api/token/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
      Accept: "application/json",
    },
    body: JSON.stringify({ username, password }),
    credentials: "include",
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
      console.error("There was an error: ", error);
    });
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
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("Token Cookies Deleted Successfully.");
      load_main();
    })
    .catch((error) => {
      console.error("there was an error: ", error);
    });
}

async function getCsrfToken() {
  const response = await fetch("/api/csrf-token/", {
    method: "GET",
    credentials: "include",
  });
  const data = await response.json();
  return data.csrfToken;
}

async function uploadAvatar() {
  const csrfToken = await getCsrfToken();

  const fileInput = document.getElementById('fileUpload');
  const file = fileInput.files[0];

  if (!file) {
      alert('Please Select a File to Upload');
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
  .then(response => response.json())
  .then(json => {
    deleteHeader();
    deleteMain();

    // CREATE HEADER

    headerLoad(json);

    // CREATE CONTAINER

    json.menuItems.forEach((item) => {
      let parent = document.getElementsByClassName("container")[0];
      let element = document.createElement(item.type);
      if (item.type == "div" || item.type == "form" || item.type == "select")
        divLoader(element, item.content);

      elementCustomize(element, item);
      parent.appendChild(element);

      // div.appendChild(element);
    });
  })
  .catch(error => {
      console.error('Error:', error);
  });
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
  .then(response => response.json())
  .then(json => {
    deleteHeader();
    deleteMain();

    // CREATE HEADER

    headerLoad(json);

    // CREATE CONTAINER

    json.menuItems.forEach((item) => {
      let parent = document.getElementsByClassName("container")[0];
      let element = document.createElement(item.type);
      if (item.type == "div" || item.type == "form" || item.type == "select")
        divLoader(element, item.content);

      elementCustomize(element, item);
      parent.appendChild(element);

      // div.appendChild(element);
    });
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

async function saveChanges() {
  event.preventDefault();

  const csrfToken = await getCsrfToken();

  let url = '/save_changes';

  let username = document.getElementById('username').value;
  let avatar = document.getElementById('avatar').value;

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
  .then(response => response.json())
  .then(json => {
    deleteHeader();
    deleteMain();

    // CREATE HEADER

    headerLoad(json);

    // CREATE CONTAINER

    json.menuItems.forEach((item) => {
      let parent = document.getElementsByClassName("container")[0];
      let element = document.createElement(item.type);
      if (item.type == "div" || item.type == "form" || item.type == "select")
        divLoader(element, item.content);

      elementCustomize(element, item);
      parent.appendChild(element);

      // div.appendChild(element);
    });
  })
  .catch(error => {
      console.error('Error:', error);
  });
}