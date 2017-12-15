import datetime
import urwid

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

    def getdisplay(self):
        return urwid.Text(u'none'), 10, 10

class printingTools:
    
    def printStats(self, stats):
        text = u'-------------------------------------------------------\n'
        text+= u'|  STR   |  DEX   |  CON   |  INT   |  WIS   |  CHA   |\n'
        text+= u'-------------------------------------------------------\n'
        text+= u'| '
        text+= ' | '.join(stats)
        text+= u' |\n'
        text+= u'-------------------------------------------------------\n'
        return text


class monster(node):
    
    def __init__(self):
        super(monster,self).__init__(self)
        self.stats = ['10(+0)','10(+0)','10(+0)','10(+0)','10(+0)','10(+0)']
        self.hp_roll = '5d4'
        self.nodeType = 'monster'
        self.name='SCARY MONSTER'

    def getdisplay(self):
        p = printingTools()
        text = p.printStats(self.stats)
        box = urwid.Text(text)
        return box, 57, 10
