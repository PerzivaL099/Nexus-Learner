class UserIntent:
    def __init__(self, domains, urgency, sentiment):
        self.domains = domains
        self.urgency = urgency
        self.sentiment = sentiment


class AgentResponse:
    def __init__(self, agent_name, payload, requirements_met):
        self.agent_name = agent_name
        self.payload = payload
        self.requirements_met = requirements_met
        