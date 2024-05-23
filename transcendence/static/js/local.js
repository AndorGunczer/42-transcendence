function startLocalGame() {
  // Get the canvas element and its 2D rendering context
  const canvas = document.getElementById("pongCanvas");
  const ctx = canvas.getContext("2d");

  // Game objects
  const paddleWidth = 10;
  const paddleHeight = 60;
  const ballSize = 10;

  // Define paddles and ball
  let leftPaddle = {
    x: 0,
    y: (canvas.height - paddleHeight) / 2,
    width: paddleWidth,
    height: paddleHeight,
    dy: 0,
  };
  let rightPaddle = {
    x: canvas.width - paddleWidth,
    y: (canvas.height - paddleHeight) / 2,
    width: paddleWidth,
    height: paddleHeight,
    dy: 0,
  };
  let ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    size: ballSize,
    dx: 2,
    dy: 2,
  };

  // Game state
  let leftPaddleUp = false;
  let leftPaddleDown = false;
  let rightPaddleUp = false;
  let rightPaddleDown = false;

  // Add event listeners for key presses
  document.addEventListener("keydown", (event) => {
    switch (event.key) {
      case "w":
        leftPaddleUp = true;
        break;
      case "s":
        leftPaddleDown = true;
        break;
      case "ArrowUp":
        rightPaddleUp = true;
        break;
      case "ArrowDown":
        rightPaddleDown = true;
        break;
    }
  });

  // Add event listeners for key releases
  document.addEventListener("keyup", (event) => {
    switch (event.key) {
      case "w":
        leftPaddleUp = false;
        console.log("W");
        break;
      case "s":
        leftPaddleDown = false;
        break;
      case "ArrowUp":
        rightPaddleUp = false;
        break;
      case "ArrowDown":
        rightPaddleDown = false;
        break;
    }
  });

  // Game loop
  function gameLoop() {
    update();
    console.log("WTF");
    draw();
    requestAnimationFrame(gameLoop);
  }

  // Update game state
  function update() {
    // Move left paddle
    if (leftPaddleUp) leftPaddle.dy = -4;
    else if (leftPaddleDown) leftPaddle.dy = 4;
    else leftPaddle.dy = 0;
    leftPaddle.y += leftPaddle.dy;

    // Move right paddle
    if (rightPaddleUp) rightPaddle.dy = -4;
    else if (rightPaddleDown) rightPaddle.dy = 4;
    else rightPaddle.dy = 0;
    rightPaddle.y += rightPaddle.dy;

    // Keep paddles within canvas
    leftPaddle.y = Math.max(
      0,
      Math.min(canvas.height - paddleHeight, leftPaddle.y)
    );
    rightPaddle.y = Math.max(
      0,
      Math.min(canvas.height - paddleHeight, rightPaddle.y)
    );

    // Move ball
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Check ball collisions with top and bottom walls
    if (ball.y <= 0 || ball.y + ball.size >= canvas.height) {
      ball.dy *= -1;
    }

    // Check ball collisions with paddles
    if (
      ball.x <= leftPaddle.x + paddleWidth &&
      ball.y >= leftPaddle.y &&
      ball.y <= leftPaddle.y + paddleHeight
    ) {
      ball.dx *= -1;
      ball.x = leftPaddle.x + paddleWidth;
    } else if (
      ball.x + ball.size >= rightPaddle.x &&
      ball.y >= rightPaddle.y &&
      ball.y <= rightPaddle.y + paddleHeight
    ) {
      ball.dx *= -1;
      ball.x = rightPaddle.x - ball.size;
    }

    // Reset ball if it goes out of bounds
    if (ball.x <= 0 || ball.x >= canvas.width) {
      ball.x = canvas.width / 2;
      ball.y = canvas.height / 2;
      ball.dx = 2;
      ball.dy = 2;
    }
  }

  // Draw game objects on canvas
  function draw() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw paddles
    ctx.fillStyle = "black";
    ctx.fillRect(leftPaddle.x, leftPaddle.y, paddleWidth, paddleHeight);
    ctx.fillRect(rightPaddle.x, rightPaddle.y, paddleWidth, paddleHeight);

    // Draw ball
    ctx.fillStyle = "black";
    ctx.fillRect(ball.x, ball.y, ball.size, ball.size);
  }

  // Start the game loop
  gameLoop();
}
