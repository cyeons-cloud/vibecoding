import streamlit as st
import os
from gemini_client import generate_acrostic_poem

# 페이지 설정
st.set_page_config(
    page_title="한국어 N행시 생성기",
    page_icon="📝",
    layout="centered"
)

# 제목과 설명
st.title("📝 한국어 N행시 생성기")
st.markdown("**단어를 입력하면 AI가 창의적인 N행시를 만들어드립니다!**")

# 사용 방법 안내
with st.expander("📖 사용 방법"):
    st.markdown("""
    1. 아래 입력창에 한글 단어를 입력하세요 (2-6글자 권장)
    2. '생성하기' 버튼을 클릭하세요
    3. AI가 각 글자로 시작하는 N행시를 만들어드립니다
    
    **예시:**
    - 입력: "바다"
    - 결과: 
      - [바]람이 불어오는 해변에서
      - [다]정한 사람들과 추억을 만들어요
    """)

# API 키 확인
if not os.getenv("GEMINI_API_KEY"):
    st.error("❌ Gemini API 키가 설정되지 않았습니다. 환경 변수 'GEMINI_API_KEY'를 설정해주세요.")
    st.stop()

# 사용자 입력
user_word = st.text_input(
    "단어를 입력하세요:",
    placeholder="예: 바다, 사랑, 희망",
    max_chars=10,
    help="한글 단어를 입력해주세요 (2-6글자 권장)"
)

# 생성 버튼
if st.button("🎨 N행시 생성하기", type="primary", use_container_width=True):
    if not user_word:
        st.warning("⚠️ 단어를 입력해주세요!")
    elif not all(ord('가') <= ord(char) <= ord('힣') for char in user_word.strip()):
        st.error("❌ 한글만 입력 가능합니다!")
    elif len(user_word.strip()) < 2:
        st.error("❌ 최소 2글자 이상 입력해주세요!")
    elif len(user_word.strip()) > 6:
        st.error("❌ 6글자 이하로 입력해주세요!")
    else:
        word = user_word.strip()
        
        # 로딩 상태 표시
        with st.spinner(f"'{word}'로 N행시를 생성하고 있습니다..."):
            try:
                # N행시 생성
                poem = generate_acrostic_poem(word)
                
                if poem:
                    # 결과 표시
                    st.success("✅ N행시가 생성되었습니다!")
                    
                    # 생성된 N행시를 예쁘게 표시
                    st.markdown("### 🎭 생성된 N행시:")
                    
                    # 각 줄을 분리하여 표시
                    lines = poem.strip().split('\n')
                    for i, line in enumerate(lines):
                        if line.strip():
                            # 각 줄을 박스 형태로 표시
                            st.markdown(f"""
                            <div style="
                                background-color: #f8f9fa;
                                color: #2c3e50;
                                padding: 15px;
                                margin: 8px 0;
                                border-left: 4px solid #3498db;
                                border-radius: 8px;
                                font-size: 18px;
                                font-weight: 500;
                                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                            ">
                                {line.strip()}
                            </div>
                            """, unsafe_allow_html=True)
                    
                    # 다시 생성 버튼
                    if st.button("🔄 다시 생성하기", use_container_width=True):
                        st.rerun()
                        
                else:
                    st.error("❌ N행시 생성에 실패했습니다. 다시 시도해주세요.")
                    
            except Exception as e:
                st.error(f"❌ 오류가 발생했습니다: {str(e)}")
                st.info("💡 잠시 후 다시 시도해주세요.")

# 예시 단어들
st.markdown("---")
st.markdown("### 💡 추천 단어")

col1, col2, col3 = st.columns(3)

example_words = [
    "사랑", "희망", "친구", "가족", "꿈", "행복",
    "봄날", "여행", "커피", "독서", "음악", "자연"
]

for i, word in enumerate(example_words):
    col = [col1, col2, col3][i % 3]
    with col:
        if st.button(word, key=f"example_{word}", use_container_width=True):
            st.session_state.example_word = word
            st.rerun()

# 세션 상태에서 예시 단어가 선택된 경우 처리
if hasattr(st.session_state, 'example_word') and st.session_state.example_word:
    selected_word = st.session_state.example_word
    st.session_state.example_word = None  # 초기화
    
    with st.spinner(f"'{selected_word}'로 N행시를 생성하고 있습니다..."):
        try:
            poem = generate_acrostic_poem(selected_word)
            
            if poem:
                st.success(f"✅ '{selected_word}' N행시가 생성되었습니다!")
                
                st.markdown("### 🎭 생성된 N행시:")
                lines = poem.strip().split('\n')
                for line in lines:
                    if line.strip():
                        st.markdown(f"""
                        <div style="
                            background-color: #f8f9fa;
                            color: #2c3e50;
                            padding: 15px;
                            margin: 8px 0;
                            border-left: 4px solid #3498db;
                            border-radius: 8px;
                            font-size: 18px;
                            font-weight: 500;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        ">
                            {line.strip()}
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.error("❌ N행시 생성에 실패했습니다.")
                
        except Exception as e:
            st.error(f"❌ 오류가 발생했습니다: {str(e)}")

# 푸터
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Powered by Gemini AI | 한국어 N행시 생성기"
    "</div>", 
    unsafe_allow_html=True
)
