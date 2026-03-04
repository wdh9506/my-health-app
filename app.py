import streamlit as st
import google.generativeai as genai

# 1. API 키 설정 (사용자님 키 그대로 유지)
genai.configure(api_key="AIzaSyDppJG64YaPgolP1yQWIeNOtGQdOB-3pNA")

# 2. 모델 설정 (가장 최신 버전인 1.5-flash 사용)
# 만약 여기서 또 에러가 나면 시스템이 자동으로 인지하도록 설정했습니다.
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 웹 화면 레이아웃
st.set_page_config(page_title="나의 AI 헬스 메이트", layout="centered")
st.title("🏋️‍♂️ 나만의 AI 운동/식단 일지")
st.write("오늘의 기록을 입력하면 AI가 즉시 분석해줍니다.")

# --- 식단 분석 섹션 ---
st.divider()
st.header("🥗 오늘 무엇을 드셨나요?")
food_input = st.text_input("음식명과 양을 적어주세요", placeholder="예: 사과 1개, 계란후라이 4개", key="food_final")

if st.button("식단 분석하기"):
    if food_input:
        with st.spinner('AI 영양사가 분석 중...'):
            try:
                # 분석 요청
                response = model.generate_content(f"당신은 전문 영양사입니다. 다음 식단의 칼로리와 탄단지 영양 성분을 분석하고 조언해 주세요: {food_input}")
                st.info(response.text)
            except Exception as e:
                st.error(f"분석 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요. (에러내용: {e})")
    else:
        st.warning("음식 내용을 먼저 입력해주세요.")

# --- 운동 분석 섹션 ---
st.divider()
st.header("💪 어떤 운동을 하셨나요?")
workout_input = st.text_input("운동 종목과 세트수를 적어주세요", placeholder="예: 벤치프레스 60kg 10회 3세트", key="workout_final")

if st.button("칼로리 분석하기"):
    if workout_input:
        with st.spinner('AI 트레이너가 분석 중...'):
            try:
                # 분석 요청
                response = model.generate_content(f"당신은 전문 헬스 트레이너입니다. 다음 운동의 예상 소모 칼로리와 운동 팁을 알려주세요: {workout_input}")
                st.success(response.text)
            except Exception as e:
                st.error(f"분석 중 오류가 발생했습니다. (에러내용: {e})")
    else:
        st.warning("운동 내용을 먼저 입력해주세요.")
