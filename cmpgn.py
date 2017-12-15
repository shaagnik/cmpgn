from node import node
from nodeList import nodeList
from commandLine import commandLine
from canvasWindow import canvasWindow
from fileOperator import fileOperator
from randomTools import randomTools
import urwid
import sys

_list = nodeList()
_file = fileOperator()
_tools = randomTools()
print('welcome back, dm')
print('cmpgn v0.5 by shagtaw mcgraw')

if(len(sys.argv)>1):
    nodes = _file.read(sys.argv[1])
    for n in nodes:
        _list.add(n)

statusLine = urwid.Text(u'status:waiting')
div = urwid.Text(u'|') 
bg = canvasWindow(urwid.SolidFill('/'))
textEntry = commandLine('>')
footer = urwid.Columns([('weight',1,statusLine), (1, div), ('weight',1,textEntry)])
body = urwid.Frame(bg, None, footer, 'footer');
fill = urwid.LineBox(body, 'CMPGN')
loop = urwid.MainLoop(fill)



def on_input(_input):
    if(_input == 'exit'):
        loop.stop()
        exit()
    command = _input.split(' ',1)
    if(len(command) < 2):
        return
    if command[0] == 'roll':
        #roller
        statusLine.set_text(_tools.roll(command[1]))
    elif command[0] == 'mod':
        #calc mod
        statusLine.set_text(_tools.mod(command[1]))
    elif command[0].startswith('p'):
        #print
        currentNode = _list.findByName(command[1])
        if currentNode != 'not found':
            box, height, width = currentNode.getdisplay()
            bg.open_box(urwid.Filler(box),command[1],height,width)
        else:
            statusLine.set_text(command[1] + ' does not exist.')
    elif command[0].startswith('a'):
        #add
        test = _list.findByName(command[1])
        if test != 'not found':
            statusLine.set_text(command[1] + ' already exists.')
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
            statusLine.set_text(command[1] + ' does not exist.')
    elif command[0].startswith('d'):
        _file.write(_list, command[1])
    elif command[0].startswith('l'):
        newNodes = _file.read(command[1], statusLine)
        statusLine.set_text(str(len(newNodes)))
        for n in newNodes:
            statusLine.set_text(str(n))
            _list.add(n)
    elif command[0].startswith('q'):
        statusLine.set_text(str(len(_list.getlist())))
        for n in _list.getlist():
            bg.open_box(urwid.SolidFill(u'#'),n.name)
    elif command[0].startswith('!'):
        result = ''
        try:
            result = eval(command[1])
        except:
            result = 'an error occurred'
        statusLine.set_text(str(result))
urwid.connect_signal(textEntry, 'done', on_input)

loop.run()

       
