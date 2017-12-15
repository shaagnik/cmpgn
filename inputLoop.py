from node import node
from nodeList import nodeList
from commandLine import commandLine
from canvasWindow import canvasWindow
import urwid


_list = nodeList()

print('welcome back, dm')

header = urwid.Text(u'')
 
bg = canvasWindow(urwid.SolidFill('/'))
textEntry = commandLine('>')
body = urwid.Frame(bg, header, textEntry, 'footer');
fill = urwid.LineBox(body, 'CMPGN')
loop = urwid.MainLoop(fill)



def on_input(_input):
    if(_input == 'exit'):
        loop.stop()
        exit()
    command = _input.split(' ',1)
    if(len(command) < 2):
        return
    if command[0].startswith('p'):
        #print
        currentNode = _list.findByName(command[1])
        if currentNode != 'not found':
            #currentNode.display()
            bg.open_box(urwid.SolidFill(u'-'),command[1])
            #bg = urwid.Overlay(urwid.LineBox(urwid.Text('hello')), bg, 'center', 10, 'center', 10) 
        else:
            header.set_text(command[1] + ' does not exist.')
    elif command[0].startswith('a'):
        #add
        test = _list.findByName(command[1])
        if test != 'not found':
            header.set_text(command[1] + ' already exists.')
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
            header.set_text(command[1] + ' does not exist.')

urwid.connect_signal(textEntry, 'done', on_input)

loop.run()

       
