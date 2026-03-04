import streamlit as st
import google.generativeai as genai

# 1. 사용자님의 제미나이 API 키 설정 완료
genai.configure(api_key="AIzaSyDppJG64YaPgolP1yQWIeNOtGQdOB-3pNA")
model = genai.GenerativeModel('gemini-pro')

# 2. 웹 화면 레이아웃 설정
st.set_page_config(page_title="나의 AI 헬스 메이트", layout="centered")

st.title("🏋️‍♂️ 나만의 AI 운동/식단 일지")
st.write("오늘의 기록을 입력하면 AI가 즉시 분석해줍니다.")

# --- 식단 분석 섹션 ---
st.divider()
st.header("🥗 오늘 무엇을 드셨나요?")
food_input = st.text_input("음식명과 양을 적어주세요", placeholder="예: 사과 1개, 계란후라이 4개", key="food_key")

if st.button("식단 분석하기"):
    if food_input:
        with st.spinner('AI 영양사가 분석 중...'):
            try:
                res = model.generate_content(f"영양사로서 다음 식단의 칼로리와 탄단지를 분석해줘: {food_input}")
                st.info(res.text)
            except Exception as e:
                st.error(f"에러 발생: {e}")
    else:
        st.warning("음식을 먼저 입력해주세요.")

# --- 운동 분석 섹션 ---
st.divider()
st.header("💪 어떤 운동을 하셨나요?")
workout_input = st.text_input("운동 종목과 세트수를 적어주세요", placeholder="예: 벤치프레스 60kg 10회 3세트", key="workout_key")

if st.button("칼로리 분석하기"):
    if workout_input:
        with st.spinner('AI 트레이너가 분석 중...'):
            try:
                res = model.generate_content(f"운동 전문가로서 다음 운동의 소모 칼로리를 추정해줘: {workout_input}")
                st.success(res.text)
            except Exception as e:
                st.error(f"에러 발생: {e}")
    else:
        st.warning("운동 내용을 먼저 입력해주세요.")
