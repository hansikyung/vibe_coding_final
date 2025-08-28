import os
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestFastAPIStructure:
    """FastAPI 기본 구조 테스트"""
    
    def test_app_folder_exists(self):
        """backend/app 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app"), "backend/app 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app"), "backend/app이 폴더가 아닙니다"
    
    def test_app_init_exists(self):
        """backend/app/__init__.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/__init__.py"), "backend/app/__init__.py 파일이 존재하지 않습니다"
    
    def test_main_py_exists(self):
        """backend/app/main.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/main.py"), "backend/app/main.py 파일이 존재하지 않습니다"
    
    def test_main_py_importable(self):
        """main.py가 import 가능한지 확인"""
        try:
            from backend.app.main import app
            assert isinstance(app, FastAPI), "app이 FastAPI 인스턴스가 아닙니다"
        except ImportError as e:
            pytest.fail(f"main.py import 실패: {e}")
    
    def test_fastapi_app_creation(self):
        """FastAPI 앱이 올바르게 생성되는지 확인"""
        try:
            from backend.app.main import app
            assert app.title is not None, "FastAPI 앱 제목이 설정되지 않았습니다"
            assert app.version is not None, "FastAPI 앱 버전이 설정되지 않았습니다"
        except ImportError as e:
            pytest.fail(f"FastAPI 앱 생성 실패: {e}")
    
    def test_root_endpoint_exists(self):
        """루트 엔드포인트가 존재하는지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.get("/")
            assert response.status_code == 200, "루트 엔드포인트가 200을 반환하지 않습니다"
        except ImportError as e:
            pytest.fail(f"루트 엔드포인트 테스트 실패: {e}")
    
    def test_health_endpoint_exists(self):
        """헬스 체크 엔드포인트가 존재하는지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.get("/health")
            assert response.status_code == 200, "헬스 체크 엔드포인트가 200을 반환하지 않습니다"
            assert "status" in response.json(), "헬스 체크 응답에 status가 없습니다"
        except ImportError as e:
            pytest.fail(f"헬스 체크 엔드포인트 테스트 실패: {e}")
    
    def test_openapi_docs_accessible(self):
        """OpenAPI 문서가 접근 가능한지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.get("/docs")
            assert response.status_code == 200, "OpenAPI 문서가 200을 반환하지 않습니다"
        except ImportError as e:
            pytest.fail(f"OpenAPI 문서 테스트 실패: {e}")
    
    def test_openapi_json_accessible(self):
        """OpenAPI JSON이 접근 가능한지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.get("/openapi.json")
            assert response.status_code == 200, "OpenAPI JSON이 200을 반환하지 않습니다"
            assert "openapi" in response.json(), "OpenAPI JSON에 openapi 필드가 없습니다"
        except ImportError as e:
            pytest.fail(f"OpenAPI JSON 테스트 실패: {e}")
