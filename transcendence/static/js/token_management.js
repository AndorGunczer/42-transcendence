// // Function to decode a JWT token
// function parseJwt(token) {
//   const base64Url = token.split(".")[1];
//   const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
//   const jsonPayload = decodeURIComponent(
//     atob(base64)
//       .split("")
//       .map(function (c) {
//         return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
//       })
//       .join("")
//   );

//   return JSON.parse(jsonPayload);
// }

// // Function to check if the token is about to expire
// function isTokenExpiring(token, bufferTimeInSeconds) {
//   console.log("ISTOKENEXPIRING()");
//   const tokenPayload = parseJwt(token);
//   const currentTime = Math.floor(Date.now() / 1000);
//   console.log("currentTIme: " + currentTime);
//   console.log("tokenPayload: " + tokenPayload.exp);
//   console.log(
//     "tokenPayload - currentTime: " + (tokenPayload.exp - currentTime)
//   );
//   return tokenPayload.exp - currentTime < bufferTimeInSeconds;
// }

// // Function to refresh the token
// function refreshToken() {
//   fetch("http://127.0.0.1:8000/api/token/refresh/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ refresh: localStorage.getItem("refresh_token") }),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       localStorage.setItem("access_token", data.access);
//     });
// }

// function startTokenRefreshCheck() {
//   const bufferTimeInSeconds = 300; // e.g., 5 minutes
//   const checkInterval = 60000; // Check every minute

//   setInterval(() => {
//     console.log("check for refresh");
//     const accessToken = localStorage.getItem("access_token");
//     if (isTokenExpiring(accessToken, bufferTimeInSeconds)) {
//       refreshToken();
//     }
//   }, checkInterval);
// }

// // Call this function when your app initializes
// startTokenRefreshCheck();

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
      } else {
        console.error("Unexpected response:", data);
      }
    })
    .catch((error) => {
      console.error("There was an error:", error);
    });
}

// Call checkAndRefreshToken periodically or based on user actions
setInterval(checkAndRefreshToken, 15 * 60 * 1000); // every 15 minutes
