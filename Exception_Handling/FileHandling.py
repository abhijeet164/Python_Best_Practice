# wrinting  text  inside a text file

file=open("C:\ISTQB Agile\myfile.txt",'w')
file.write("Hello Anuradha\n")
file.write("Hello Radha\n")
file.write("Hello Nilam\n")
file.write("Hello Nilu\n")
file.close()
print("Program Completed")



# Read the data on console
file=open("C:/Python Notes/anuradha.txt",'r')
s=file.read()
print(s)

# Appending data to file
file=open("C:/Python Notes/anuradha.txt",'a')
file.write("Good Morning Anu \n")
file.write("Good Morning Radha\n")
file.write("Good MorningAisharya \n")
print("Execution Coplitade")























