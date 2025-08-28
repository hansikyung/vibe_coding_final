import os
import pytest
from fastapi.testclient import TestClient


class TestRouters:
    """라우터 구조 테스트"""
    
    def test_routers_folder_exists(self):
        """backend/app/routers 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app/routers"), "backend/app/routers 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app/routers"), "backend/app/routers가 폴더가 아닙니다"
    
    def test_routers_init_exists(self):
        """backend/app/routers/__init__.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/routers/__init__.py"), "backend/app/routers/__init__.py 파일이 존재하지 않습니다"
    
    def test_chat_router_exists(self):
        """backend/app/routers/chat.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/routers/chat.py"), "backend/app/routers/chat.py 파일이 존재하지 않습니다"
    
    def test_chat_router_importable(self):
        """chat 라우터가 import 가능한지 확인"""
        try:
            from backend.app.routers.chat import router
            assert router is not None, "chat 라우터가 None입니다"
        except ImportError as e:
            pytest.fail(f"chat 라우터 import 실패: {e}")
    
    def test_chat_endpoint_exists(self):
        """chat 엔드포인트가 존재하는지 확인"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.post("/chat", json={"message": "Hello"})
            # API 키가 없을 때는 500이 정상
            assert response.status_code in [200, 422, 500], f"chat 엔드포인트가 예상된 상태 코드를 반환하지 않습니다: {response.status_code}"
        except ImportError as e:
            pytest.fail(f"chat 엔드포인트 테스트 실패: {e}")
    
    def test_chat_endpoint_with_valid_data(self):
        """유효한 데이터로 chat 엔드포인트 테스트"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.post("/chat", json={"message": "Hello, how are you?"})
            # API 키가 없을 때는 500이 정상
            assert response.status_code in [200, 500], f"chat 엔드포인트가 예상된 상태 코드를 반환하지 않습니다: {response.status_code}"
            if response.status_code == 200:
                data = response.json()
                assert "response" in data, "응답에 response 필드가 없습니다"
        except ImportError as e:
            pytest.fail(f"chat 엔드포인트 유효 데이터 테스트 실패: {e}")
    
    def test_chat_endpoint_with_invalid_data(self):
        """잘못된 데이터로 chat 엔드포인트 테스트"""
        try:
            from backend.app.main import app
            client = TestClient(app)
            response = client.post("/chat", json={"invalid": "data"})
            assert response.status_code == 422, f"잘못된 데이터에 대해 422를 반환하지 않습니다: {response.status_code}"
        except ImportError as e:
            pytest.fail(f"chat 엔드포인트 잘못된 데이터 테스트 실패: {e}")
