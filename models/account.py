"""
Account details
"""
class Account():
    def __init__(self, uname, passw, email, fnam, lnam):
        self.posts = {}
        self.user = uname
        self.fname = fnam
        self.lname = lnam
        self.password = passw
        self.em = email
        self.friends = {}
        
    # Adds a search to the search Array
    def addSearch(self, post):
        self.posts.append(post)
    
    # Lists all the posts an account has made
    def listPosts(self):
        for searchData in self.posts:
            # Print out the searchData
            pass
    
    # Lists the last few posts an account has made
    def getRecents(self, number):
        for searchData in range(number):
            # Print out the last "number" posts
            pass
    
    # Lists the last 3 posts
    def getRecents(self):
        for searchData in range(3):
            # Print out the last 3 posts
            pass
        
    # Lists all friends of account
    def listFriends(self):
        for friend in self.friends:
            pass
    
    