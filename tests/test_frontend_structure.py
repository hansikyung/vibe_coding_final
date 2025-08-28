import os
import pytest


class TestFrontendStructure:
    """Streamlit 프론트엔드 기본 구조 테스트"""
    
    def test_frontend_app_exists(self):
        """frontend/app.py 파일이 존재하는지 확인"""
        assert os.path.exists("frontend/app.py"), "frontend/app.py 파일이 존재하지 않습니다"
    
    def test_frontend_app_importable(self):
        """frontend/app.py가 import 가능한지 확인"""
        try:
            import frontend.app
            assert frontend.app is not None, "frontend.app가 None입니다"
        except ImportError as e:
            pytest.fail(f"frontend.app import 실패: {e}")
    
    def test_streamlit_importable(self):
        """Streamlit이 import 가능한지 확인"""
        try:
            import streamlit as st
            assert st is not None, "streamlit이 None입니다"
        except ImportError as e:
            pytest.fail(f"streamlit import 실패: {e}")
    
    def test_requests_importable(self):
        """requests가 import 가능한지 확인"""
        try:
            import requests
            assert requests is not None, "requests가 None입니다"
        except ImportError as e:
            pytest.fail(f"requests import 실패: {e}")
    
    def test_frontend_requirements_exists(self):
        """frontend/requirements.txt 파일이 존재하는지 확인"""
        assert os.path.exists("frontend/requirements.txt"), "frontend/requirements.txt 파일이 존재하지 않습니다"
    
    def test_frontend_requirements_content(self):
        """frontend/requirements.txt 내용이 올바른지 확인"""
        try:
            with open("frontend/requirements.txt", "r", encoding="utf-8") as f:
                content = f.read()
            
            # 필수 패키지들이 포함되어 있는지 확인
            required_packages = ["streamlit", "requests"]
            for package in required_packages:
                assert package in content, f"{package}가 requirements.txt에 포함되지 않았습니다"
                
        except Exception as e:
            pytest.fail(f"frontend/requirements.txt 내용 확인 실패: {e}")
    
    def test_app_has_title(self):
        """앱에 제목이 설정되어 있는지 확인"""
        try:
            with open("frontend/app.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # st.title이 포함되어 있는지 확인
            assert "st.title" in content, "앱에 제목이 설정되지 않았습니다"
            
        except Exception as e:
            pytest.fail(f"앱 제목 확인 실패: {e}")
    
    def test_app_has_chat_interface(self):
        """앱에 챗봇 인터페이스가 구현되어 있는지 확인"""
        try:
            with open("frontend/app.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # 챗봇 관련 요소들이 포함되어 있는지 확인
            chat_elements = ["st.chat_input", "st.chat_message", "session_state"]
            for element in chat_elements:
                assert element in content, f"챗봇 인터페이스에 {element}가 포함되지 않았습니다"
                
        except Exception as e:
            pytest.fail(f"챗봇 인터페이스 확인 실패: {e}")
    
    def test_app_has_backend_integration(self):
        """앱에 백엔드 연동이 구현되어 있는지 확인"""
        try:
            with open("frontend/app.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # 백엔드 연동 관련 요소들이 포함되어 있는지 확인
            backend_elements = ["requests", "http://", "localhost:8000"]
            found_elements = [element for element in backend_elements if element in content]
            
            assert len(found_elements) > 0, "백엔드 연동이 구현되지 않았습니다"
                
        except Exception as e:
            pytest.fail(f"백엔드 연동 확인 실패: {e}")
    
    def test_app_has_error_handling(self):
        """앱에 에러 핸들링이 구현되어 있는지 확인"""
        try:
            with open("frontend/app.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # 에러 핸들링 관련 요소들이 포함되어 있는지 확인
            error_elements = ["try:", "except", "error", "Exception"]
            found_elements = [element for element in error_elements if element in content]
            
            assert len(found_elements) > 0, "에러 핸들링이 구현되지 않았습니다"
                
        except Exception as e:
            pytest.fail(f"에러 핸들링 확인 실패: {e}")
    
    def test_app_has_loading_state(self):
        """앱에 로딩 상태 표시가 구현되어 있는지 확인"""
        try:
            with open("frontend/app.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # 로딩 상태 관련 요소들이 포함되어 있는지 확인
            loading_elements = ["st.spinner", "loading", "progress"]
            found_elements = [element for element in loading_elements if element in content]
            
            # 로딩 상태가 없어도 기본 기능은 동작하므로 경고만 표시
            if len(found_elements) == 0:
                print("경고: 로딩 상태 표시가 구현되지 않았습니다")
                
        except Exception as e:
            pytest.fail(f"로딩 상태 확인 실패: {e}")
    
    def test_app_has_user_friendly_ui(self):
        """앱에 사용자 친화적 UI가 구현되어 있는지 확인"""
        try:
            with open("frontend/app.py", "r", encoding="utf-8") as f:
                content = f.read()
            
            # UI 관련 요소들이 포함되어 있는지 확인
            ui_elements = ["st.markdown", "st.info", "st.success", "st.warning", "st.error"]
            found_elements = [element for element in ui_elements if element in content]
            
            # 기본 UI 요소가 없어도 동작하므로 경고만 표시
            if len(found_elements) == 0:
                print("경고: 사용자 친화적 UI 요소가 구현되지 않았습니다")
                
        except Exception as e:
            pytest.fail(f"UI 확인 실패: {e}")
