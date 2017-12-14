import urwid

class commandLine(urwid.Edit):
    _metaclass_ = urwid.signals.MetaSignals
    signals = ['done']

    def keypress(self, size, key):
        if key == 'enter':
            urwid.emit_signal(self, 'done', self)
            super(commandLine, self).set_edit_text('')
            return
        elif key == 'esc':
            super(commandLine, self).set_edit_text('')
            return
        urwid.Edit.keypress(self,size,key)

