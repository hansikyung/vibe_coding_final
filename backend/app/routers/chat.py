from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.agent.execution import invoke_agent
from app.config import settings

# APIRouter 인스턴스 생성
router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """채팅 메시지 처리 엔드포인트"""
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="메시지가 비어있습니다")
    
    # Agent 호출
    result = invoke_agent(request.message)
    
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    
    # LangSmith 추적 정보 로깅
    if result.get("langsmith_tracing"):
        print(f"✅ LangSmith 추적 활성화됨 - 프로젝트: {settings.LANGCHAIN_PROJECT}")
    
    return ChatResponse(response=result["response"]) 