import os
import pytest
from typing import Dict, Any


class TestAgentStructure:
    """LangGraph Agent 기본 구조 테스트"""
    
    def test_agent_folder_exists(self):
        """backend/app/agent 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app/agent"), "backend/app/agent 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app/agent"), "backend/app/agent이 폴더가 아닙니다"
    
    def test_agent_init_exists(self):
        """backend/app/agent/__init__.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/agent/__init__.py"), "backend/app/agent/__init__.py 파일이 존재하지 않습니다"
    
    def test_agent_state_exists(self):
        """backend/app/agent/state.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/agent/state.py"), "backend/app/agent/state.py 파일이 존재하지 않습니다"
    
    def test_agent_state_importable(self):
        """AgentState가 import 가능한지 확인"""
        try:
            from backend.app.agent.state import AgentState
            assert AgentState is not None, "AgentState가 None입니다"
        except ImportError as e:
            pytest.fail(f"AgentState import 실패: {e}")
    
    def test_agent_state_structure(self):
        """AgentState 구조가 올바른지 확인"""
        try:
            from backend.app.agent.state import AgentState
            from typing import get_type_hints
            
            # AgentState가 TypedDict인지 확인
            assert hasattr(AgentState, '__annotations__'), "AgentState가 TypedDict가 아닙니다"
            
            # 필수 필드들이 있는지 확인
            annotations = get_type_hints(AgentState)
            required_fields = ['messages']
            
            for field in required_fields:
                assert field in annotations, f"AgentState에 {field} 필드가 없습니다"
                
        except ImportError as e:
            pytest.fail(f"AgentState 구조 테스트 실패: {e}")
    
    def test_agent_workflow_exists(self):
        """backend/app/agent/workflow.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/agent/workflow.py"), "backend/app/agent/workflow.py 파일이 존재하지 않습니다"
    
    def test_agent_workflow_importable(self):
        """Agent 워크플로우가 import 가능한지 확인"""
        try:
            from backend.app.agent.workflow import create_agent
            assert callable(create_agent), "create_agent가 함수가 아닙니다"
        except ImportError as e:
            pytest.fail(f"Agent 워크플로우 import 실패: {e}")
    
    def test_agent_execution_exists(self):
        """backend/app/agent/execution.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/agent/execution.py"), "backend/app/agent/execution.py 파일이 존재하지 않습니다"
    
    def test_agent_execution_importable(self):
        """Agent 실행 함수가 import 가능한지 확인"""
        try:
            from backend.app.agent.execution import invoke_agent
            assert callable(invoke_agent), "invoke_agent가 함수가 아닙니다"
        except ImportError as e:
            pytest.fail(f"Agent 실행 함수 import 실패: {e}")
    
    def test_langgraph_importable(self):
        """LangGraph가 import 가능한지 확인"""
        try:
            from langgraph.graph import StateGraph, END, START
            assert StateGraph is not None, "StateGraph가 None입니다"
            assert END is not None, "END가 None입니다"
            assert START is not None, "START가 None입니다"
        except ImportError as e:
            pytest.fail(f"LangGraph import 실패: {e}")
    
    def test_langchain_google_importable(self):
        """LangChain Google이 import 가능한지 확인"""
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            assert ChatGoogleGenerativeAI is not None, "ChatGoogleGenerativeAI가 None입니다"
        except ImportError as e:
            pytest.fail(f"LangChain Google import 실패: {e}")
    
    def test_duckduckgo_tool_importable(self):
        """DuckDuckGo Search Tool이 import 가능한지 확인"""
        try:
            from langchain_community.tools import DuckDuckGoSearchRun
            assert DuckDuckGoSearchRun is not None, "DuckDuckGoSearchRun이 None입니다"
        except ImportError as e:
            pytest.fail(f"DuckDuckGo Search Tool import 실패: {e}")
