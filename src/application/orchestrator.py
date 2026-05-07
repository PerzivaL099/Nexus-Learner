from typing import List
from src.domain.entities import UserIntent, AgentResponse
from src.application.interfaces import CounselorAgent, ClassifierModel

class NexusOrchestrator:
    def __init__(self, classifier: ClassifierModel, agents: List[CounselorAgent]):
        self.classifier = classifier
        # Create a router dictionary for O(1) agent lookups
        self.agent_router = {agent.domain_expertise: agent for agent in agents}

    async def handle_student_request(self, raw_input: str, student_history: dict) -> str:
        # 1. Intent Classification
        intent: UserIntent = await self.classifier.classify(raw_input)
        
        # 2. Safety Escalation Check
        if intent.urgency_level >= 5 or 'crisis' in intent.detected_stressors:
            return self._trigger_emergency_protocol()

        # 3. Route to the specialized agent
        target_agent = self.agent_router.get(intent.primary_domain)
        
        if not target_agent:
            return "I'm having trouble understanding. Can you clarify what you need help with?"

        # 4. Agent Processing
        agent_response: AgentResponse = await target_agent.process_intent(intent, student_history)

        # 5. Final Synthesis (Here is where we will eventually pass the agent's 
        # raw output back to Gemma 4 for empathetic formatting)
        final_message = await self._synthesize_response(agent_response)
        return final_message

    def _trigger_emergency_protocol(self) -> str:
        # Deterministic override. No LLM generation here.
        return "This sounds urgent. Please contact the 24/7 campus support line at 555-0199 immediately."

    async def _synthesize_response(self, response: AgentResponse) -> str:
        # Placeholder for the final LLM formatting pass
        return response.student_message