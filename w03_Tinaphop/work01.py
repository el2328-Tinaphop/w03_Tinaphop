# if - else
A = 1

if A > 10 :
     print("A is greater than 10")
else :
     print("A is less than 10")

B = int(input("Enter a number: "))
if  B > 10 :
     print("B is greater than 10")
else :
     print("B is less than 10")

try : 
     if  B > 10 :
         print("B is greater than 10")
     else :
         print("B is less than 10")
except ValueError :     
         print("Error")

if A > 0 :
        print("A is positive")
elif A < 0 :
        print("A is negative")
else : 
        print("A is between 1 to 9")