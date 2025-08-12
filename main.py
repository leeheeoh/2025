import streamlit as st

# 간단한 MBTI 궁합 데이터 (예시)
mbti_compatibility = {
    ("ENFP", "INFJ"): {"score": 95, "desc": "서로의 장점을 잘 이해하며 보완하는 관계입니다."},
    ("INTP", "ENTJ"): {"score": 90, "desc": "목표 지향적인 관계로 서로 발전시킵니다."},
    ("ISFJ", "ESFP"): {"score": 85, "desc": "성격 차이가 매력으로 작용하여 끌립니다."},
    # 나머지 조합은 기본값 사용
}

# 기본 궁합 계산 함수
def get_compatibility(mbti1, mbti2):
    pair = (mbti1.upper(), mbti2.upper())
    reverse_pair = (mbti2.upper(), mbti1.upper())
    
    if pair in mbti_compatibility:
        return mbti_compatibility[pair]
    elif reverse_pair in mbti_compatibility:
        return mbti_compatibility[reverse_pair]
    else:
        return {"score": 70, "desc": "평범한 궁합입니다. 서로 노력하면 좋은 관계가 될 수 있어요."}

# Streamlit UI
st.title("💞 MBTI 궁합 테스트")
st.write("두 사람의 MBTI를 입력하고 궁합을 확인해보세요!")

mbti_list = [
    "ENFJ", "ENFP", "ENTJ", "ENTP", 
    "ESFJ", "ESFP", "ESTJ", "ESTP",
    "INFJ", "INFP", "INTJ", "INTP",
    "ISFJ", "ISFP", "ISTJ", "ISTP"
]

col1, col2 = st.columns(2)
with col1:
    mbti1 = st.selectbox("당신의 MBTI", mbti_list)
with col2:
    mbti2 = st.selectbox("상대방 MBTI", mbti_list)

if st.button("궁합 보기"):
    result = get_compatibility(mbti1, mbti2)
    st.subheader(f"궁합 점수: {result['score']}점")
    st.write(result['desc'])
