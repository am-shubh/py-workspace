# parent class
class Parents:

    behaviour = 'good'

    def __init__(self, eyeColor: str, complexion: str):
        self.eyeColor = eyeColor
        self.complexion = complexion

    def printFeatures(self):
        print('You have {} eyes and you are {}'.format(self.eyeColor, self.complexion))


# child class
class Children(Parents):
    
    # intelligence can't be inherited.. your parents can be intelligent but you can be dumb... lol
    def __init__(self, eyeColor: str, complexion: str, intelligence: str):
        super().__init__(eyeColor, complexion)
        self.intelligence = intelligence

    # overriding parent printFeatures method
    def printFeatures(self):
        print('You have {} eyes, your behaviour is {} and you are {} and {}'.format(self.eyeColor, self.behaviour, self.complexion, self.intelligence))

    # setting child behaviour.. they can be pain in ass in future. So providing a method for that
    # if not set, will take default i.e. 'good'. I know this assumption sucks
    @classmethod
    def setBehaviour(cls, behaviour:str):
        cls.behaviour = behaviour


# parent1 = Parents('black','brown')
# parent1.printFeatures()

child1 = Children('black','white', 'dumb')
child1.setBehaviour('bad')
child1.printFeatures()