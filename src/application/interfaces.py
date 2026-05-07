from abc import ABC, abstractmethod
from src.domain.entities import UserIntent, AgentResponse

class CounselorAgent(ABC):
    @property
    @abstractmethod
    def domain_expertise(self) -> str:
        pass

    @abstractmethod
    async def process_intent(self, intent: UserIntent, student_history: dict) -> AgentResponse:
        pass

class ClassifierModel(ABC):
    @abstractmethod
    async def classify(self, text: str) -> UserIntent:
        pass

