import random
import streamlit as st

# 1. 웹앱 제목 및 설명 설정
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("무엇을 먹을지 고민되시나요? 아래 버튼을 눌러 오늘의 점심 메뉴를 추천받아 보세요!")

# 2. 추천할 점심 메뉴 리스트
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "비빔밥",
    "국밥",
    "쌀국수",
    "햄버거",
    "초밥",
    "파스타",
    "떡볶이",
    "마라탕",
    "칼국수"
]

# 3. 버튼 생성 및 클릭 시 동작 설정
if st.button("오늘의 메뉴 뽑기! 🎲"):
    # random.choice()를 사용하여 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(lunch_menus)
    
    # 결과 출력 및 축하 효과
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
    st.balloons()
