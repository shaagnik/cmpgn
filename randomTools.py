import random

class randomTools():

    def roll(self, string):
        params = string.split('d')
        numRolls = 1
        total = 0
        if(params[0]!=''):
            try:
                numRolls = int(params[0])
            except:
                pass
        for x in range(0, numRolls):
            try:
                total += random.randint(1,int(params[1]))
            except:
                pass
        return str(total)

    def mod(self, stat):
        return str((int(stat)-10)/2)
