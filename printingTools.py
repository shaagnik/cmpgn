
class printingTools():
    
    def printStats(self, stats):
        text = u'-------------------------------------------------------\n'
        text+= u'|  STR   |  DEX   |  CON   |  INT   |  WIS   |  CHA   |\n'
        text+= u'-------------------------------------------------------\n'
        text+= u'| '
        text+= ' | '.join(stats)
        text+= u' |\n'
        text+= u'-------------------------------------------------------\n'
        return text


