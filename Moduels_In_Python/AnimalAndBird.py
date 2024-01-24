# Importing Modules having Same Name Of Functions
# Approach 1 Just Import by Module Name
import Animal
import Bird

Animal.fly()  # Animals Cant Fly
Animal.colour()  # Colour Of Animal is Black
Bird.fly()  # Birds Can Fly
Bird.colour()  # Colour Of Bird  is White

# Approach 2  In This Approach This will give the Result For Latest Import Statement
# And Hides The Previous Import Statement
from Animal import *
from Bird import *

fly()  # Birds Can Fly
colour()  # Colour Of Bird  is White

# Approach 3 Solving the Above Issue =First Import And call the belonging module Functions
from Animal import *

fly()  # Animals Cant Fly
colour()  # Colour Of Animal is Black
from Bird import *

fly()  # Birds Can Fly
colour()  # Colour Of Bird  is White
