import streamlit as st
import itertools

# MBTI 목록
mbti_list = [
    "ENFJ", "ENFP", "ENTJ", "ENTP", 
    "ESFJ", "ESFP", "ESTJ", "ESTP",
    "INFJ", "INFP", "INTJ", "INTP",
    "ISFJ", "ISFP", "ISTJ", "ISTP"
]

# 점수 계산
def calculate_score(m1, m2):
    if m1 == m2:
        return 85
    score = 0
    score += 10 if m1[0] != m2[0] else -5
    score += 10 if m1[1] != m2[1] else -5
    score += 10 if m1[2] != m2[2] else -5
    score += 10 if m1[3] != m2[3] else -5
    return max(50, min(100, 70 + score))

# 설명 생성
def generate_description(m1, m2, score):
    if m1 == m2:
        return f"✨ 둘 다 {m1} 타입이라 서로를 깊이 이해하지만, 비슷한 점이 많아 가끔은 부딪힐 수도 있어요 💞"
    elif score >= 90:
        return "💖 성격 차이가 완벽히 보완되며 강한 시너지를 냅니다. 최고의 궁합! 💍"
    elif score >= 80:
        return "💕 서로 잘 맞으며 대화와 활동에서 즐거움을 느낍니다. 함께라면 매일이 행복해요 🌈"
    elif score >= 70:
        return "💛 평범한 궁합이지만 노력한다면 특별한 관계로 발전할 수 있어요 ✨"
    else:
        return "💔 성격 차이가 커서 이해와 배려가 필요합니다. 하지만 사랑은 노력으로 완성돼요 🌱"

# 전체 궁합 데이터 생성
mbti_compatibility = {}
for a, b in itertools.product(mbti_list, repeat=2):
    score = calculate_score(a, b)
    desc = generate_description(a, b, score)
    mbti_compatibility[(a, b)] = {"score": score, "desc": desc}

# Streamlit UI
st.title("💞 MBTI 궁합 테스트 💌")

col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("🌸 당신의 이름")
    mbti1 = st.selectbox("당신의 MBTI", mbti_list)
with col2:
    name2 = st.text_input("🌟 상대방 이름")
    mbti2 = st.selectbox("상대방 MBTI", mbti_list)

if st.button("💘 궁합 보기 💘"):
    result = mbti_compatibility[(mbti1, mbti2)]
    score_emoji = "💖" if result['score'] >= 90 else "💕" if result['score'] >= 80 else "💛" if result['score'] >= 70 else "💔"
    st.subheader(f"{score_emoji} {name1} ❤️ {name2} 의 궁합 점수: {result['score']}점 {score_emoji}")
    st.write(result['desc'])
