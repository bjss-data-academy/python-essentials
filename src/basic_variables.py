first_name = "Alan"
print(type(first_name))

# Integers
quantity = 11
print(type(quantity), quantity)

half_quantity = quantity / 2
print(type(half_quantity), half_quantity)


# Big integers
large_integer = 99912367826748762876478287636646782876234678432876234
print("large int", large_integer)
print("ginormous int", large_integer*large_integer*large_integer) # that was nothing 

large_float = 99912367826748762876478287636646782876234678432876234.0165
print("large float showing precision limitations", large_float)


# Showing dynamic typing - changing the data type of a variable at runtime
dynamic_type = "dogbanana"
print(type(dynamic_type), dynamic_type)

dynamic_type = 11
print(type(dynamic_type), dynamic_type)

dynamic_type = dynamic_type / 2
print(type(dynamic_type), dynamic_type)

# Type casting
quantity_as_text = "26"
quantity = int(quantity_as_text)

print("quantity as integer", type(quantity), quantity)

# Decimal module
from decimal import *

a = Decimal(1)
b = Decimal(7)
result = a/b
print(result)

# Strings

single_quoted = "Hello 'Alan' - if that's your real name!"
print(single_quoted)

double_quoted = 'Hello "Alan" - if you are really called that!'
print(double_quoted)

many_lines = """I mean,
just how
many libes of text
do you 
really need?
"""
print(many_lines)

# String slices
source = "A stitch in time saves a mixed metaphor"

first_ten = source[:10]
print(first_ten)

all_after_tenth = source[10:]
print(all_after_tenth)

middle = source[10:15]
print(middle)

from_the_end =  source[-5:-2]
print(from_the_end)

# String concatenation

start = "Can we join it? "
end = "yes we can!"
result = start + end
print(result)

# F strings
item = "bananadog"
template = f"Blimey! I did not expect to see a {item}!"
print(template)

# String methods

original = "i wish i was in upper case!"
result = original.upper()
print(result)


# Date example
import time
from datetime import date

today = date.today()

my_birthday = date(2001, 12, 31)
time_to_birthday = abs(my_birthday - today)
print(time_to_birthday.days)


# Complex numbers
a = 2-3j # native complex literals supported
print(type(a), a)

x = complex(3, 5)
print(x) # Note Python uses j to represent root(-1) like engineering, not maths

x = complex(0, 2)
print(x)

y  =complex('0+2j') # Parse from string representation. No spaces around '+'
print(y)

print ("x*y=", x * y) # Multiplies two complex numbers to give a real