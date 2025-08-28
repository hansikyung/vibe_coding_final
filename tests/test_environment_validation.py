import os
import pytest
from dotenv import load_dotenv


class TestEnvironmentValidation:
    """환경 변수 검증 테스트"""
    
    def test_env_example_file_content(self):
        """env.example 파일의 내용이 올바른지 확인"""
        env_file = "backend/env.example"
        assert os.path.exists(env_file), "env.example 파일이 존재하지 않습니다"
        
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 필수 환경 변수들이 포함되어 있는지 확인
        required_vars = [
            "API_HOST",
            "API_PORT", 
            "DEBUG",
            "ENVIRONMENT"
        ]
        
        for var in required_vars:
            assert var in content, f"env.example에 {var} 변수가 없습니다"
    
    def test_env_file_can_be_loaded(self):
        """env.example 파일이 dotenv로 로드 가능한지 확인"""
        env_file = "backend/env.example"
        
        # 임시로 .env 파일 생성
        temp_env_file = "backend/.env"
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            with open(temp_env_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # dotenv로 로드
            load_dotenv(temp_env_file)
            
            # 환경 변수들이 로드되었는지 확인
            assert os.getenv("API_HOST") is not None, "API_HOST 환경 변수가 로드되지 않았습니다"
            assert os.getenv("API_PORT") is not None, "API_PORT 환경 변수가 로드되지 않았습니다"
            assert os.getenv("DEBUG") is not None, "DEBUG 환경 변수가 로드되지 않았습니다"
            assert os.getenv("ENVIRONMENT") is not None, "ENVIRONMENT 환경 변수가 로드되지 않았습니다"
            
        finally:
            # 임시 파일 정리
            if os.path.exists(temp_env_file):
                os.remove(temp_env_file)
    
    def test_requirements_files_content(self):
        """requirements.txt 파일들의 내용이 올바른지 확인"""
        # 백엔드 requirements.txt 확인
        backend_req = "backend/requirements.txt"
        assert os.path.exists(backend_req), "backend/requirements.txt 파일이 존재하지 않습니다"
        
        with open(backend_req, 'r', encoding='utf-8') as f:
            backend_content = f.read()
        
        backend_packages = [
            "fastapi",
            "uvicorn", 
            "pydantic",
            "python-dotenv"
        ]
        
        for package in backend_packages:
            assert package in backend_content, f"backend/requirements.txt에 {package}가 없습니다"
        
        # 프론트엔드 requirements.txt 확인
        frontend_req = "frontend/requirements.txt"
        assert os.path.exists(frontend_req), "frontend/requirements.txt 파일이 존재하지 않습니다"
        
        with open(frontend_req, 'r', encoding='utf-8') as f:
            frontend_content = f.read()
        
        frontend_packages = [
            "streamlit",
            "requests"
        ]
        
        for package in frontend_packages:
            assert package in frontend_content, f"frontend/requirements.txt에 {package}가 없습니다"
