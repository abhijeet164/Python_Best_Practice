#Approach 1

import sys
sys.path.append("C:/Python Project/Python_Best_Practice/Packages_In_Python/PackageA")
sys.path.append("C:/Python Project/Python_Best_Practice/Packages_In_Python/PackageA/SubPackageA")


import ModuleA1
import ModuleB1

ModuleA1.display1() #This Is display1 Function of ModuleA1
ModuleB1.show1()  #This is show1 Function Of ModuleB1


# Approach 2 Import all by * now no need to write fully qualified name

import sys
sys.path.append("C:/Users/abhij/PycharmProjects/pythonProject/day9/PackageA")
sys.path.append("C:/Users/abhij/PycharmProjects/pythonProject/day9/PackageA/SubPackageA")

from ModuleA1 import *
from ModuleB1 import *

display1() #This Is display1 Function of ModuleA1
show1()  #This is sho   w1 Function Of ModuleB1