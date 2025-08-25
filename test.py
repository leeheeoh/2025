import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="과일 잡기 게임", page_icon="🍎", layout="centered")

st.title("🍎 과일 잡기 게임")
st.write("좌우 화살표 키로 바구니를 움직여 과일을 잡으세요! (돌멩이를 3번 맞으면 게임 오버❌)")

game_code = """
<canvas id="gameCanvas" width="400" height="400" 
    style="border:2px solid black; background-color: #e6f7ff"></canvas>
<p>점수: <span id="score">0</span> | 남은 기회: <span id="lives">3</span></p>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let basket = {x: 160, y: 360, width: 80, height: 20, dx: 0};
let items = [];
let score = 0;
let lives = 3;
let frame = 0;
let gameOver = false;

// 과일/돌멩이 이모지
const fruits = ["🍎","🍌","🍊","🍇"];
const stone = "🪨";

function drawBasket() {
  ctx.fillStyle = "brown";
  ctx.fillRect(basket.x, basket.y, basket.width, basket.height);
}

function drawItems() {
  ctx.font = "20px Arial";
  for (let item of items) {
    ctx.fillText(item.symbol, item.x, item.y);
  }
}

function updateItems() {
  for (let item of items) {
    item.y += item.speed;
  }
  // 아이템 추가
  if (frame % 50 === 0) {
    let isFruit = Math.random() < 0.7;
    let symbol = isFruit ? fruits[Math.floor(Math.random()*fruits.length)] : stone;
    items.push({
      x: Math.random() * (canvas.width - 20) + 10,
      y: 0,
      speed: 3 + Math.random() * 2,
      type: isFruit ? "fruit" : "stone",
      symbol: symbol
    });
  }
  // 화면 밖 제거
  items = items.filter(item => item.y < canvas.height + 20);
}

function checkCollision() {
  for (let item of items) {
    if (item.y >= basket.y - 5 &&
        item.x >= basket.x &&
        item.x <= basket.x + basket.width) {
      if (item.type === "fruit") {
        score += 10;
      } else {
        lives -= 1;
        if (lives <= 0) {
          gameOver = true;
        }
      }
      item.y = canvas.height + 100; // 사라지게
    }
  }
}

function updateBasket() {
  basket.x += basket.dx;
  if (basket.x < 0) basket.x = 0;
  if (basket.x + basket.width > canvas.width) basket.x = canvas.width - basket.width;
}

function drawScore() {
  document.getElementById("score").textContent = score;
  document.getElementById("lives").textContent = lives;
}

function gameLoop() {
  if (gameOver) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "black";
    ctx.font = "30px Arial";
    ctx.fillText("GAME OVER", 120, 180);
    ctx.font = "20px Arial";
    ctx.fillText("최종 점수: " + score, 140, 220);
    return;
  }

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  drawBasket();
  drawItems();
  updateItems();
  checkCollision();
  updateBasket();
  drawScore();

  frame++;
  requestAnimationFrame(gameLoop);
}

document.addEventListener("keydown", function(e) {
  if (e.code === "ArrowLeft") basket.dx = -5;
  if (e.code === "ArrowRight") basket.dx = 5;
});

document.addEventListener("keyup", function(e) {
  if (e.code === "ArrowLeft" || e.code === "ArrowRight") basket.dx = 0;
});

gameLoop();
</script>
"""

components.html(game_code, height=500)
