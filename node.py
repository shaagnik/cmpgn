import datetime

class node():
    """represents a base node"""

    def __init__(self,nodeType='npc',name='',serialized=''):
        self.nodeType = nodeType
        self.name = name
        self.lDescription = ''
        self.sDescription = ''
        self.createdOn = datetime.datetime.now()

    def display(self):
        print('name:',self.name)
        print('type:',self.nodeType)
        print('description:',self.lDescription)

    def set(self,field,value):
        setattr(self, field, value)
