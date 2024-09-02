function startLocalGame() {
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
  const winningScore = 15;
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
    if (event.key === "PageUp") P2MoveUp = true;
    if (event.key === "PageDown") P2MoveDown = true;
  });

  document.addEventListener("keyup", (event) => {
    if (event.key === "w") P1MoveUp = false;
    if (event.key === "s") P1MoveDown = false;
    if (event.key === "PageUp") P2MoveUp = false;
    if (event.key === "PageDown") P2MoveDown = false;
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
    resetBall();
    render();
    setInterval(update, 1000 / 60); // 60 FPS
  }

  startGame();
}
