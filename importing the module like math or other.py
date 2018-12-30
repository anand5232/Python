# how to import module in python
import math
x=math.sqrt(16)
print(x)

# we can change the name of the math as m

import math as m
x=math.sqrt(18)
print(x)

# we can also use some function that is only going to use
# here you want to use only a math function that is sqare root
from math import sqrt
from math import factorial
x=sqrt(25)
y=factorial(5)
print(x)
print(y)
