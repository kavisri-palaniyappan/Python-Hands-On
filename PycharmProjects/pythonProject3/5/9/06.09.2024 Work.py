#Nested For Loop
for i in range(1,4,1):
    for j in range(1,4,1):
        print(i)

for i in range(1,4,1):
    for j in range(1,4,1):
        print(j)

#For Each
# for x in "PYTHON":
#     print(x)

x="JAVA"
x="PYTHON"
x="c#"
print(x)

#Array
x=["JAVA","PYTHON","c#","JAVA"]
print(x)

#Iteration of Array
for i in x:
    print(i)

#To get the given index value
print(x[1])

#To get the size of the array
len1=len(x)
print(len1)

#To add the values after the declaration
append=x.append("c++")
print(x)

#Replace
x[1]="c"
print(x)

#To remove the element based on the Index
x.pop(4)
print(x)

#To remove the element based on the Values
x.remove("JAVA")
print(x)

##Insert the Values
x.insert(1,"JAVA")
print(x)

#Count the Values
count=x.count("JAVA")
print(count)

#Reverse the Values
x.reverse()
print(x)

#To find the Index of the given Value
index=x.index("JAVA")
print(index)

#Ascendind Order
y=["aaple","python","c","java","Zoom"]
y.sort()
print(y)

#List
l=["JAVA",10,"PYTHON",10,  True ,98.258,10]
print(l)

#Index values
print(l.index(10))
print(l.index(10,2))
print(l.index(10,2,5))

#Minimum Values
l1=[100,201,25,58,98]
mini=min(l1)
print(mini)

#Maximum Values
maxi=max(l1)
print(maxi)

#Copy the Values
newlist=l.copy()
print(newlist)















