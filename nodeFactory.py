import node

class nodeFactory():
    def __init__(self):
        self.numNodes = 0

    def create(self, nodeType):
        if(nodeType=='monster'):
            return node.monster()
        return node.node()

    def deserialize(self, string):
        members = string.split('|')
        nodeType = 'none'
        for m in members:
            if(m.startswith('nodeType')):
                t = m.split('=')
                nodeType = t[1]
        n = self.create(nodeType)
        for m in members:
            t = m.split('=')
            n.set(t[0],t[1])
        return n

    def serialize(self, _node):
        c = '|'
        seq = []
        members = [attr for attr in dir(_node) if not callable(getattr(_node, attr)) and not attr.startswith('__')]
        for member in members:
            item = member + '=' + str(getattr(_node,member))
            seq.append(item)
        return c.join(seq)
