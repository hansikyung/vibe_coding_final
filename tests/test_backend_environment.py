import os
import pytest

def test_backend_requirements_exists():
    """백엔드 requirements.txt 파일이 존재하는지 확인"""
    assert os.path.exists("backend/requirements.txt"), "backend/requirements.txt 파일이 존재하지 않습니다"

def test_backend_env_example_exists():
    """백엔드 env.example 파일이 존재하는지 확인"""
    assert os.path.exists("backend/env.example"), "backend/env.example 파일이 존재하지 않습니다"

def test_backend_requirements_content():
    """백엔드 requirements.txt 파일에 필요한 패키지들이 포함되어 있는지 확인"""
    with open("backend/requirements.txt", "r", encoding="utf-8") as f:
        content = f.read()
        required_packages = ["fastapi", "uvicorn", "pydantic", "python-dotenv"]
        for package in required_packages:
            assert package in content, f"{package}가 requirements.txt에 포함되지 않았습니다"

def test_backend_env_example_content():
    """백엔드 env.example 파일에 필요한 환경 변수들이 포함되어 있는지 확인"""
    with open("backend/env.example", "r", encoding="utf-8") as f:
        content = f.read()
        required_vars = ["LANGSMITH_API_KEY"]
        for var in required_vars:
            assert var in content, f"{var}가 env.example에 포함되지 않았습니다"
