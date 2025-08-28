import pytest


class TestBasicImports:
    """기본 import 테스트"""
    
    def test_fastapi_import(self):
        """FastAPI import 테스트"""
        try:
            from fastapi import FastAPI
            app = FastAPI()
            assert app is not None, "FastAPI 인스턴스 생성 실패"
        except ImportError as e:
            pytest.fail(f"FastAPI import 실패: {e}")
    
    def test_uvicorn_import(self):
        """uvicorn import 테스트"""
        try:
            import uvicorn
            assert uvicorn is not None, "uvicorn import 실패"
        except ImportError as e:
            pytest.fail(f"uvicorn import 실패: {e}")
    
    def test_pydantic_import(self):
        """pydantic import 테스트"""
        try:
            from pydantic import BaseModel
            assert BaseModel is not None, "pydantic BaseModel import 실패"
        except ImportError as e:
            pytest.fail(f"pydantic import 실패: {e}")
    
    def test_dotenv_import(self):
        """python-dotenv import 테스트"""
        try:
            from dotenv import load_dotenv
            assert load_dotenv is not None, "dotenv load_dotenv import 실패"
        except ImportError as e:
            pytest.fail(f"python-dotenv import 실패: {e}")
    
    def test_streamlit_import(self):
        """streamlit import 테스트"""
        try:
            import streamlit as st
            assert st is not None, "streamlit import 실패"
        except ImportError as e:
            pytest.fail(f"streamlit import 실패: {e}")
    
    def test_requests_import(self):
        """requests import 테스트"""
        try:
            import requests
            assert requests is not None, "requests import 실패"
        except ImportError as e:
            pytest.fail(f"requests import 실패: {e}")
    
    def test_pytest_import(self):
        """pytest import 테스트"""
        try:
            import pytest
            assert pytest is not None, "pytest import 실패"
        except ImportError as e:
            pytest.fail(f"pytest import 실패: {e}")
    
    def test_basic_fastapi_app_creation(self):
        """기본 FastAPI 앱 생성 테스트"""
        try:
            from fastapi import FastAPI
            
            app = FastAPI(title="Test App")
            assert app.title == "Test App", "FastAPI 앱 제목 설정 실패"
            
            # 기본 라우트 추가 테스트
            @app.get("/")
            def read_root():
                return {"Hello": "World"}
            
            assert len(app.routes) > 0, "FastAPI 라우트 추가 실패"
            
        except Exception as e:
            pytest.fail(f"FastAPI 앱 생성 실패: {e}")
    
    def test_basic_pydantic_model(self):
        """기본 Pydantic 모델 테스트"""
        try:
            from pydantic import BaseModel
            
            class TestModel(BaseModel):
                name: str
                age: int
            
            # 모델 인스턴스 생성 테스트
            test_data = {"name": "Test", "age": 25}
            model = TestModel(**test_data)
            
            assert model.name == "Test", "Pydantic 모델 name 필드 실패"
            assert model.age == 25, "Pydantic 모델 age 필드 실패"
            
        except Exception as e:
            pytest.fail(f"Pydantic 모델 테스트 실패: {e}")
    
    def test_basic_streamlit_components(self):
        """기본 Streamlit 컴포넌트 테스트"""
        try:
            import streamlit as st
            
            # Streamlit 컴포넌트들이 사용 가능한지 확인
            assert hasattr(st, 'title'), "streamlit title 컴포넌트 없음"
            assert hasattr(st, 'text'), "streamlit text 컴포넌트 없음"
            assert hasattr(st, 'button'), "streamlit button 컴포넌트 없음"
            assert hasattr(st, 'text_input'), "streamlit text_input 컴포넌트 없음"
            
        except Exception as e:
            pytest.fail(f"Streamlit 컴포넌트 테스트 실패: {e}")
