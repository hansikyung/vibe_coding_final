import os
import pytest

def test_frontend_requirements_exists():
    """프론트엔드 requirements.txt 파일이 존재하는지 확인"""
    assert os.path.exists("frontend/requirements.txt"), "frontend/requirements.txt 파일이 존재하지 않습니다"

def test_frontend_requirements_content():
    """프론트엔드 requirements.txt 파일에 필요한 패키지들이 포함되어 있는지 확인"""
    with open("frontend/requirements.txt", "r", encoding="utf-8") as f:
        content = f.read()
        required_packages = ["streamlit"]
        for package in required_packages:
            assert package in content, f"{package}가 requirements.txt에 포함되지 않았습니다"

