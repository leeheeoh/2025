import streamlit as st

# =========================
# 1) 무서운 이야기 데이터
# =========================
scary_stories = {
    "거울 속의 미소": """밤새 혼자 공부하던 나는, 창문에 비친 내 얼굴이 웃고 있는 걸 보았다.
하지만 난 웃고 있지 않았다.
눈을 돌리자 거울 속의 나는 천천히 손을 흔들었다.
방안은 적막했고, 뒤에서는 차갑게 식은 숨소리가 들렸다.
나는 움직일 수가 없었다.""",

    "찍힌 사진": """휴대폰 알람이 울려 눈을 떴다.
화면에는 "방금 찍은 사진"이라는 알림이 있었다.
열어보니 내가 자는 모습이 찍혀 있었다.
하지만 나는 혼자 살고 있다.
그리고 사진 속 내 옆에는 희미하게 웃는 얼굴이 있었다.""",

    "발자국 소리": """깊은 새벽, 발자국 소리가 내 방 앞으로 다가왔다.
현관문이 덜컥 열리는 소리가 났다.
나는 숨을 죽이고 이불을 덮었다.
하지만 곧 귓가에 속삭임이 들렸다.
"숨지 마, 다 보여." """,

    "지하 2층": """퇴근길 엘리베이터에 탔다.
1층을 눌렀는데, 버튼이 스스로 지하 2층으로 바뀌었다.
문이 열리자 불 꺼진 공간에서 누군가 서 있었다.
그 사람은 고개를 들지도 않고 내게 다가왔다.
나는 급히 닫힘 버튼을 눌렀지만, 이미 옆에서 숨소리가 들렸다.""",

    "잘 들어왔어": """친구에게 "집에 도착했어?" 하고 메시지를 보냈다.
곧 "응, 잘 들어왔어"라는 답이 왔다.
그 순간, 내 옆자리에서 그 친구가 물었다.
"누구한테 메시지 보낸 거야?"
핸드폰은 손에서 떨어졌다.""",

    "웹캠 속 그림자": """컴퓨터를 하다 뒤에서 인기척을 느꼈다.
돌아봤지만 아무도 없었다.
다시 모니터를 보니 웹캠이 켜져 있었다.
그리고 화면 속에선 내 뒤에 검은 그림자가 웃고 있었다.
나는 아직 고개를 돌리지 못했다.""",

    "막차의 승객": """지하철 막차를 탔다.
칸 안에는 나 혼자뿐이었다.
그러다 문이 닫히고, 내 맞은편 좌석에 사람이 앉아 있었다.
그는 눈도 코도 없는 얼굴로 나를 똑바로 바라보고 있었다.
그리고 서서히 다가오기 시작했다.""",

    "돌아온 인형": """어릴 적 잃어버린 인형을 다시 발견했다.
책상 위에 올려두고 잠이 들었다.
새벽에 깨어보니, 인형이 내 얼굴 바로 앞에서 웃고 있었다.
그리고 작은 목소리가 속삭였다.
"이번엔 절대 놓치지 않을 거야." """,

    "거울의 손자국": """샤워를 마치고 거울을 보니 김이 서려 있었다.
그 위에 손자국이 찍혀 있었다.
나는 혼자 사는데.
그리고 그 손자국은 점점 커지고 있었다.
내 뒤에서 물방울이 떨어지는 소리가 들렸다.""",

    "엄마의 목소리": """엄마가 불 꺼진 내 방으로 들어왔다.
"자니?" 하고 묻더니, 조용히 문을 닫고 나갔다.
잠시 뒤, 현관문 열리는 소리와 함께 엄마가 집에 들어왔다.
방금 나에게 말을 건 사람은 누구였을까?
나는 아직 이불 속에 숨어 있다."""
}

# =========================
# 2) 피 + 글씨 깜빡임 CSS / HTML (배경 검정)
# =========================
blood_css = """
<style>
[data-testid="stAppViewContainer"] {
  background: #000 !important;
  position: relative;
  overflow: hidden;
}
[data-testid="stHeader"] { background: rgba(0,0,0,0) !important; }
[data-testid="stSidebar"] { background: #000 !important; }
h1, h2, h3, h4, h5, h6, p, li, span, label {
  color: #e6e6e6 !important;
  animation: flicker 1.5s infinite;
}
@keyframes flicker {
  0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; }
  20%, 22%, 24%, 55% { opacity: 0.3; }
}
:root { --blood: #8a0000; --blood-bright: #c40000; }
#blood-overlay {
  pointer-events: none;
  position: fixed; inset: 0;
  z-index: 0;
}
#blood-overlay .pool {
  position: absolute; top: 0; left: 0; right: 0; height: 120px;
  background:
    radial-gradient(ellipse at 20% 100%, var(--blood-bright) 0%, var(--blood) 60%, rgba(0,0,0,0) 70%),
    radial-gradient(ellipse at 50% 100%, var(--blood-bright) 0%, var(--blood) 60%, rgba(0,0,0,0) 70%),
    radial-gradient(ellipse at 80% 100%, var(--blood-bright) 0%, var(--blood) 60%, rgba(0,0,0,0) 70%),
    linear-gradient(to bottom, var(--blood) 0%, var(--blood) 70%, rgba(0,0,0,0) 100%);
  filter: drop-shadow(0 8px 4px rgba(0,0,0,0.6));
}
#blood-overlay .drip {
  position: absolute; top: 80px; width: 18px; border-radius: 12px;
  background: linear-gradient(to bottom, var(--blood-bright), var(--blood));
  box-shadow: 0 4px 2px rgba(0,0,0,0.6);
  animation: drip 4.2s ease-in-out infinite;
  transform-origin: top center; opacity: 0.95;
}
#blood-overlay .drip:after {
  content: ""; position: absolute; top: -10px; left: 50%;
  width: 10px; height: 10px; transform: translateX(-50%);
  border-radius: 50%; background: var(--blood-bright);
}
@keyframes drip {
  0%   { height: 0px; opacity: 0.0; }
  10%  { height: 40px; opacity: 1; }
  40%  { height: 160px; }
  55%  { height: 200px; }
  70%  { height: 120px; }
  85%  { height: 60px;  }
  100% { height: 0px; opacity: 0.0; }
}
#blood-overlay .drip:nth-child(2)  { left: 6%;  animation-duration: 4.6s; animation-delay: 0.2s; width: 14px; }
#blood-overlay .drip:nth-child(3)  { left: 14%; animation-duration: 5.2s; animation-delay: 0.8s; width: 16px; }
#blood-overlay .drip:nth-child(4)  { left: 21%; animation-duration: 4.0s; animation-delay: 1.1s; width: 12px; }
#blood-overlay .drip:nth-child(5)  { left: 29%; animation-duration: 4.9s; animation-delay: 0.4s; width: 18px; }
#blood-overlay .drip:nth-child(6)  { left: 36%; animation-duration: 5.5s; animation-delay: 1.3s; width: 14px; }
#blood-overlay .drip:nth-child(7)  { left: 44%; animation-duration: 4.3s; animation-delay: 0.6s; width: 16px; }
#blood-overlay .drip:nth-child(8)  { left: 51%; animation-duration: 5.0s; animation-delay: 1.0s; width: 12px; }
#blood-overlay .drip:nth-child(9)  { left: 59%; animation-duration: 4.7s; animation-delay: 0.3s; width: 16px; }
#blood-overlay .drip:nth-child(10) { left: 66%; animation-duration: 5.3s; animation-delay: 1.2s; width: 14px; }
#blood-overlay .drip:nth-child(11) { left: 74%; animation-duration: 4.1s; animation-delay: 0.7s; width: 18px; }
#blood-overlay .drip:nth-child(12) { left: 81%; animation-duration: 5.6s; animation-delay: 0.5s; width: 12px; }
#blood-overlay .drip:nth-child(13) { left: 89%; animation-duration: 4.8s; animation-delay: 1.0s; width: 16px; }
.stAlert { background: rgba(20,20,20,0.65) !important; border: 1px solid #420000 !important; }
</style>
"""

blood_html = """
<div id="blood-overlay">
  <div class="pool"></div>
  <div class="drip"></div><div class="drip"></div><div class="drip"></div>
  <div class="drip"></div><div class="drip"></div><div class="drip"></div>
  <div class="drip"></div><div class="drip"></div><div class="drip"></div>
  <div class="drip"></div><div class="drip"></div><div class="drip"></div>
</div>
"""

st.markdown(blood_css + blood_html, unsafe_allow_html=True)

# =========================
# 3) UI
# =========================
st.title(" 무서운 이야기 ")
st.caption("검은 어둠 속에서, 피가 천천히 흘러내린다...")

options = ["고르시오오"] + list(scary_stories.keys())
choice = st.selectbox("이야기 제목을 선택하세요:", options)

if choice != "-- 제목을 선택하세요 --":
    st.subheader(f"📖 {choice}")
    st.error(scary_stories[choice])

# =========================
# 4) 공포 앰비언스
# =========================
st.markdown("### 🔊 공포 앰비언스")
st.audio("https://www.free-stock-music.com/downloads/spooky-ambience.mp3")
st.caption("출처: Free-Stock-Music – Spooky Ambience (Public Domain / CC0)")
