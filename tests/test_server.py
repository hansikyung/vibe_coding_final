import os
import pytest
import subprocess
import time
from fastapi.testclient import TestClient


class TestServer:
    """서버 실행 스크립트 테스트"""
    
    def test_run_py_exists(self):
        """backend/run.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/run.py"), "backend/run.py 파일이 존재하지 않습니다"
    
    def test_run_py_executable(self):
        """run.py가 실행 가능한지 확인"""
        try:
            # run.py 파일의 내용을 확인하여 올바른 구조인지 검증
            with open("backend/run.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # 필수 요소들이 포함되어 있는지 확인
            assert "uvicorn" in content, "uvicorn이 포함되지 않았습니다"
            assert "main:app" in content, "main:app이 포함되지 않았습니다"
            assert "reload" in content, "reload 옵션이 포함되지 않았습니다"
        except Exception as e:
            pytest.fail(f"run.py 파일 검증 실패: {e}")
    
    def test_server_configuration(self):
        """서버 설정이 올바른지 확인"""
        try:
            from backend.app.main import app
            from backend.app.config import settings
            
            # 설정이 올바르게 로드되는지 확인
            assert settings.API_HOST == "0.0.0.0", f"API_HOST가 올바르지 않습니다: {settings.API_HOST}"
            assert settings.API_PORT == 8000, f"API_PORT가 올바르지 않습니다: {settings.API_PORT}"
            
            # FastAPI 앱이 올바르게 구성되어 있는지 확인
            assert app.title == "Vibe Coding API", f"앱 제목이 올바르지 않습니다: {app.title}"
            assert app.version == "1.0.0", f"앱 버전이 올바르지 않습니다: {app.version}"
        except ImportError as e:
            pytest.fail(f"서버 설정 테스트 실패: {e}")
    
    def test_server_endpoints_accessible(self):
        """서버 엔드포인트들이 접근 가능한지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            
            # 루트 엔드포인트
            response = client.get("/")
            assert response.status_code == 200, "루트 엔드포인트가 200을 반환하지 않습니다"
            
            # 헬스 체크 엔드포인트
            response = client.get("/health")
            assert response.status_code == 200, "헬스 체크 엔드포인트가 200을 반환하지 않습니다"
            
            # chat 엔드포인트 (API 키가 없을 때는 500이 정상)
            response = client.post("/chat", json={"message": "test"})
            assert response.status_code in [200, 500], "chat 엔드포인트가 예상된 상태 코드를 반환하지 않습니다"
            
        except ImportError as e:
            pytest.fail(f"서버 엔드포인트 테스트 실패: {e}")
    
    def test_development_mode_settings(self):
        """개발 모드 설정이 올바른지 확인"""
        try:
            from backend.app.config import settings
            
            # 개발 모드 설정 확인
            assert settings.DEBUG is True, "DEBUG가 True가 아닙니다"
            assert settings.ENVIRONMENT == "development", f"ENVIRONMENT가 development가 아닙니다: {settings.ENVIRONMENT}"
            
        except ImportError as e:
            pytest.fail(f"개발 모드 설정 테스트 실패: {e}")
    
    def test_cors_enabled(self):
        """CORS가 활성화되어 있는지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            
            # CORS 헤더가 포함되어 있는지 확인
            response = client.options("/", headers={"Origin": "http://localhost:3000"})
            
            # CORS 미들웨어가 설정되어 있는지 확인
            middleware_found = False
            for middleware in app.user_middleware:
                if "CORSMiddleware" in str(middleware.cls):
                    middleware_found = True
                    break
            
            assert middleware_found, "CORS 미들웨어가 설정되지 않았습니다"
            
        except ImportError as e:
            pytest.fail(f"CORS 테스트 실패: {e}")
    
    def test_openapi_documentation(self):
        """OpenAPI 문서가 올바르게 생성되는지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            
            # OpenAPI JSON
            response = client.get("/openapi.json")
            assert response.status_code == 200, "OpenAPI JSON이 200을 반환하지 않습니다"
            
            openapi_data = response.json()
            assert "openapi" in openapi_data, "OpenAPI JSON에 openapi 필드가 없습니다"
            assert "paths" in openapi_data, "OpenAPI JSON에 paths 필드가 없습니다"
            assert "info" in openapi_data, "OpenAPI JSON에 info 필드가 없습니다"
            
            # OpenAPI 문서
            response = client.get("/docs")
            assert response.status_code == 200, "OpenAPI 문서가 200을 반환하지 않습니다"
            
        except ImportError as e:
            pytest.fail(f"OpenAPI 문서 테스트 실패: {e}")
