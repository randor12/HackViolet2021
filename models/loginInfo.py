# Login Info

class LoginInfo():
    def __init__(self):
        self.id = -1
        self.email = ''
        self.password = ''
        self.username = ''
        self.salt = ''
        self.fname = ''
        self.lname = ''
        
    def set_id(self, i):
        self.id = i
        
    def get_id(self):
        return self.id    
    
    def set_email(self, e):
        self.email = e
    
    def get_email(self):
        return self.email
    
    def set_pass(self, p):
        self.password = p
    
    def get_pass(self):
        return self.password
    
    def set_user(self, u):
        self.username = u
        
    def get_user(self):
        return self.username
    
    def set_salt(self, s):
        self.salt = s
        
    def get_salt(self):
        return self.salt
    
    def set_fname(self, f):
        self.fname = f
        
    def get_fname(self):
        return self.fname
    
    def set_lname(self, l):
        self.lname = l
        
    def get_lname(self):
        return self.lname
    