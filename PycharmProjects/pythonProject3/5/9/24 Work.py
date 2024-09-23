x="Python"
def myProgramme():
    x="Java"
    print(x)
myProgramme()

x="Python"
def myProgramme():
    global x
    x="Java"
    print(x)
myProgramme()

x="Python"
def myProgramme():
    x="Java"
print(x)
myProgramme()

print('"KAVISRI"')
print("'KAVISRI'")

def myName(name):
    print("My Name is",name)
def mySin_Number(sin_number):
    print("My Sin_Number is",sin_number)
def myDOB(DOB):
    print("My DOB is",DOB)
def myGender(gender):
    print("My Gender is",gender)
myName("KAVISRI")
mySin_Number("E21CS025")
myDOB("15.07.2004")
myGender("Female")

#Boolean Values
print(10==10)
print(10>1)
print(10<11)
print(1==10)

#Control Statements
def votingEligiblity(age):
    if age>=18:
        print("Eligible To Vote")
    else:
        print("Not Eligible To Vote")
votingEligiblity(20)
votingEligiblity(15)

def oddorEven(a):
    if(a % 2)==0:
        print("a is an even number")
    else:
        print("a is an odd number")
oddorEven(10)
oddorEven(3)
oddorEven(15)
oddorEven(14)
#
# #AND OPERATOR
#      #age=20,weight=50
# age=int(input("Enter Your Age"))
# weight=int(input("Enter Your Weight"))
# def bloodDonation():
#     if(age>=20 and weight>=50):
#         print("Eligible to donate the blood")
#     else:
#         print("Not Eligible to donate the blood")
# bloodDonation()
#
# #OR OPERATOR
# age=int(input("Enter Your Age"))
# weight=int(input("Enter Your Weight"))
# def cricketMatch():
#     if(age>=18 and weight>=50):
#         print("Eligible to play the match")
#     else:
#         print("Not Eligible to play the match")
# cricketMatch()
#
# a=int(input("Enter a's Height"))
# b=int(input("Enter b's  Height"))
# c=int(input("Enter c's Height"))
# def heightOfabc():
#  if(a>b and a>c):
#   print("a is Taller than b and c")
#  elif (b > c and b > a):

#      print("b is Taller than b and c")
#  else:
#     print("Enter the correct Height")
# heightOfabc()

#Looping Statements
# a=1
# while a<=10:
#  print(a)
#  a = a + 1
#
# a=10
# while a>=1:
#  print(a)
#  a = a - 1
#
# a=-10
# while a<=10:
#  print(a)
#  a+=1


#For Loop
for i in range(1,11):
 print(i)

for i in range(10,0,-1):
 print(i)

for i in range(-10,11,+1):
 print(i)

