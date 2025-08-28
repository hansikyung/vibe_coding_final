from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """Agent 상태 정의"""
    
    # 메시지 리스트 (add_messages 리듀서로 처리)
    messages: Annotated[Sequence[BaseMessage], add_messages]
