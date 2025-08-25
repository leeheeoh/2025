import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="장애물 피하기 게임", page_icon="🏃", layout="centered")

st.title("🏃 장애물 피하기 게임")
st.write("스페이스바를 눌러 점프해서 장애물을 피해보세요!")

# HTML + JS 코드
game_code = """
<canvas id="gameCanvas" width="600" height="200" 
    style="border:2px solid black; background-color: #f0f0f0"></canvas>
<p>점수: <span id="score">0</span></p>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let player = {x: 50, y: 150, width: 20, height: 20, dy: 0, jump: -8, gravity: 0.4, onGround: true};
let obstacles = [];
let frame = 0;
let score = 0;
let gameOver = false;

function drawPlayer() {
  ctx.fillStyle = "blue";
  ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawObstacles() {
  ctx.fillStyle = "red";
  for (let obs of obstacles) {
    ctx.fillRect(obs.x, obs.y, obs.width, obs.height);
  }
}

function updatePlayer() {
  player.y += player.dy;
  if (player.y + player.height < canvas.height) {
    player.dy += player.gravity;
    player.onGround = false;
  } else {
    player.y = canvas.height - player.height;
    player.dy = 0;
    player.onGround = true;
  }
}

function updateObstacles() {
  for (let obs of obstacles) {
    obs.x -= 4;
  }
  if (frame % 90 === 0) {
    obstacles.push({x: canvas.width, y: 170, width: 20, height: 30});
  }
  obstacles = obstacles.filter(obs => obs.x + obs.width > 0);
}

function checkCollision() {
  for (let obs of obstacles) {
    if (player.x < obs.x + obs.width &&
        player.x + player.width > obs.x &&
        player.y < obs.y + obs.height &&
        player.y + player.height > obs.y) {
      gameOver = true;
    }
  }
}

function drawScore() {
  document.getElementById("score").textContent = score;
}

function gameLoop() {
  if (gameOver) {
    ctx.fillStyle = "black";
    ctx.font = "30px Arial";
    ctx.fillText("Game Over!", 220, 100);
    return;
  }
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  drawPlayer();
  drawObstacles();

  updatePlayer();
  updateObstacles();
  checkCollision();

  if (frame % 10 === 0) score++;
  drawScore();

  frame++;
  requestAnimationFrame(gameLoop);
}

document.addEventListener("keydown", function(e) {
  if (e.code === "Space" && player.onGround) {
    player.dy = player.jump;
  }
});

gameLoop();
</script>
"""

components.html(game_code, height=300)
