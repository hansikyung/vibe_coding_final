import os
import pytest
from pydantic import ValidationError


class TestModels:
    """Pydantic 모델 테스트"""
    
    def test_models_folder_exists(self):
        """backend/app/models 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app/models"), "backend/app/models 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app/models"), "backend/app/models가 폴더가 아닙니다"
    
    def test_models_init_exists(self):
        """backend/app/models/__init__.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/models/__init__.py"), "backend/app/models/__init__.py 파일이 존재하지 않습니다"
    
    def test_chat_models_exists(self):
        """backend/app/models/chat.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/models/chat.py"), "backend/app/models/chat.py 파일이 존재하지 않습니다"
    
    def test_chat_models_importable(self):
        """chat 모델이 import 가능한지 확인"""
        try:
            from backend.app.models.chat import ChatRequest, ChatResponse
            assert ChatRequest is not None, "ChatRequest 모델이 None입니다"
            assert ChatResponse is not None, "ChatResponse 모델이 None입니다"
        except ImportError as e:
            pytest.fail(f"chat 모델 import 실패: {e}")
    
    def test_chat_request_valid_data(self):
        """ChatRequest 모델 유효한 데이터 테스트"""
        try:
            from backend.app.models.chat import ChatRequest
            
            # 유효한 데이터로 모델 생성
            data = {"message": "Hello, world!"}
            request = ChatRequest(**data)
            
            assert request.message == "Hello, world!", "메시지가 올바르게 설정되지 않았습니다"
        except ImportError as e:
            pytest.fail(f"ChatRequest 모델 테스트 실패: {e}")
    
    def test_chat_request_invalid_data(self):
        """ChatRequest 모델 잘못된 데이터 테스트"""
        try:
            from backend.app.models.chat import ChatRequest
            
            # 잘못된 데이터로 모델 생성 시도
            with pytest.raises(ValidationError):
                ChatRequest(**{"invalid": "data"})
        except ImportError as e:
            pytest.fail(f"ChatRequest 모델 잘못된 데이터 테스트 실패: {e}")
    
    def test_chat_request_empty_message(self):
        """ChatRequest 모델 빈 메시지 테스트"""
        try:
            from backend.app.models.chat import ChatRequest
            
            # 빈 메시지로 모델 생성 (빈 문자열은 허용)
            data = {"message": ""}
            request = ChatRequest(**data)
            
            assert request.message == "", "빈 메시지가 올바르게 설정되지 않았습니다"
        except ImportError as e:
            pytest.fail(f"ChatRequest 모델 빈 메시지 테스트 실패: {e}")
    
    def test_chat_response_valid_data(self):
        """ChatResponse 모델 유효한 데이터 테스트"""
        try:
            from backend.app.models.chat import ChatResponse
            
            # 유효한 데이터로 모델 생성
            data = {"response": "This is a response"}
            response = ChatResponse(**data)
            
            assert response.response == "This is a response", "응답이 올바르게 설정되지 않았습니다"
        except ImportError as e:
            pytest.fail(f"ChatResponse 모델 테스트 실패: {e}")
    
    def test_chat_response_invalid_data(self):
        """ChatResponse 모델 잘못된 데이터 테스트"""
        try:
            from backend.app.models.chat import ChatResponse
            
            # 잘못된 데이터로 모델 생성 시도
            with pytest.raises(ValidationError):
                ChatResponse(**{"invalid": "data"})
        except ImportError as e:
            pytest.fail(f"ChatResponse 모델 잘못된 데이터 테스트 실패: {e}")
    
    def test_model_serialization(self):
        """모델 직렬화 테스트"""
        try:
            from backend.app.models.chat import ChatRequest, ChatResponse
            
            # ChatRequest 생성 및 직렬화
            request = ChatRequest(message="Test message")
            request_dict = request.model_dump()
            
            assert request_dict["message"] == "Test message", "ChatRequest 직렬화 실패"
            
            # ChatResponse 생성 및 직렬화
            response = ChatResponse(response="Test response")
            response_dict = response.model_dump()
            
            assert response_dict["response"] == "Test response", "ChatResponse 직렬화 실패"
        except ImportError as e:
            pytest.fail(f"모델 직렬화 테스트 실패: {e}")
