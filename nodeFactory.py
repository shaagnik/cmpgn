import node

class nodeFactory():
    def __init__(self):
        self.numNodes = 0

    def deserialize(self, string):
        return node.node(name=string)

    def serialize(self, _node):
        c = '|'
        seq = []
        members = [attr for attr in dir(_node) if not callable(getattr(_node, attr)) and not attr.startswith('__')]
        for member in members:
            item = member + '=' + str(getattr(_node,member))
            seq.append(item)
        return c.join(seq)
