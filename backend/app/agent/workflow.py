import os
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, AIMessage
from app.agent.state import AgentState
from app.config import settings


def create_agent():
    """React Agent 생성 및 설정"""
    
    # Google API 키가 없으면 더미 Agent 반환
    if not settings.GOOGLE_API_KEY or settings.GOOGLE_API_KEY == "your_google_api_key_here" or settings.GOOGLE_API_KEY == "":
        print("⚠️ Google API 키가 설정되지 않아 더미 모드로 실행됩니다.")
        return create_dummy_agent()
    
    print("✅ Google API 키가 설정되어 실제 Gemini AI를 사용합니다.")
    
    # LangSmith 추적 설정
    if settings.LANGSMITH_API_KEY:
        os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY
        os.environ["LANGCHAIN_TRACING_V2"] = str(settings.LANGCHAIN_TRACING_V2)
        os.environ["LANGCHAIN_PROJECT"] = settings.LANGCHAIN_PROJECT
        os.environ["LANGCHAIN_ENDPOINT"] = settings.LANGCHAIN_ENDPOINT
    
    # Google API 키 설정
    if settings.GOOGLE_API_KEY:
        os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
    
        # Gemini 모델 초기화
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-05-20",
        temperature=0.1
    )
    
    # DuckDuckGo 검색 도구 설정
    search_tool = DuckDuckGoSearchRun()
    tools = [search_tool]
    
    # 간단한 Agent 함수 생성
    def simple_agent(state):
        """간단한 Agent 함수"""
        messages = state["messages"]
        last_message = messages[-1].content
        
        try:
            # Gemini 모델로 응답 생성
            response = model.invoke([HumanMessage(content=last_message)])
            return {"messages": [response]}
        except Exception as e:
            # 오류 발생 시 더미 응답
            error_response = f"AI 응답 생성 중 오류가 발생했습니다: {str(e)}"
            return {"messages": [AIMessage(content=error_response)]}
    
    # StateGraph 생성
    workflow = StateGraph(AgentState)
    
    # 노드 추가
    workflow.add_node("agent", simple_agent)
    
    # 엣지 설정
    workflow.add_edge(START, "agent")
    workflow.add_edge("agent", END)
    
    # 그래프 컴파일
    return workflow.compile()


def create_dummy_agent():
    """더미 Agent 생성 (API 키가 없을 때 사용)"""
    from langchain_core.messages import AIMessage
    
    def dummy_agent(state):
        """더미 Agent 함수"""
        messages = state["messages"]
        last_message = messages[-1].content
        
        # 간단한 응답 생성
        if "안녕" in last_message or "hello" in last_message.lower():
            response = "안녕하세요! 저는 Vibe Coding 챗봇입니다. 현재 Google API 키가 설정되지 않아 더미 모드로 작동하고 있습니다. 실제 기능을 사용하려면 Google API 키를 설정해주세요."
        elif "검색" in last_message or "search" in last_message.lower():
            response = "검색 기능을 사용하려면 Google API 키가 필요합니다. 현재는 더미 모드로 작동하고 있습니다."
        else:
            response = f"'{last_message}'에 대한 응답입니다. 현재 더미 모드로 작동하고 있습니다. 실제 AI 기능을 사용하려면 Google API 키를 설정해주세요."
        
        return {"messages": [AIMessage(content=response)]}
    
    # StateGraph 생성
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", dummy_agent)
    workflow.add_edge(START, "agent")
    workflow.add_edge("agent", END)
    
    return workflow.compile()


def should_continue(state: AgentState):
    """다음 단계 결정 함수"""
    messages = state["messages"]
    last_message = messages[-1]
    
    # 마지막 메시지에 도구 호출이 있으면 계속
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "continue"
    
    # 그렇지 않으면 종료
    return "end"
