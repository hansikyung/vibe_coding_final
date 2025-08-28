from typing import Dict, Any
from langchain_core.messages import HumanMessage
from app.agent.workflow import create_agent
from app.config import settings


def invoke_agent(message: str) -> Dict[str, Any]:
    """Agent 실행 함수"""
    
    try:
        # Agent 생성
        agent = create_agent()
        
        # 메시지 생성
        messages = [HumanMessage(content=message)]
        
        # Agent 실행 (LangSmith 추적 포함)
        result = agent.invoke({"messages": messages})
        
        # 결과 반환
        return {
            "success": True,
            "response": result["messages"][-1].content,
            "messages": result["messages"],
            "langsmith_tracing": settings.LANGCHAIN_TRACING_V2 and bool(settings.LANGSMITH_API_KEY)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "response": "Agent 실행 중 오류가 발생했습니다.",
            "langsmith_tracing": settings.LANGCHAIN_TRACING_V2 and bool(settings.LANGSMITH_API_KEY)
        }
