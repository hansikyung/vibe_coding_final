from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

# FastAPI 인스턴스 생성
app = FastAPI(
    title="Vibe Coding API",
    description="FastAPI 백엔드 서버",
    version="1.0.0"
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 환경에서는 모든 origin 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(chat.router)

@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {"message": "Vibe Coding API Server"}

@app.get("/health")
async def health_check():
    """헬스 체크 엔드포인트"""
    return {"status": "healthy", "message": "Server is running"} 