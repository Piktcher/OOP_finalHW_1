class Note:

    def __init__ (self, title = '', body = ''):
        self.title = title
        self.body = body

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body
    
    def __str__ (self):
        return self.title + "\n" + self.body