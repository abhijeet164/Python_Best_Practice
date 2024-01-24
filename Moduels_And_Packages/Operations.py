# How To Call Function ?Method Of One Module To Another Module

# Approach 1 ==> If Imported only module Name Than Specify module Name Before The Function Name
import Calculator

Calculator.add(2, 3)
Calculator.mul(4, 5)

# Approach 2 ==> Use Form To Import Specific Function To Import
from Calculator import add, mul

add(12, 23)
mul(7, 9)

# Approach 3 ==> Use * To Import All TYhe Class And Method Name
from Calculator import *

add(20, 30)
mul(4, 9)
