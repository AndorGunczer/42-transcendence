async function submit_registration_form(event) {
  event.preventDefault(); // Prevent default form submission

  let validation = validate_registration_form();

  if (!validation) {
    return ; 
  }

  const csrfToken = await getCsrfToken();

  console.log(document.getElementById("username").value);

  // let formData = new FormData();
  // formData.append("username", document.getElementById("username").value);
  // formData.append("password", document.getElementById("password").value);

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
    .then((response) => response.json())
    .then((json) => {
      load_next_step(json);
    })
    .catch((error) =>
      console.error("Error submitting registration form:", error)
    );
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
  // Implement this function to handle the next step after successful registration
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
//     let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];;
//     let element = document.createElement(item.type);
//     if (item.type == "div" || item.type == "form")
//       divLoader(element, item.content);

//     elementCustomize(element, item);
//     parent.appendChild(element);
//   })
// };

async function submit_login_form(event) {
  event.preventDefault(); // Prevent default form submission

  let validation = validate_login_form();

  if (!validation)
    return ;

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
  .then((response) => response.json())
  .then((json) => {
    console.log(json.status);
      if (json.status === 'otp_sent') {
        // Show OTP popup
        document.getElementById("otpPopup").style.display = "block";
      } else {
        load_main();
      }
      
  })
  .catch((error) => console.error("Error submitting login form:", error));
}

function validate_login_form(){
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
  .then((response) => response.json())
  .then((json) => {
      load_main()
  })
  .catch((error) => console.error("Error verifying OTP:", error));
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

async function uploadAvatar(event) {
  event.preventDefault();
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
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
      console.log(parent);
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
      let parent = document.getElementsByClassName("container")[0] ? document.getElementsByClassName("container")[0] : document.getElementsByClassName("container-fluid")[0];
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
  .then(response => response.json())
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
  .catch(error => {
      console.error('Error:', error);
  });
}