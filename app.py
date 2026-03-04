import streamlit as st
import google.generativeai as genai

# 1. API 키 설정
genai.configure(api_key="AIzaSyDppJG64YaPgolP1yQWIeNOtGQdOB-3pNA")

# 2. 에러 방지를 위해 모델 설정 방식을 변경합니다.
# 'models/gemini-1.5-flash'라고 전체 경로를 적어주면 404 에러를 피할 수 있습니다.
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

st.set_page_config(page_title="나의 AI 헬스 메이트", layout="centered")
st.title("🏋️‍♂️ 나만의 AI 운동/식단 일지")

# --- 식단 분석 ---
st.divider()
st.header("🥗 오늘 무엇을 드셨나요?")
food_input = st.text_input("음식명과 양을 적어주세요", key="food_final_v2")

if st.button("식단 분석하기"):
    if food_input:
        with st.spinner('AI 영양사가 분석 중...'):
            try:
                # 명시적으로 콘텐츠 생성 호출
                response = model.generate_content(f"영양사로서 분석해줘: {food_input}")
                st.info(response.text)
            except Exception as e:
                st.error(f"오류 발생! 모델명을 'gemini-pro'로 자동 전환해 시도합니다... (에러: {e})")
                # 예비책: flash가 안되면 pro로 즉시 재시도
                model_backup = genai.GenerativeModel(model_name="models/gemini-pro")
                response = model_backup.generate_content(food_input)
                st.info(response.text)

# --- 운동 분석 ---
st.divider()
st.header("💪 어떤 운동을 하셨나요?")
workout_input = st.text_input("운동 종목과 세트수", key="workout_final_v2")

if st.button("칼로리 분석하기"):
    if workout_input:
        with st.spinner('AI 트레이너가 분석 중...'):
            try:
                response = model.generate_content(f"트레이너로서 분석해줘: {workout_input}")
                st.success(response.text)
            except Exception as e:
                model_backup = genai.GenerativeModel(model_name="models/gemini-pro")
                response = model_backup.generate_content(workout_input)
                st.success(response.text)
