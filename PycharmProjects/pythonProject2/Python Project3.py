#Global Variable
from tkinter import Variable

name="jack"

def mydata():
  print("my data is",name)

def myname():
  print("my name is",name)
mydata()
myname()
print(name)


name="KAVISRI"
def myname():
 print("My Name is",name)
myname()
sin_number="e21cs025"
def mysin_number():
 print("My Sin Number is",sin_number)
mysin_number()
date_of_birth="15.07.2004"
def mydate_of_birth():
 print("My Date Of Birth is",date_of_birth)
mydate_of_birth()
age="19"
def myage():
 print("My Age is",age)
myage()

#Local Variable
name="Thanga Ponnu"
date_of_birth="14.08.2024"
def myname():
    print("My Sister's Daughter Name is",name)
    print("Her's DOB is", date_of_birth)
myname()

college="Sri Shanmugha College Of Engineering And Technology"
print(len(college))
print(college[2])
print(college[2:])
print(college[:3])
print(college[0:10])
print(college.startswith("Sr"))
print(college.endswith("gy"))
print(college.endswith("ge"))
print(college.find("i"))
print(college.count("e"))
print(college.capitalize())
print(college.upper())
print(college.lower())
print(college.isupper())
print(college.islower())
print(college.index("h"))
print(college.find("x"))
a="    SSCET      "
print(a)
print(a.strip())
b="Kavi"
print(b.isalnum())
c="Kavi0315"
print(c.isalnum())
d="0315"
print(d.isalnum())
d="Kavisri"
print(d.isnumeric())
print(d.split("K"))


















