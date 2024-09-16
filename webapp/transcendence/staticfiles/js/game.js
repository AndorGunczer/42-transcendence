// document.addEventListener("DOMContentLoaded", () => {

function startSingleGame() {
  const canvas = document.getElementById("pongCanvas");
  const ctx = canvas.getContext("2d");

  canvas.width = 1200;
  canvas.height = 600;

  const paddleWidth = 10,
    paddleHeight = 75,
    ballSize = 10;
  const playerX = 10,
    aiX = canvas.width - paddleWidth - 10;
  let playerY = (canvas.height - paddleHeight) / 2,
    aiY = (canvas.height - paddleHeight) / 2;
  let ballX = canvas.width / 2,
    ballY = canvas.height / 2;
  let ballSpeedX = 7.5,
    ballSpeedY = 7.5,
    ballDirectionX = 1,
    ballDirectionY = 1;
  const paddleSpeed = 9;
  let playerScore = 0,
    aiScore = 0;
  const winningScore = 5;
  let gameRunning = false;
  let countdown = 3;
  let playerMoveUp = false,
    playerMoveDown = false;
  let lastPlayerY = playerY,
    lastAiY = aiY;

  function drawRect(x, y, width, height, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
  }

  function drawCircle(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, true);
    ctx.fill();
  }

  function drawText(text, x, y, color, fontSize) {
    ctx.fillStyle = color;
    ctx.font = `${fontSize}px Arial`;
    ctx.fillText(text, x, y);
  }

  function drawNet() {
    for (let i = 0; i < canvas.height; i += 20) {
      drawRect(canvas.width / 2 - 1, i, 2, 10, "white");
    }
  }

  function moveBall() {
    if (!gameRunning) return;

    ballX += ballSpeedX * ballDirectionX;
    ballY += ballSpeedY * ballDirectionY;

    if (ballY <= 0 || ballY >= canvas.height) {
      ballDirectionY *= -1;
    }

    if (ballX <= playerX + paddleWidth) {
      if (ballY > playerY && ballY < playerY + paddleHeight) {
        ballDirectionX *= -1;

        // Calculate reflection angle based on where the ball hit the paddle and paddle movement
        let deltaY = ballY - (playerY + paddleHeight / 2);
        ballSpeedY = deltaY * 0.3;
        if (playerMoveUp) {
          ballSpeedY -= 2; // Add a bit more speed if the paddle is moving
        } else if (playerMoveDown) {
          ballSpeedY += 2;
        }

        ballX = playerX + paddleWidth; // Move ball out of the paddle
      } else if (ballX <= 0) {
        aiScore++;
        resetBall();
      }
    }

    if (ballX >= aiX - ballSize) {
      if (ballY > aiY && ballY < aiY + paddleHeight) {
        ballDirectionX *= -1;

        // Calculate reflection angle based on where the ball hit the paddle and paddle movement
        let deltaY = ballY - (aiY + paddleHeight / 2);
        ballSpeedY = deltaY * 0.3;
        if (aiY < lastAiY) {
          ballSpeedY -= 2; // Add a bit more speed if the paddle is moving
        } else if (aiY > lastAiY) {
          ballSpeedY += 2;
        }

        ballX = aiX - ballSize; // Move ball out of the paddle
      } else if (ballX >= canvas.width) {
        playerScore++;
        resetBall();
      }
    }
  }

  function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballDirectionX = Math.random() > 0.5 ? 1 : -1;
    ballDirectionY = Math.random() > 0.5 ? 1 : -1;
    ballSpeedY = 7.5;
    gameRunning = false;
    countdown = 3;
    if (playerScore < winningScore && aiScore < winningScore) {
      countdownAnimation();
    }
  }

  function moveAI() {
    const aiCenter = aiY + paddleHeight / 2;
    if (aiCenter < ballY - 35) {
      aiY += paddleSpeed;
    } else if (aiCenter > ballY + 35) {
      aiY -= paddleSpeed;
    }
    if (aiY < 0) aiY = 0;
    if (aiY > canvas.height - paddleHeight) aiY = canvas.height - paddleHeight;
  }

  function movePlayer() {
    lastPlayerY = playerY;

    if (playerMoveUp && playerY > 0) {
      playerY -= paddleSpeed;
    }
    if (playerMoveDown && playerY < canvas.height - paddleHeight) {
      playerY += paddleSpeed;
    }
  }

  function draw() {
    drawRect(0, 0, canvas.width, canvas.height, "black");
    drawNet();
    drawRect(playerX, playerY, paddleWidth, paddleHeight, "white");
    drawRect(aiX, aiY, paddleWidth, paddleHeight, "white");
    drawCircle(ballX, ballY, ballSize, "white");
    drawText(playerScore, canvas.width / 4, 50, "white", 24);
    drawText(aiScore, (3 * canvas.width) / 4, 50, "white", 24);

    if (!gameRunning) {
      drawText(
        countdown,
        canvas.width / 2 - 20,
        canvas.height / 2 - 50,
        "white",
        50
      );
    }
  }

  function countdownAnimation() {
    if (countdown > 0) {
      setTimeout(() => {
        countdown--;
        draw();
        countdownAnimation();
      }, 1000);
    } else {
      gameRunning = true;
    }
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "w") playerMoveUp = true;
    if (event.key === "s") playerMoveDown = true;
  });

  document.addEventListener("keyup", (event) => {
    if (event.key === "w") playerMoveUp = false;
    if (event.key === "s") playerMoveDown = false;
  });

  function gameLoop() {
    if (playerScore >= winningScore || aiScore >= winningScore) {
      drawText(
        "Game Over",
        canvas.width / 2 - 100,
        canvas.height / 2,
        "white",
        50
      );
      return;
    }
    moveBall();
    moveAI();
    movePlayer();
    draw();
    lastAiY = aiY;
    requestAnimationFrame(gameLoop);
  }

  resetBall();
  countdownAnimation();
  gameLoop();
}

// function getRandomInt(max) {
//   let num = Math.floor(Math.random() * 20);

//   if (num <= 10) return num;
//   else return Math.floor(num / 2) * -1;
// }

function startLocalGame(state_json) {
  const canvas = document.getElementById("pongCanvas");
  const ctx = canvas.getContext("2d");

  canvas.width = 1200;
  canvas.height = 600;

  const paddleWidth = 10,
    paddleHeight = 75,
    ballSize = 10;
  const P1X = 10,
    P2X = canvas.width - paddleWidth - 10;
  let P1Y = (canvas.height - paddleHeight) / 2,
    P2Y = (canvas.height - paddleHeight) / 2;
  let ballX = canvas.width / 2,
    ballY = canvas.height / 2;
  let ballSpeedX = 7.5,
    ballSpeedY = 7.5,
    ballDirectionX = 1,
    ballDirectionY = 1;
  const paddleSpeed = 9;
  let P1Score = 0,
    P2Score = 0;
  const winningScore = 1;
  let gameRunning = false;
  let countdown = 3;
  let P1MoveUp = false,
    P1MoveDown = false;
  let P2MoveUp = false,
    P2MoveDown = false;
  let lastP1Y = P1Y,
    lastP2Y = P2Y;

  function drawRect(x, y, width, height, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
  }

  function drawCircle(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, true);
    ctx.fill();
  }

  function drawText(text, x, y, color, fontSize) {
    ctx.fillStyle = color;
    ctx.font = `${fontSize}px Arial`;
    ctx.fillText(text, x, y);
  }

  function drawNet() {
    for (let i = 0; i < canvas.height; i += 20) {
      drawRect(canvas.width / 2 - 1, i, 2, 10, "white");
    }
  }

  function moveBall() {
    if (!gameRunning) return;

    ballX += ballSpeedX * ballDirectionX;
    ballY += ballSpeedY * ballDirectionY;

    if (ballY <= 0 || ballY >= canvas.height) {
      ballDirectionY *= -1;
    }

    if (ballX <= P1X + paddleWidth) {
      if (ballY > P1Y && ballY < P1Y + paddleHeight) {
        ballDirectionX *= -1;

        // Calculate reflection angle based on where the ball hit the paddle and paddle movement
        let deltaY = ballY - (P1Y + paddleHeight / 2);
        ballSpeedY = deltaY * 0.3;
        if (P1MoveUp) {
          ballSpeedY -= 2; // Add a bit more speed if the paddle is moving
        } else if (P1MoveDown) {
          ballSpeedY += 2;
        }

        ballX = P1X + paddleWidth; // Move ball out of the paddle
      } else if (ballX <= 0) {
        P2Score++;
        resetBall();
      }
    }

    if (ballX >= P2X - ballSize) {
      if (ballY > P2Y && ballY < P2Y + paddleHeight) {
        ballDirectionX *= -1;

        // Calculate reflection angle based on where the ball hit the paddle and paddle movement
        let deltaY = ballY - (P2Y + paddleHeight / 2);
        ballSpeedY = deltaY * 0.3;
        if (P2MoveUp) {
          ballSpeedY -= 2; // Add a bit more speed if the paddle is moving
        } else if (P2MoveDown) {
          ballSpeedY += 2;
        }

        ballX = P2X - ballSize; // Move ball out of the paddle
      } else if (ballX >= canvas.width) {
        P1Score++;
        resetBall();
      }
    }
  }

  function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballDirectionX = Math.random() > 0.5 ? 1 : -1;
    ballDirectionY = Math.random() > 0.5 ? 1 : -1;
    ballSpeedY = 7.5;
    gameRunning = false;
    countdown = 3;
    if (P1Score < winningScore && P2Score < winningScore) {
      countdownAnimation();
    }
  }

  function moveP1() {
    lastP1Y = P1Y;

    if (P1MoveUp && P1Y > 0) {
      P1Y -= paddleSpeed;
    }
    if (P1MoveDown && P1Y < canvas.height - paddleHeight) {
      P1Y += paddleSpeed;
    }
  }

  function moveP2() {
    lastP2Y = P2Y;

    if (P2MoveUp && P2Y > 0) {
      P2Y -= paddleSpeed;
    }
    if (P2MoveDown && P1Y < canvas.height - paddleHeight) {
      P2Y += paddleSpeed;
    }
  }

  function draw() {
    drawRect(0, 0, canvas.width, canvas.height, "black");
    drawNet();
    drawRect(P1X, P1Y, paddleWidth, paddleHeight, "white");
    drawRect(P2X, P2Y, paddleWidth, paddleHeight, "white");
    drawCircle(ballX, ballY, ballSize, "white");
    drawText(P1Score, canvas.width / 4, 50, "white", 24);
    drawText(P2Score, (3 * canvas.width) / 4, 50, "white", 24);

    if (!gameRunning) {
      drawText(
        countdown,
        canvas.width / 2 - 20,
        canvas.height / 2 - 50,
        "white",
        50
      );
    }
  }

  function countdownAnimation() {
    if (countdown > 0) {
      setTimeout(() => {
        countdown--;
        draw();
        countdownAnimation();
      }, 1000);
    } else {
      gameRunning = true;
    }
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "w") P1MoveUp = true;
    if (event.key === "s") P1MoveDown = true;
    if (event.key === "i") P2MoveUp = true;
    if (event.key === "k") P2MoveDown = true;
  });

  document.addEventListener("keyup", (event) => {
    if (event.key === "w") P1MoveUp = false;
    if (event.key === "s") P1MoveDown = false;
    if (event.key === "i") P2MoveUp = false;
    if (event.key === "k") P2MoveDown = false;
  });

  function update() {
    moveBall();
    moveP1();
    moveP2();
  }

  function render() {
    draw();
    requestAnimationFrame(render);
  }

  function startGame() {
    return new Promise((resolve) => {
      function gameLoop() {
        if (P1Score >= winningScore || P2Score >= winningScore) {
          resolve(); // Game over
        } else {
          update();
          render();
          requestAnimationFrame(gameLoop);
        }
      }
      resetBall();
      render();
      gameLoop();
    });
  }

  async function runGame() {
    await startGame();

    let player1;
    let player2;
    console.log(state_json);
    let state_json_string = JSON.stringify(state_json);

    let jsonObject = JSON.parse(state_json_string);

    if (P1Score > P2Score) {
      player1 = {
        name: jsonObject.player1,
        id: jsonObject.player1_id,
        status: 'winner'
      }
      player2 = {
        name: jsonObject.player2,
        id: jsonObject.player2_id,
        status: 'loser'
      }
    } else {
      player1 = {
        name: jsonObject.player1,
        id: jsonObject.player1_id,
        status: 'loser'
      }
      player2 = {
        name: jsonObject.player2,
        id: jsonObject.player2_id,
        status: 'winner'
      }
    }

    close_local_game(player1, player2);
  }

  runGame();
}

async function close_local_game(player1, player2) {
  let url = "/close_local";

  const csrfToken = await getCsrfToken();

  fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      player1: player1,
      player2: player2,
    }),
    credentials: "include",
  }).then((response) => {
    return response.json()
  }).then((json) => {
    load_next_step(json);
  });
}

function startTournamentGame(state_json) {
  const canvas = document.getElementById("pongCanvas");
  const ctx = canvas.getContext("2d");

  canvas.width = 1200;
  canvas.height = 600;

  const paddleWidth = 10,
    paddleHeight = 75,
    ballSize = 10;
  const P1X = 10,
    P2X = canvas.width - paddleWidth - 10;
  let P1Y = (canvas.height - paddleHeight) / 2,
    P2Y = (canvas.height - paddleHeight) / 2;
  let ballX = canvas.width / 2,
    ballY = canvas.height / 2;
  let ballSpeedX = 7.5,
    ballSpeedY = 7.5,
    ballDirectionX = 1,
    ballDirectionY = 1;
  const paddleSpeed = 9;
  let P1Score = 0,
    P2Score = 0;
  const winningScore = 1;
  let gameRunning = false;
  let countdown = 3;
  let P1MoveUp = false,
    P1MoveDown = false;
  let P2MoveUp = false,
    P2MoveDown = false;
  let lastP1Y = P1Y,
    lastP2Y = P2Y;

  function drawRect(x, y, width, height, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
  }

  function drawCircle(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, true);
    ctx.fill();
  }

  function drawText(text, x, y, color, fontSize) {
    ctx.fillStyle = color;
    ctx.font = `${fontSize}px Arial`;
    ctx.fillText(text, x, y);
  }

  function drawNet() {
    for (let i = 0; i < canvas.height; i += 20) {
      drawRect(canvas.width / 2 - 1, i, 2, 10, "white");
    }
  }

  function moveBall() {
    if (!gameRunning) return;

    ballX += ballSpeedX * ballDirectionX;
    ballY += ballSpeedY * ballDirectionY;

    if (ballY <= 0 || ballY >= canvas.height) {
      ballDirectionY *= -1;
    }

    if (ballX <= P1X + paddleWidth) {
      if (ballY > P1Y && ballY < P1Y + paddleHeight) {
        ballDirectionX *= -1;

        // Calculate reflection angle based on where the ball hit the paddle and paddle movement
        let deltaY = ballY - (P1Y + paddleHeight / 2);
        ballSpeedY = deltaY * 0.3;
        if (P1MoveUp) {
          ballSpeedY -= 2; // Add a bit more speed if the paddle is moving
        } else if (P1MoveDown) {
          ballSpeedY += 2;
        }

        ballX = P1X + paddleWidth; // Move ball out of the paddle
      } else if (ballX <= 0) {
        P2Score++;
        resetBall();
      }
    }

    if (ballX >= P2X - ballSize) {
      if (ballY > P2Y && ballY < P2Y + paddleHeight) {
        ballDirectionX *= -1;

        // Calculate reflection angle based on where the ball hit the paddle and paddle movement
        let deltaY = ballY - (P2Y + paddleHeight / 2);
        ballSpeedY = deltaY * 0.3;
        if (P2MoveUp) {
          ballSpeedY -= 2; // Add a bit more speed if the paddle is moving
        } else if (P2MoveDown) {
          ballSpeedY += 2;
        }

        ballX = P2X - ballSize; // Move ball out of the paddle
      } else if (ballX >= canvas.width) {
        P1Score++;
        resetBall();
      }
    }
  }

  function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballDirectionX = Math.random() > 0.5 ? 1 : -1;
    ballDirectionY = Math.random() > 0.5 ? 1 : -1;
    ballSpeedY = 7.5;
    gameRunning = false;
    countdown = 3;
    if (P1Score < winningScore && P2Score < winningScore) {
      countdownAnimation();
    }
  }

  function moveP1() {
    lastP1Y = P1Y;

    if (P1MoveUp && P1Y > 0) {
      P1Y -= paddleSpeed;
    }
    if (P1MoveDown && P1Y < canvas.height - paddleHeight) {
      P1Y += paddleSpeed;
    }
  }

  function moveP2() {
    lastP2Y = P2Y;

    if (P2MoveUp && P2Y > 0) {
      P2Y -= paddleSpeed;
    }
    if (P2MoveDown && P1Y < canvas.height - paddleHeight) {
      P2Y += paddleSpeed;
    }
  }

  function draw() {
    drawRect(0, 0, canvas.width, canvas.height, "black");
    drawNet();
    drawRect(P1X, P1Y, paddleWidth, paddleHeight, "white");
    drawRect(P2X, P2Y, paddleWidth, paddleHeight, "white");
    drawCircle(ballX, ballY, ballSize, "white");
    drawText(P1Score, canvas.width / 4, 50, "white", 24);
    drawText(P2Score, (3 * canvas.width) / 4, 50, "white", 24);

    if (!gameRunning) {
      drawText(
        countdown,
        canvas.width / 2 - 20,
        canvas.height / 2 - 50,
        "white",
        50
      );
    }
  }

  function countdownAnimation() {
    if (countdown > 0) {
      setTimeout(() => {
        countdown--;
        draw();
        countdownAnimation();
      }, 1000);
    } else {
      gameRunning = true;
    }
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "w") P1MoveUp = true;
    if (event.key === "s") P1MoveDown = true;
    if (event.key === "i") P2MoveUp = true;
    if (event.key === "k") P2MoveDown = true;
  });

  document.addEventListener("keyup", (event) => {
    if (event.key === "w") P1MoveUp = false;
    if (event.key === "s") P1MoveDown = false;
    if (event.key === "i") P2MoveUp = false;
    if (event.key === "k") P2MoveDown = false;
  });

  function update() {
    moveBall();
    moveP1();
    moveP2();
  }

  function render() {
    draw();
    requestAnimationFrame(render);
  }

  function startGame() {
    return new Promise((resolve) => {
      function gameLoop() {
        if (P1Score >= winningScore || P2Score >= winningScore) {
          resolve(); // Game over
        } else {
          update();
          render();
          requestAnimationFrame(gameLoop);
        }
      }
      resetBall();
      render();
      gameLoop();
    });
  }

  async function runGame() {
    await startGame();

    let player1;
    let player2;
    console.log(state_json);
    let state_json_string = JSON.stringify(state_json);

    let jsonObject = JSON.parse(state_json_string);

    console.log('jsonObject contains: ' + jsonObject);
    console.log('Game ID is: ' + jsonObject.game_id);
    if (P1Score > P2Score) {
      game = {
        game_id: jsonObject.game_id,
      }
      player1 = {
        name: jsonObject.player1,
        id: jsonObject.player1_id,
        status: 'winner'
      }
      player2 = {
        name: jsonObject.player2,
        id: jsonObject.player2_id,
        status: 'loser'
      }
    } else {
      game = {
        game_id: jsonObject.game_id,
      }
      player1 = {
        name: jsonObject.player1,
        id: jsonObject.player1_id,
        status: 'loser'
      }
      player2 = {
        name: jsonObject.player2,
        id: jsonObject.player2_id,
        status: 'winner'
      }
    }

    close_tournament_game(game, player1, player2);
  }

  runGame();
}

async function close_tournament_game(gameId, player1, player2) {
  let url = "/close_tournament_game";

  const csrfToken = await getCsrfToken();

  fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      game: gameId,
      player1: player1,
      player2: player2,
    }),
    credentials: "include",
  }).then((response) => {
    return response.json()
  }).then((json) => {
    console.log('menu returned after game: ');
    console.log(json);
    load_next_step(json);
  });
}