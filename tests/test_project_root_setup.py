import os
import pytest

def test_pytest_ini_exists():
    """pytest.ini 파일이 존재하는지 확인"""
    assert os.path.exists("pytest.ini"), "pytest.ini 파일이 존재하지 않습니다"

def test_gitignore_exists():
    """gitignore 파일이 존재하는지 확인"""
    assert os.path.exists(".gitignore"), ".gitignore 파일이 존재하지 않습니다"

def test_readme_exists():
    """README.md 파일이 존재하는지 확인"""
    assert os.path.exists("README.md"), "README.md 파일이 존재하지 않습니다"

def test_pytest_ini_content():
    """pytest.ini 파일에 기본 설정이 포함되어 있는지 확인"""
    with open("pytest.ini", "r", encoding="utf-8") as f:
        content = f.read()
        assert "[tool:pytest]" in content, "pytest.ini에 [tool:pytest] 섹션이 없습니다"

def test_gitignore_content():
    """gitignore 파일에 필요한 항목들이 포함되어 있는지 확인"""
    with open(".gitignore", "r", encoding="utf-8") as f:
        content = f.read()
        required_items = ["__pycache__", ".env", "venv"]
        for item in required_items:
            assert item in content, f"{item}가 .gitignore에 포함되지 않았습니다"

def test_readme_content():
    """README.md 파일에 기본 내용이 포함되어 있는지 확인"""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        assert len(content) > 0, "README.md 파일이 비어있습니다"
