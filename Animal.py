import random
import sys
import os
class Animal:
    __name = ""
    __height = 0



    def set_name(self, name) :
        self.__name = name
    def get_name(self):
        return self.__name

    def set_height(self, height) :
        self.__height = height
    def get_height(self):
        return self.__height

    def get_type(self):
        print("cat")

    def toString(self):
        return "{} is {} cm tall".format(self.__name, self.__height)

cat = Animal()
cat.set_name("Whisker")
cat.set_height(33)
print(cat.toString())

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animal =  AnimalTesting()
test_animal.get_type(cat)