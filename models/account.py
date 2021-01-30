"""
Account details
"""
class Account():
    def __init__(self, uname, passw, email):
        self.dataArray = {}
        self.user = uname
        self.password = passw
        self.em = email
        
    # Adds a search to the search Array
    def addSearch(self, search):
        self.dataArray.append(search)
    
    # Lists all the searches an account has made
    def listSearch(self):
        for searchData in self.dataArray:
            # Print out the searchData
            pass
    
    # Lists the last few searches an account has made
    def getRecents(self, number):
        for searchData in range(number):
            # Print out the last "number" searches
            pass
    
    # Lists the last 3 searches
    def getRecents(self):
        for searchData in range(3):
            # Print out the last 3 searches
            pass
            
    
    