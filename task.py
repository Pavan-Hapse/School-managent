import sys
sys.path.append("/mymodules/")
import mymodules
from mymodules import *

print(responses[3])
print(responses[4])
print(responses[5])

print("\n Enter your Choice From below Menu :-")
print("\n 1 : Teachers Login")
print(" 2 : Students Login")

no=int(input("\n Enter Your Choice :- "))


class Base:
       def f2():
              print(responses[6])
              print(responses[7])
              print(responses[8])
              t1=input("Enter Teacher's User Name:- ")
              t2=tuple(input("Enter Password:- "))
              
       def f4():   
              print("Enter Teacher's Information: ")
              p1=input("Enter Teacher's Name:- ")
              p2=input("Enter Teacher's Subject:- ")
              p3=input("Enter Teacher's Address:- ")

              print("Your Good Name is:- ",p1)
              print("Your Subject is:- ",p2)
              print("Your Address is:- ",p3)       


       

class Base1:
       def f1():
              print(responses[0])
              print(responses[1])
              print(responses[2])
              t1=input("Enter Student's User Name:- ")
              print("Enter student's Information: ")
              k1=input("Enter Student's Name:- ")
              k2=input("Enter Student's Subject:- ")
              k3=input("Enter Student's Address:- ")

              print("Your Good Name is:- ",k1)
              print("Your Subject is:- ",k2)
              print("Your Address is:- ",k3)

class Dummy:
       def f2():
              t1=input("Enter Teacher's User Name:- ")
              t2=tuple(input("Enter Password:- "))
              
       def f4():   
              print("Enter Teacher's Information: ")
              p1=input("Enter Teacher's Name:- ")
              p2=input("Enter Teacher's Subject:- ")
              p3=input("Enter Teacher's Address:- ")

              print("Your Good Name is:- ",p1)
              print("Your Subject is:- ",p2)
              print("Your Address is:- ",p3)       


       
class Dummy1:
       def f1():
              t1=input("Enter Student's User Name:- ")
              print("Enter student's Information: ")
              k1=input("Enter Student's Name:- ")
              k2=input("Enter Student's Subject:- ")
              k3=input("Enter Student's Address:- ")

              print("Your Good Name is:- ",k1)
              print("Your Subject is:- ",k2)
              print("Your Address is:- ",k3)


if no==1:
       while True:   
              Base.f2()
              Base.f4()
              ch=input("Do You want to switch the module..? Please enter Y/N: ")
              while ch=='Y' or ch=='y':
                     Base1.f1()
              if ch=='N' or ch=='n':
                     Dummy.f2()
                     Dummy.f4()
       ch=input("Do You want to switch the module..? Please enter Y/N: ")
       
if no==2:
       while True:
              Base1.f1()
              ch=input("Do You want to switch the module..? Please enter Y/N: ")
              while ch=='Y' or ch=='y':
                     Base.f2()
                     Base.f4()
              if ch=='N' or ch=='n':
                     Dummy1.f1()
       ch=input("Do You want to switch the module..? Please enter Y/N: ")
                     
                     
                     
       



