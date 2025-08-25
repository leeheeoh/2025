import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="과일 잡기 게임", page_icon="🍎", layout="wide")

st.title("🍎 과일 잡기 게임")
st.write("좌우 화살표 키로 바구니(🧺)를 움직여 과일을 잡으세요! (돌멩이를 3번 맞으면 게임 오버❌)")

game_code = """
<canvas id="gameCanvas" 
    style="border:3px solid black; background: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1350&q=80'); 
           background-size: cover; width:100%; height:80vh;"></canvas>
<p>점수: <span id="score">0</span> | 남은 기회: <span id="lives">3</span></p>

<audio id="fruitSound" src="https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg"></audio>
<audio id="stoneSound" src="https://actions.google.com/sounds/v1/impacts/crash.ogg"></audio>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Canvas 크기
canvas.width = window.innerWidth * 0.95;
canvas.height = window.innerHeight * 0.75;

let basket = {
  x: canvas.width/2 - 100, 
  y: canvas.height - 100, 
  width: 120, 
  height: 80, 
  dx: 0,
  symbol: "🧺"
};

let items = [];
let score = 0;
let lives = 3;
let frame = 0;
let gameOver = false;

// 과일/돌멩이 이모지
const fruits = ["🍎","🍌","🍊","🍇","🍓","🍍"];
const stone = "🪨";

function drawBasket() {
  ctx.font = "80px Arial";   // 바구니 크게
  ctx.fillText(basket.symbol, basket.x, basket.y + basket.height);
}

function drawItems() {
  ctx.font = "40px Arial";
  for (let item of items) {
    ctx.fillText(item.symbol, item.x, item.y);
  }
}

function updateItems() {
  for (let item of items) {
    item.y += item.speed + Math.floor(frame / 1000);
  }
  if (frame % 40 === 0) {
    let isFruit = Math.random() < 0.7;
    let symbol = isFruit ? fruits[Math.floor(Math.random()*fruits.length)] : stone;
    items.push({
      x: Math.random() * (canvas.width - 40) + 20,
      y: 0,
      speed: 4 + Math.random() * 3,
      type: isFruit ? "fruit" : "stone",
      symbol: symbol
    });
  }
  items = items.filter(item => item.y < canvas.height + 40);
}

function checkCollision() {
  for (let item of items) {
    if (item.y >= basket.y - 20 &&
        item.x >= basket.x - 30 &&
        item.x <= basket.x + basket.width) {
      if (item.type === "fruit") {
        score += 10;
        document.getElementById("fruitSound").play();
      } else {
        lives -= 1;
        document.getElementById("stoneSound").play();
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
    ctx.fillStyle = "white";
    ctx.font = "60px Arial";
    ctx.fillText("GAME OVER", canvas.width/2 - 180, canvas.height/2);
    ctx.font = "40px Arial";
    ctx.fillText("최종 점수: " + score, canvas.width/2 - 120, canvas.height/2 + 60);
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
  if (e.code === "ArrowLeft") basket.dx = -10;
  if (e.code === "ArrowRight") basket.dx = 10;
});

document.addEventListener("keyup", function(e) {
  if (e.code === "ArrowLeft" || e.code === "ArrowRight") basket.dx = 0;
});

gameLoop();
</script>
"""

components.html(game_code, height=800)
