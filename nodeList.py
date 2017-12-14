class nodeList():
    def __init__(self):
        self.list = []

    def findByName(self, query):
        for node in self.list:
            if node.name == query:
                return node
        return 'not found'

    def add(self, node):
        self.list.append(node)

    def remove(self, node):
        self.list.remove(node)
