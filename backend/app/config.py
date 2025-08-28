import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# 환경 변수 파일 로드 (우선순위: backend/env.example > .env)
load_dotenv("backend/env.example")  # 기본 설정 파일
load_dotenv(".env")  # 실제 API 키가 있는 .env 파일 (우선순위)


class Settings(BaseSettings):
    """애플리케이션 설정"""
    
    # API 설정
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # 환경 설정
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Google API 설정
    GOOGLE_API_KEY: str = ""

    # LangSmith 설정
    LANGSMITH_API_KEY: str = ""
    LANGCHAIN_TRACING_V2: bool = True
    LANGCHAIN_PROJECT: str = "vibecoding"
    LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # 추가 필드 무시


# 설정 인스턴스 생성
settings = Settings() 