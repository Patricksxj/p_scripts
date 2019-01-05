# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shenxianjun)s

#E_mail: shenxianjun.patrick@gmail.com

"""


dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian





class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

tk = Person('TK', 'tk@mail.com')
print(tk._email) # tk@mail.com

tk.first_name


class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email
    def update_email(self, new_email):
        self._email = new_email
    def email(self):
        return self._email

tk = Person('TK', 'tk@mail.com')
print(tk.email()) # => tk@mail.comtk._email = 'new_tk@mail.com'print(tk.email()) # => tk@mail.comtk.update_email('new_tk@mail.com')
print(tk.email()) # => new_tk@mail.com



class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age
    def show_age(self):
        return self._age

tk=Person('TK',25)

print(tk.show_age

print(tk.first_name)

print(tk._age)






class Person2:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age
    def _show_age(self):
        return self._age


tk=Person2('TK',25)

print(tk._show_age())

print(tk.first_name)

print(tk._age)




class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age
    def show_age(self):
        return self._get_age()
    def _get_age(self):
        return self._age

tk = Person('TK', 25)
print(tk.show_age()) # => 25
print(tk._get_age())



#类似继承

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

my_car = Car(4, 5, 250)
print(my_car.number_of_wheels)
print(my_car.seating_capacity)
print(my_car.maximum_velocity)

class ElectricCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)

my_electric_car=ElectricCar(4,5,250)

print(my_electric_car.number_of_wheels)
print(my_electric_car.seating_capacity)
print(my_electric_car.maximum_velocity)




class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

result=MyClass()

result.i

