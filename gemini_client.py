import os
import logging
from google import genai
from google.genai import types

# Gemini 클라이언트 초기화
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_acrostic_poem(word: str) -> str:
    """
    주어진 한글 단어로 N행시를 생성합니다.
    
    Args:
        word (str): N행시를 만들 한글 단어
        
    Returns:
        str: 생성된 N행시 텍스트
    """
    try:
        # 각 글자를 분리
        characters = list(word)
        
        # N행시 생성을 위한 프롬프트 작성
        system_prompt = """
        당신은 창의적인 한국어 N행시(acrostic poem) 작가입니다. 
        주어진 단어의 각 글자로 시작하는 아름답고 의미있는 문장들을 만들어주세요.
        
        규칙:
        1. 각 줄은 해당 글자를 대괄호 []로 감싸서 시작해야 합니다
        2. 각 줄은 완전한 문장이어야 합니다
        3. 전체적으로 일관된 주제나 분위기를 가져야 합니다
        4. 긍정적이고 아름다운 내용으로 작성해주세요
        5. 각 줄은 10-20글자 정도로 적당한 길이여야 합니다
        
        예시:
        단어: "사랑"
        결과:
        [사]람들 사이의 따뜻한 마음
        [랑]랑한 목소리로 불러주는 이름
        [아]름다운 추억들이 쌓여가네요
        [ㅇ]원히 함께하고 싶은 사람
        """
        
        user_prompt = f"""
        다음 단어로 N행시를 만들어주세요: "{word}"
        
        각 글자: {', '.join(characters)}
        
        위의 규칙을 따라서 {len(characters)}줄의 N행시를 작성해주세요.
        """
        
        # Gemini API 호출
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Content(
                    role="user", 
                    parts=[types.Part(text=user_prompt)]
                )
            ],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.8,  # 창의성을 위해 온도를 조금 높임
                max_output_tokens=1000
            )
        )
        
        if response.text:
            # 응답 텍스트 정리
            poem = response.text.strip()
            
            # 기본적인 정리 작업
            lines = poem.split('\n')
            cleaned_lines = []
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('결과:') and not line.startswith('단어:'):
                    cleaned_lines.append(line)
            
            return '\n'.join(cleaned_lines)
        else:
            raise ValueError("빈 응답을 받았습니다")
            
    except Exception as e:
        logging.error(f"N행시 생성 중 오류 발생: {e}")
        raise Exception(f"N행시 생성에 실패했습니다: {str(e)}")

def validate_korean_word(word: str) -> bool:
    """
    입력된 단어가 유효한 한글인지 확인합니다.
    
    Args:
        word (str): 검증할 단어
        
    Returns:
        bool: 유효한 한글이면 True, 아니면 False
    """
    if not word or not word.strip():
        return False
    
    # 한글 범위 확인 (가-힣)
    for char in word.strip():
        if not (ord('가') <= ord(char) <= ord('힣')):
            return False
    
    return True
