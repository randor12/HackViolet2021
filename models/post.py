class post():
    def __init__(self, msg, post):
        self.text = msg
        self.poster = post
    
    def getMsg(self):
        return self.text
    
    def getPoster(self):
        return self.poster
    