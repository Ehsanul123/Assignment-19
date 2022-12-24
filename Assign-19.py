#Ans(1)
class Thing:
    pass
print(Thing)

example = Thing()
print(example)

#Ans(2)
class Thing2:
    letters = 'abc'
print(Thing2.letters)

#Ans(3)
class Thing3:
    def __init__(self):
        self.letters = 'xyz'
try:
    print(Thing3.letters)  # Will raise a syntax Error
except:
    my_thing = Thing3()
    print(my_thing.letters)
#Ans(4)
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
my_elements = Element('Hydrogen','H',1)

#Ans(5)
custom_dict = {'name':'Hydrogen','symbol':'H','number':1}
print(custom_dict)

hydrogen = Element(**custom_dict)
print(hydrogen.name,hydrogen.symbol,hydrogen.number, sep='\t')

#Ans(6)
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('name=%s, symbol=%s, number=%s'%(self.name, self.symbol, self.number))

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()

#Ans(7)
print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'

Hydrogen = Element('Hydrogen', 'H', 1)
print(Hydrogen)

#Ans(8)

class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def get_name(self):
        return self.__name

    @property
    def get_symbol(self):
        return self.__symbol

    @property
    def get_number(self):
        return self.__number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.get_name)
print(hydrogen.get_symbol)
print(hydrogen.get_number)

#Ans(9)
class Bear:
    def eats(self):
        print('Bear Eat : berries')

class Rabbit:
    def eats(self):
        print('Rabbit eat : clover')

class Octothorpe:
    def eats(self):
        print('Octothorpe Eat  : campers')

bear = Bear()
rabbit = Rabbit()
octothrope = Octothorpe()

bear.eats()
rabbit.eats()
octothrope.eats()

#Ans(10)
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()

    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())

Eh = Robot()
Eh.does()
