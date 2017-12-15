import datetime

class node(object):
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


class creature(node):
    
    def __init___(self):
        super(creature, self).__init__()
        self.stats = {'str':'','dex':'','con':'','int':'','wis':'','cha':''}

    def printStats(self):
        return self.stats


class monster(creature):
    
    def __init__(self):
        super(monster, self).__init__()
        self.hp_roll = '5d4'
        self.nodeType = 'monster'
        self.name='SCARY MONSTER'

