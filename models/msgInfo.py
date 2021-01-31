# Message Info

class MsgInfo():
    def __init__(self):
        self.mID = -1
        self.aID = -1
        self.title = ''
        self.message = ''
        self.feed = -1
        self.sentID = -1

    def set_mID(self, m):
        self.mID = m

    def get_mID(self):
        return self.mID

    def set_aID(self, a):
        self.aID = a

    def get_aID(self):
        return self.aID

    def set_title(self, t):
        self.title = t

    def get_title(self):
        return self.title

    def set_message(self, me):
        self.message = me

    def get_message(self):
        return self.message

    def set_feed(self, f):
        self.feed = f

    def get_feed(self):
        return self.feed

    def set_sentID(self, s):
        self.sentID = s

    def get_sentID(self):
        return self.sentID