from node import node
from nodeList import nodeList
from nodeFactory import nodeFactory

class fileOperator():
    def __init__(self):
        self.fileName = 'default.cmp'
        self.factory = nodeFactory()

    def write(self, nodes, newName=''):
        if(newName != ''):
            self.fileName = newName
        with open(self.fileName, 'w') as f:
            for node in nodes.getlist():
                f.write(self.factory.serialize(node))
                f.write('\n')

    def read(self, newName='', h=None):
        if(newName != ''):
            self.fileName = newName
        with open(self.fileName) as f:
            lines = f.readlines()
        returnList = []
        for line in lines:
            if(h):
                h.set_text(line)
            returnList.append(self.factory.deserialize(line))
        return returnList
