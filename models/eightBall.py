import random
class eightBall():
    def __init__(self):
        self.quotes = {}
        
    def rand(self):
        return self.quotes[int(random.random() * len(self.quotes))]
    
        