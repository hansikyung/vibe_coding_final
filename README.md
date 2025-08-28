# Vibe Coding Project

FastAPI 백엔드와 Streamlit 프론트엔드를 사용한 챗봇 애플리케이션입니다.

## 프로젝트 구조

```
vibe_coding/
├── backend/          # FastAPI 백엔드
├── frontend/         # Streamlit 프론트엔드
├── tests/           # 테스트 파일
└── docs/            # 문서
```

## 기술 스택

### 백엔드
- FastAPI
- uvicorn
- pydantic
- python-dotenv
- LangGraph (Agent 프레임워크)
- LangChain Google (Gemini 모델)
- LangSmith (모니터링)

### 프론트엔드
- Streamlit

### AI/ML
- Gemini 2.5 Flash (Google AI)
- DuckDuckGo Search Tool
- LangSmith 추적 및 모니터링

## 설치 및 실행

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows
```

### 2. 의존성 설치
```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 3. 환경 변수 설정
```bash
# .env 파일 생성 (API 키 입력)
python setup_env.py
```

또는 수동으로 `.env` 파일을 생성:
```bash
# .env 파일 생성
GOOGLE_API_KEY=your_google_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=vibe_coding_agent
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

### 4. 백엔드 실행
```bash
cd backend
python run.py
```

### 5. 프론트엔드 실행
```bash
cd frontend
streamlit run app.py
```

## 개발

### 테스트 실행
```bash
pytest
```

## 모니터링

### LangSmith 대시보드
LangSmith를 통해 Agent 실행을 실시간으로 모니터링할 수 있습니다:

1. [LangSmith 대시보드](https://smith.langchain.com/)에 접속
2. 프로젝트: `vibe_coding_agent` 선택
3. Agent 실행 추적 및 성능 분석 확인

### 추적 정보
- Agent 실행 단계별 추적
- 도구 호출 기록
- 응답 시간 분석
- 에러 로그 확인

## GitHub Actions

이 프로젝트는 다음과 같은 GitHub Actions를 포함합니다:

### 자동화된 워크플로우
- **테스트 자동 실행**: 모든 PR에서 테스트 실행
- **코드 품질 검사**: Black, Flake8, MyPy 검사
- **보안 검사**: Bandit, Safety 검사
- **PR 자동 관리**: 코멘트, 할당, 라벨링, 리뷰 요청
- **이슈 자동 관리**: 코멘트, 할당, 라벨링

### 브랜치 보호 규칙
- `main` 브랜치 보호 활성화
- PR 리뷰 필수
- 테스트 통과 필수

## 라이선스

MIT License
