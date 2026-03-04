import streamlit as st
import google.generativeai as genai

# 1. API 키 설정
genai.configure(api_key="AIzaSyDppJG64YaPgolP1yQWIeNOtGQdOB-3pNA")

# 2. 가장 호환성 높은 모델 호출 방식
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="나의 AI 헬스 메이트", layout="centered")
st.title("🏋️‍♂️ 나만의 AI 운동/식단 일지")

# --- 식단 분석 ---
st.divider()
st.header("🥗 오늘 무엇을 드셨나요?")
food_input = st.text_input("음식명과 양을 적어주세요", key="food_final_fix")

if st.button("식단 분석하기"):
    if food_input:
        with st.spinner('AI 영양사가 분석 중...'):
            try:
                # 첫 번째 시도
                response = model.generate_content(f"영양사로서 분석해줘: {food_input}")
                st.info(response.text)
            except:
                try:
                    # 두 번째 시도 (안전빵 모델)
                    model_retry = genai.GenerativeModel('gemini-pro')
                    response = model_retry.generate_content(f"영양사로서 분석해줘: {food_input}")
                    st.info(response.text)
                except Exception as e:
                    st.error("구글 서버 연결이 지연되고 있습니다. 1분 뒤에 다시 시도해 주세요!")
    else:
        st.warning("음식 내용을 먼저 입력해주세요.")

# --- 운동 분석 ---
st.divider()
st.header("💪 어떤 운동을 하셨나요?")
workout_input = st.text_input("운동 종목과 세트수", key="workout_final_fix")

if st.button("칼로리 분석하기"):
    if workout_input:
        with st.spinner('AI 트레이너가 분석 중...'):
            try:
                response = model.generate_content(f"트레이너로서 분석해줘: {workout_input}")
                st.success(response.text)
            except:
                try:
                    model_retry = genai.GenerativeModel('gemini-pro')
                    response = model_retry.generate_content(f"트레이너로서 분석해줘: {workout_input}")
                    st.success(response.text)
                except Exception as e:
                    st.error("구글 서버 연결이 지연되고 있습니다.")
