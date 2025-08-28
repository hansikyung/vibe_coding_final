import os
import pytest


class TestProjectStructure:
    """프로젝트 폴더 구조 검증 테스트"""
    
    def test_backend_folder_exists(self):
        """backend 폴더가 존재하는지 확인"""
        assert os.path.exists("backend"), "backend 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend"), "backend가 폴더가 아닙니다"
    
    def test_frontend_folder_exists(self):
        """frontend 폴더가 존재하는지 확인"""
        assert os.path.exists("frontend"), "frontend 폴더가 존재하지 않습니다"
        assert os.path.isdir("frontend"), "frontend가 폴더가 아닙니다"
    
    def test_tests_folder_exists(self):
        """tests 폴더가 존재하는지 확인"""
        assert os.path.exists("tests"), "tests 폴더가 존재하지 않습니다"
        assert os.path.isdir("tests"), "tests가 폴더가 아닙니다"
    
    def test_docs_folder_exists(self):
        """docs 폴더가 존재하는지 확인"""
        assert os.path.exists("docs"), "docs 폴더가 존재하지 않습니다"
        assert os.path.isdir("docs"), "docs가 폴더가 아닙니다"
    
    def test_backend_requirements_exists(self):
        """backend/requirements.txt 파일이 존재하는지 확인"""
        assert os.path.exists("backend/requirements.txt"), "backend/requirements.txt 파일이 존재하지 않습니다"
    
    def test_frontend_requirements_exists(self):
        """frontend/requirements.txt 파일이 존재하는지 확인"""
        assert os.path.exists("frontend/requirements.txt"), "frontend/requirements.txt 파일이 존재하지 않습니다"
    
    def test_env_example_exists(self):
        """backend/env.example 파일이 존재하는지 확인"""
        assert os.path.exists("backend/env.example"), "backend/env.example 파일이 존재하지 않습니다"
    
    def test_pytest_ini_exists(self):
        """pytest.ini 파일이 존재하는지 확인"""
        assert os.path.exists("pytest.ini"), "pytest.ini 파일이 존재하지 않습니다"
    
    def test_gitignore_exists(self):
        """gitignore 파일이 존재하는지 확인"""
        assert os.path.exists(".gitignore"), ".gitignore 파일이 존재하지 않습니다"
    
    def test_readme_exists(self):
        """README.md 파일이 존재하는지 확인"""
        assert os.path.exists("README.md"), "README.md 파일이 존재하지 않습니다"

