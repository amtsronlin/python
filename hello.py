import random
import sys
import os

print("Hello World")
# String -----------------------------------------
name = "Derek"
print(name)
number = 15
print("5-3=", 5-3)

quote = "\" Alway remeber that you are unique"

multi_line_quote = ''' just
like every one else'''

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
#-------------------------------------------------

# Array ------------------------------------------
grocery_list = ['tomato', 'banana' , 'tea', 'cream']
grocery_list[0] = 'water melon'
print(grocery_list[0])
print(grocery_list[1:3])
#-------------------------------------------------

# Loop ------------------------------------------
age = 16
if age > 16 :
    print('you are old')
elif age == 16:
    print('you are young')
else :
    print('you are still baby')
random_num = random.randrange(0,100)
while(random_num != 15 or random_num == 5):
    print(random_num)
    random_num = random.randrange(0,100)
for x in  range(0, 10):
    print(x, ' ', end='' )
#-------------------------------------------------