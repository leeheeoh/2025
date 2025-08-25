import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="과일 잡기 게임", page_icon="🍎", layout="wide")

st.title("🍎 과일 잡기 게임")
st.write("좌우 화살표 키로 바구니(🧺)를 움직여 과일을 잡으세요! (돌멩이를 3번 맞으면 게임 오버❌)")

game_code = """
<canvas id="gameCanvas" 
    style="border:2px solid black; background-color: #e6f7ff; width:100%; height:80vh;"></canvas>
<p>점수: <span id="score">0</span> | 남은 기회: <span id="lives">3</span></p>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Canvas 크기를 화면에 맞게 자동 조정
canvas.width = window.innerWidth * 0.95;
canvas.height = window.innerHeight * 0.75;

let basket = {
  x: canvas.width/2 - 40, 
  y: canvas.height - 60, 
  width: 80, 
  height: 40, 
  dx: 0,
  symbol: "🧺"
};

let items = [];
let score = 0;
let lives = 3;
let frame = 0;
let gameOver = false;

// 과일/돌멩이 이모지
const fruits = ["🍎","🍌","🍊","🍇","🍓"];
const stone = "🪨";

function drawBasket() {
  ctx.font = "40px Arial";
  ctx.fillText(basket.symbol, basket.x, basket.y + basket.height);
}

function drawItems() {
  ctx.font = "30px Arial";
  for (let item of items) {
    ctx.fillText(item.symbol, item.x, item.y);
  }
}

function updateItems() {
  for (let item of items) {
    // 난이도 상승: 시간이 지날수록 속도 증가
    item.y += item.speed + Math.floor(frame / 1000) * 1;
  }

  if (frame % 40 === 0) { // 더 자주 등장 (난이도 ↑)
    let isFruit = Math.random() < 0.7;
    let symbol = isFruit ? fruits[Math.floor(Math.random()*fruits.length)] : stone;
    items.push({
      x: Math.random() * (canvas.width - 40) + 20,
      y: 0,
      speed: 3 + Math.random() * 2,
      type: isFruit ? "fruit" : "stone",
      symbol: symbol
    });
  }

  items = items.filter(item => item.y < canvas.height + 40);
}

function checkCollision() {
  for (let item of items) {
    if (item.y >= basket.y - 20 &&
        item.x >= basket.x - 10 &&
        item.x <= basket.x + basket.width) {
      if (item.type === "fruit") {
        score += 10;
      } else {
        lives -= 1;
        if (lives <= 0) {
          gameOver = true;
        }
      }
      item.y = canvas.height + 100; 
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
    ctx.font = "50px Arial";
    ctx.fillText("GAME OVER", canvas.width/2 - 120, canvas.height/2);
    ctx.font = "30px Arial";
    ctx.fillText("최종 점수: " + score, canvas.width/2 - 80, canvas.height/2 + 50);
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
  if (e.code === "ArrowLeft") basket.dx = -7;
  if (e.code === "ArrowRight") basket.dx = 7;
});

document.addEventListener("keyup", function(e) {
  if (e.code === "ArrowLeft" || e.code === "ArrowRight") basket.dx = 0;
});

gameLoop();
</script>
"""

components.html(game_code, height=700)
