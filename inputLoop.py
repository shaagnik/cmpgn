from node import node
from nodeList import nodeList
import urwid


_list = nodeList()

print('welcome back, dm')

header = urwid.Text(u'')
 
bg = urwid.SolidFill('/')
textEntry = urwid.Edit('>')
body = urwid.Frame(bg, header, textEntry);
fill = urwid.LineBox(body, 'CMPGN')

def on_input(obj, _input):
   if  _input.endswith('\n'):
        print('hello')
        header.set_text(_input)
 
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

loop = urwid.MainLoop(fill)

urwid.connect_signal(textEntry, 'change', on_input)

loop.run()

       
