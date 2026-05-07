from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class UserIntent:
    primary_domain: str
    urgency_level: int
    detected_stressors: List[str]
    raw_input: str

@dataclass 
class AgentResponse:
    agent_name: str
    proposed_actions: List[Dict[str, Any]]
    student_message: str
    confidence_score: float