# Step involved in Importing modules from diffreint package
# Step1 Import sys File
# step Declare the path location inside Append method

# Approach 1
import sys

sys.path.append("C:/Python Project/Python_Best_Practice/Packages_In_Python/Pack1")
#
import ModuleA  # Pycharm Issue not to worry  O/p = Disp Function of ModuleA
import ModuleB  # Pycharm Issue not To worry

#
ModuleA.display()
ModuleB.show()

# Approach 2

from ModuleA import *  # Pycharm Issue not to worry
from ModuleB import *  # Pycharm Issue not to worry

display() # O/p = Disp Function of ModuleA
show() # O/p = Show Function Of ModuleB
