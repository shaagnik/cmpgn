import datetime

class node():
    """represents a base node"""

    def __init__(self,nodeType,name):
        self.nodeType = nodeType
        self.name = name
        self.lDescription = ''
        self.sDescription = ''
        self.createdOn = datetime.datetime.now()

    def display(self):
        print(self.name)
        print(self.lDescription)

    def set(self,field,value):
        setattr(self, field, value)
        
