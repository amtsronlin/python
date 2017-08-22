import random
import sys
import os

fileW = open("testfile.txt", "w")
fileW.write("I have enter something in here")
fileW.close()

fileR = open("testfile.txt", "r")
fileR.read()
fileR.tell()

