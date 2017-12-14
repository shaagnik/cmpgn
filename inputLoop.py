from node import node


_input = ''

n = node('whatever','whatever')
n.set('lDescription','desc')
n.display()

print('welcome back, dm')

while _input != 'exit':
    _input = raw_input('>')
    print(_input)
