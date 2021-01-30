"""
Holds the search data for an account
"""
class searchData():
    def __init__(self, own, addy, ran, cat):
        self.ownership = own
        self.address = addy
        self.range = ran
        self.type = cat
    
    def getOwn(self):
        return self.ownership
    
    def getAddy(self):
        return self.address
    
    def getRan(self):
        return self.range
    
    def getType(self):
        return self.type
    
    