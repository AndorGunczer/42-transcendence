// Set up an event listener for the play button
const backButton = document.getElementById("backButton");
const singlePlayerButton = document.getElementById("singlePlayerButton");
const localButton = document.getElementById("localButton");
const onlineButton = document.getElementById("onlineButton");

console.log("loaded");

singlePlayerButton.addEventListener("click", function () {
  // Define the URL of the Django server endpoint
  const url = "/singleplayer";

  // Make an asynchronous GET request to the server
  fetch(url)
    .then((response) => {
      // Check if the response status is ok (status code 200-299)
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      // Return the response as text (HTML)
      return response.text();
    })
    .then((html) => {
      // Find the target element to update
      const targetDiv = document.getElementById("targetDiv");
      // Update the target element with the server's response
      targetDiv.innerHTML = html;

      // Load additional JavaScript and CSS from the new content
      // Find script and link tags in the new HTML
      console.log(html);
      const scriptTags = targetDiv.querySelectorAll("script");
      const linkTags = targetDiv.querySelectorAll("link");

      // Load each script tag
      scriptTags.forEach((script) => {
        // Create a new script element and copy the attributes
        const newScript = document.createElement("script");
        newScript.src = script.src;
        newScript.type = script.type || "text/javascript";

        // Append the script to the document body to load it
        document.body.appendChild(newScript);
      });

      // Load each link tag (CSS)
      linkTags.forEach((link) => {
        // Create a new link element and copy the attributes
        const newLink = document.createElement("link");
        newLink.href = link.href;
        newLink.rel = link.rel || "stylesheet";
        newLink.type = link.type || "text/css";

        // Append the link to the document head to load it
        document.head.appendChild(newLink);
      });
    })
    .catch((error) => {
      // Handle any errors that occurred during the request
      console.error("Error:", error);
    });
});
