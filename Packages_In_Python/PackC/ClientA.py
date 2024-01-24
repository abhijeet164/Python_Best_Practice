import sys
sys.path.append("C:/Python Project/Python_Best_Practice/Packages_In_Python/PackA")
sys.path.append("C:/Python Project/Python_Best_Practice/Packages_In_Python/PackB")


import Emp
empobj=Emp.Employee("Abhijeet",105,5000)
empobj.display() #Abhijeet 105 5000

import Stud
sobj=Stud.Student("Nilam",108,90)
sobj.show() #Nilam 108 90


from Emp import Employee
empobj=Employee("Abhijeet",105,5000)
empobj.display()

from Stud import Student
stobj=Student("Anuradha",14,5)
stobj.show() #Anuradha 14 5
