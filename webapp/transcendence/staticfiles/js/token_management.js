function checkAndRefreshToken() {
  fetch("/api/token/refresh/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.message === "Token refreshed") {
        console.log("Token refreshed successfully.");
      } else {
        console.error("Unexpected response:", data);
      }
    })
    .catch((error) => {
      handleError(error);
    });
}

// Call checkAndRefreshToken periodically or based on user actions
setInterval(checkAndRefreshToken, 15 * 60 * 1000); // every 15 minutes
