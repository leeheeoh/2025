import streamlit as st
import itertools

# MBTI 목록
mbti_list = [
    "ENFJ", "ENFP", "ENTJ", "ENTP", 
    "ESFJ", "ESFP", "ESTJ", "ESTP",
    "INFJ", "INFP", "INTJ", "INTP",
    "ISFJ", "ISFP", "ISTJ", "ISTP"
]

# 규칙 기반 궁합 점수 계산
def calculate_score(m1, m2):
    # 동일 유형
    if m1 == m2:
        return 85
    # 외향(E)과 내향(I) 보완
    score = 0
    score += 10 if m1[0] != m2[0] else -5
    # 직관(N)과 감각(S) 보완
    score += 10 if m1[1] != m2[1] else -5
    # 감정(F)과 사고(T) 보완
    score += 10 if m1[2] != m2[2] else -5
    # 계획(J)과 인식(P) 보완
    score += 10 if m1[3] != m2[3] else -5
    
    return max(50, min(100, 70 + score))  # 점수 범위 제한

# 설명 생성
def generate_description(m1, m2, score):
    if m1 == m2:
        return f"둘 다 {m1} 타입이라 서로를 깊이 이해하지만, 비슷한 점이 많아 가끔은 부딪힐 수 있습니다."
    elif score >= 90:
        return "성격 차이가 서로를 보완하며 강한 시너지를 냅니다."
    elif score >= 80:
        return "서로 잘 맞으며 대화와 활동에서 즐거움을 느낍니다."
    elif score >= 70:
        return "평범한 궁합입니다. 서로 노력하면 좋은 관계로 발전할 수 있습니다."
    else:
        return "성격 차이가 커서 이해가 필요합니다."
    
# 전체 궁합 데이터 생성
mbti_compatibility = {}
for a, b in itertools.product(mbti_list, repeat=2):
    score = calculate_score(a, b)
    desc = generate_description(a, b, score)
    mbti_compatibility[(a, b)] = {"score": score, "desc": desc}

# Streamlit UI
st.title("💞 MBTI 궁합 테스트 (전체 버전)")
st.write("두 사람의 MBTI를 선택하면 궁합 점수와 설명을 확인할 수 있습니다.")

col1, col2 = st.columns(2)
with col1:
    mbti1 = st.selectbox("당신의 MBTI", mbti_list)
with col2:
    mbti2 = st.selectbox("상대방 MBTI", mbti_list)

if st.button("궁합 보기"):
    result = mbti_compatibility[(mbti1, mbti2)]
    st.subheader(f"궁합 점수: {result['score']}점")
    st.write(result['desc'])
