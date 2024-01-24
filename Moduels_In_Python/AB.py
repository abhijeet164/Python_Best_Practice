# Approach 1 Specifying the Module Name Explicitly

import A
import B

obj1 = A.Animal()  # In This Approach we Are Specifying The Module name Explicitly
obj1.disp()  # This Is Animal Class Of  Module A

obj2 = B.Birds()
obj2.disp()  # This Bird Class Of Module B

# Approach 2 = In this Approach we Don't need to call Module Name
# Explicitly As already Declared on Import Statement
# From Module Name import  import function and Classes

from A import Animal
from B import Birds

obj1 = Animal()
obj1.disp()  # This Is Animal Class Of  Module A

obj2 = Birds()
obj2.disp()  # This Bird Class Of Module B
