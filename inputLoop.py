from node import node
from nodeList import nodeList

_input = ''

_list = nodeList()


print('welcome back, dm')

while _input != 'exit':
    _input = raw_input('>')
    command = _input.split(' ',1)
    if command[0].startswith('p'):
        #print
        currentNode = _list.findByName(command[1])
        if currentNode != 'not found':
            currentNode.display()
        else:
            print command[1] + ' does not exist.'
    elif command[0].startswith('a'):
        #add
        test = _list.findByName(command[1])
        if test != 'not found':
            print command[1] + ' already exists.'
        else:
            params = command[1].split('|')
            _list.add(node(params[0],params[1]))
    elif command[0].startswith('s'):
        #set
        params = command[1].split('|')
        currentNode = _list.findByName(params[0])
        if currentNode != 'not found':
            currentNode.set(params[1],params[2])
        else:
            print command[1] + ' does not exist.'

        
