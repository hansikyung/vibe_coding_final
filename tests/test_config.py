import os
import pytest
from dotenv import load_dotenv


class TestConfig:
    """설정 및 의존성 관리 테스트"""
    
    def test_config_file_exists(self):
        """backend/app/config.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/config.py"), "backend/app/config.py 파일이 존재하지 않습니다"
    
    def test_config_importable(self):
        """config 모듈이 import 가능한지 확인"""
        try:
            from backend.app.config import settings
            assert settings is not None, "settings가 None입니다"
        except ImportError as e:
            pytest.fail(f"config import 실패: {e}")
    
    def test_environment_variables_loaded(self):
        """환경 변수가 로드되는지 확인"""
        try:
            from backend.app.config import settings
            
            # 기본 환경 변수들이 설정되어 있는지 확인
            assert hasattr(settings, 'API_HOST'), "API_HOST 설정이 없습니다"
            assert hasattr(settings, 'API_PORT'), "API_PORT 설정이 없습니다"
            assert hasattr(settings, 'DEBUG'), "DEBUG 설정이 없습니다"
            assert hasattr(settings, 'ENVIRONMENT'), "ENVIRONMENT 설정이 없습니다"
        except ImportError as e:
            pytest.fail(f"환경 변수 로드 테스트 실패: {e}")
    
    def test_default_values(self):
        """기본값들이 올바르게 설정되어 있는지 확인"""
        try:
            from backend.app.config import settings
            
            # 기본값 확인
            assert settings.API_HOST == "0.0.0.0", f"API_HOST 기본값이 올바르지 않습니다: {settings.API_HOST}"
            assert settings.API_PORT == 8000, f"API_PORT 기본값이 올바르지 않습니다: {settings.API_PORT}"
            assert settings.DEBUG is True, f"DEBUG 기본값이 올바르지 않습니다: {settings.DEBUG}"
            assert settings.ENVIRONMENT == "development", f"ENVIRONMENT 기본값이 올바르지 않습니다: {settings.ENVIRONMENT}"
        except ImportError as e:
            pytest.fail(f"기본값 테스트 실패: {e}")
    
    def test_env_file_loading(self):
        """env 파일 로딩 테스트"""
        # env.example 파일이 존재하는지 확인
        env_example_path = "backend/env.example"
        assert os.path.exists(env_example_path), "env.example 파일이 존재하지 않습니다"
        
        # env.example 파일을 로드할 수 있는지 확인
        try:
            load_dotenv(env_example_path)
            # 환경 변수가 로드되었는지 확인
            assert os.getenv("API_HOST") is not None, "API_HOST 환경 변수가 로드되지 않았습니다"
            assert os.getenv("API_PORT") is not None, "API_PORT 환경 변수가 로드되지 않았습니다"
            assert os.getenv("DEBUG") is not None, "DEBUG 환경 변수가 로드되지 않았습니다"
            assert os.getenv("ENVIRONMENT") is not None, "ENVIRONMENT 환경 변수가 로드되지 않았습니다"
        except Exception as e:
            pytest.fail(f"env 파일 로딩 실패: {e}")
    
    def test_cors_settings(self):
        """CORS 설정이 올바르게 적용되는지 확인"""
        try:
            from backend.app.main import app
            
            # CORS 미들웨어가 설정되어 있는지 확인
            middleware_found = False
            for middleware in app.user_middleware:
                if "CORSMiddleware" in str(middleware.cls):
                    middleware_found = True
                    break
            
            assert middleware_found, "CORS 미들웨어가 설정되지 않았습니다"
        except ImportError as e:
            pytest.fail(f"CORS 설정 테스트 실패: {e}")
    
    def test_app_configuration(self):
        """앱 설정이 올바르게 적용되는지 확인"""
        try:
            from backend.app.main import app
            
            # FastAPI 앱 설정 확인
            assert app.title == "Vibe Coding API", f"앱 제목이 올바르지 않습니다: {app.title}"
            assert app.version == "1.0.0", f"앱 버전이 올바르지 않습니다: {app.version}"
            assert "FastAPI 백엔드 서버" in app.description, f"앱 설명이 올바르지 않습니다: {app.description}"
        except ImportError as e:
            pytest.fail(f"앱 설정 테스트 실패: {e}")
