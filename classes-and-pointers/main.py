'''
    - Classes and Pointers
'''

'''
    - Class is a blueprint or user defined data type
'''
class Cookie:
    def __init__(self, color):
        self._color = color
        
    # Getter
    @property
    def color(self):
        print('*** Getter ***')
        return self._color
    
    @color.setter
    def color(self, color):
        print('*** Setter ***')
        self._color = color
        
cookie_one = Cookie('Green')        # Green Cookie
cookie_two = Cookie('Blue')         # Blue Cookie
cookie_three = Cookie('Green')
cookie_three.color = 'Gray'

cookie_four = Cookie('bLUE')
cookie_four.color = 'Yellow'
print()

print(cookie_three.color)
print(cookie_four.color)
print()

'''
    - Pointers
'''
num1 = 11
num2 = num1

print(num1, num2)
print(id(num1), id(num2))

num2 = 22

print(num1, num2)
print(id(num1), id(num2))
print()

num1 = 11
num2 = 11

print(num1, num2)
print(id(num1), id(num2))
print()

dict1 = {
    'value': 11
}

dict2 = dict1

dict2['value'] = 101

# change the value of dict2
dict2 = {
    'value': 11
}

dict2['value'] = 100001

print(dict1, dict2)
print(id(dict1), id(dict2))
print()


'''
    - Classes
        - Class is a user defined data type
'''
class Cookie:
    def __init__(self, color):
        self._color = color
        
    @property
    def color(self):
        print(''' *** Getter *** ''')
        return self._color
    
    @color.setter
    def color(self, color):
        print(''' *** Setter *** ''')
        self._color = color
        
cookie1 = Cookie('Red')
cookie2 = Cookie('Green')
cookie3 = Cookie('Blue')

cookie1.color = 'Blue'
print(cookie1.color)
print()

cookie2.color = 'Green'
print(cookie2.color)
print()

cookie3.color = 'Red'
print(cookie3.color)
print()

'''
    - Pointers
'''
n1 = 11
n2 = n1

print(n1, n2)
print(id(n1), id(n2))
print()

n2 = 22

print(n1, n2)
print(id(n1), id(n2))
print()

d1 = {'value': 11}
d2 = d1

print(d1)
print(d2)
print(id(d1), id(d2))
print()

d2['value'] = 101

print(d1)
print(d2)
print()

d3 = {'value': 33}

d2 = d3

print(d1)
print(d2)
print(d3)
print()

d1 = d3
print(d1)
print(d2)
print(d3)

