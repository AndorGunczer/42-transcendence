function checkAndRefreshToken() {
  fetch("/api/token/refresh/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.message === "Token refreshed") {
        console.log("Token refreshed successfully.");
      } else if (data.message === "Refresh token missing"){
        console.log(data.message);}
        else {
        console.error("Unexpected response:", data);
      }
    })
    .catch((error) => {
      console.error("There was an error:", error);
    });
}

// Call checkAndRefreshToken periodically or based on user actions
setInterval(checkAndRefreshToken, 15 * 60 * 1000); // every 15 minutes
