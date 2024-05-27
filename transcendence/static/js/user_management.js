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
