import os
import sys
import pytest


class TestEnvironmentSetup:
    """환경 설정 검증 테스트"""
    
    def test_python_version(self):
        """Python 3.11 이상 버전인지 확인"""
        version = sys.version_info
        assert version.major == 3, "Python 3이 필요합니다"
        assert version.minor >= 11, "Python 3.11 이상이 필요합니다"
    
    def test_virtual_environment_active(self):
        """가상환경이 활성화되어 있는지 확인"""
        assert hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix), "가상환경이 활성화되지 않았습니다"
    
    def test_fastapi_installed(self):
        """FastAPI가 설치되어 있는지 확인"""
        try:
            import fastapi
            assert fastapi.__version__, "FastAPI가 설치되지 않았습니다"
        except ImportError:
            pytest.fail("FastAPI가 설치되지 않았습니다")
    
    def test_uvicorn_installed(self):
        """uvicorn이 설치되어 있는지 확인"""
        try:
            import uvicorn
            assert uvicorn.__version__, "uvicorn이 설치되지 않았습니다"
        except ImportError:
            pytest.fail("uvicorn이 설치되지 않았습니다")
    
    def test_pydantic_installed(self):
        """pydantic이 설치되어 있는지 확인"""
        try:
            import pydantic
            assert pydantic.__version__, "pydantic이 설치되지 않았습니다"
        except ImportError:
            pytest.fail("pydantic이 설치되지 않았습니다")
    
    def test_python_dotenv_installed(self):
        """python-dotenv가 설치되어 있는지 확인"""
        try:
            import dotenv
            # dotenv 모듈이 import되면 설치된 것으로 간주
            assert True, "python-dotenv가 정상적으로 설치되었습니다"
        except ImportError:
            pytest.fail("python-dotenv가 설치되지 않았습니다")
    
    def test_streamlit_installed(self):
        """streamlit이 설치되어 있는지 확인"""
        try:
            import streamlit
            assert streamlit.__version__, "streamlit이 설치되지 않았습니다"
        except ImportError:
            pytest.fail("streamlit이 설치되지 않았습니다")
    
    def test_requests_installed(self):
        """requests가 설치되어 있는지 확인"""
        try:
            import requests
            assert requests.__version__, "requests가 설치되지 않았습니다"
        except ImportError:
            pytest.fail("requests가 설치되지 않았습니다")
    
    def test_pytest_installed(self):
        """pytest가 설치되어 있는지 확인"""
        try:
            import pytest
            assert pytest.__version__, "pytest가 설치되지 않았습니다"
        except ImportError:
            pytest.fail("pytest가 설치되지 않았습니다")
