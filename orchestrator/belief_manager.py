import asyncio
from datetime import datetime

class BeliefManager:
    def __init__(self):
        self.beliefs = {}

    async def update_beliefs(self, source, data):
        self.beliefs[source] = {
            'data': data,
            'timestamp': datetime.now()
        }

    def get_belief(self, source):
        return self.beliefs.get(source, {})
