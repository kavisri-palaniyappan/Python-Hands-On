# # Pattern Problem
# n=int(input())
# for i in range(1,n+1,1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")
# # Middle Width Pattern Problem
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     print()
# # Reverse Pattern Problem
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         print(k,end="")
#     print()
# # 1-10 Printing
# for i in range(1,11,1):
#     print(i)
#  # Reverse of 1-10 Printing
# for i in range(10,0,-1):
#     print(i)
# # Triangle Pattern
# n=int(input())
# for i in range(1,n+n,2):
#     for j in range(1,n+n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()
# Diamond Pattern
# n=int(input())
# t=1;
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end="")
#     for k in range(1,i+t,1):
#         print(k,end="")
#     t=t+1
#     print()
# t=t-2
# for i in range(n-1,0,-1):
#     for j in range(n-i,0,-1):
#         print(" ",end="")
#     for k in range(1,i+t,1):
#         print(k,end="")
#     t=t-1
#     print()
# String
# a=input("Enter the Input String")
# count=0
# a=a.lower()
# for i in a:
#     if i=='a' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         count+=1
# if count==0:
#     print("No Vowels")
# else:
#     print(""+ str(count))
#
# Finding  Duplicate Letters Count
# n=input()
# s=set()
# for i in range(len(n)):
#     c=0
#     for j in range(len(n)):
#         if n[i]==n[j]:
#             c=c+1
#     if c>1:
#         s.add(n[i])
# print(len(s))




















