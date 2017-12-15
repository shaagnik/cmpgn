import urwid

class canvasWindow(urwid.WidgetPlaceholder):
    max_box_levels = 4
    
    def __init__(self, box):
        super(canvasWindow, self).__init__(urwid.SolidFill(u'/'))
        self.box_position=0

    def open_box(self, box, title):
        self.original_widget = urwid.Overlay(urwid.LineBox(box, title), 
                self.original_widget, 
                align='left', width=20,
                valign='top', height=20,
                min_width=8, min_height=8,
                left=(self.box_position%4)*20 + self.box_position + 1,
               # right=(self.max_box_levels - self.box_position-1)*3,
                top=(self.box_position/4) * 20 + 1)
               # bottom=(self.max_box_levels - self.box_position -1 )*2)
        self.box_position+=1
