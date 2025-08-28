#!/usr/bin/env python3
"""
.env 파일 생성 스크립트
실제 API 키를 입력하여 .env 파일을 생성합니다.
"""

import os

def create_env_file():
    """실제 API 키를 입력받아 .env 파일을 생성합니다."""
    
    print("🔧 .env 파일 생성")
    print("=" * 50)
    
    # API 키 입력 받기
    google_api_key = input("Google API 키를 입력하세요: ").strip()
    langsmith_api_key = input("LangSmith API 키를 입력하세요: ").strip()
    
    # .env 파일 내용 생성
    env_content = f"""# FastAPI 설정
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# 환경 설정
ENVIRONMENT=development

# Google API 설정
GOOGLE_API_KEY={google_api_key}

# LangSmith 설정
LANGSMITH_API_KEY={langsmith_api_key}
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=vibe_coding_agent
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
"""
    
    # .env 파일 작성
    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)
    
    print("✅ .env 파일이 생성되었습니다!")
    print("📁 파일 위치: .env")
    print("🔒 API 키가 안전하게 저장되었습니다.")
    print("\n🚀 이제 앱을 실행할 수 있습니다:")
    print("   1. 백엔드: cd backend && python run.py")
    print("   2. 프론트엔드: cd frontend && streamlit run app.py")

if __name__ == "__main__":
    create_env_file()
