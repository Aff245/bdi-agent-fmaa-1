class EdgeNode:
    def __init__(self, region, endpoint):
        self.region = region
        self.endpoint = endpoint
        self.latency = 0.0
        self.health_score = 1.0
