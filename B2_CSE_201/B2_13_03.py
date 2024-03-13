# Question 1 (Armstrong Number)

num1=int(input("Enter a number "))
num=num1
digits=len(str(num1))
arm=0
while num1>0:
    arm=arm+((num1%10)**digits)
    num1=num1//10
if num==arm:
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")

# Question 2 ( Strong Number )

import math
num1=int(input("Enter a number "))
num=num1
strong=0
while num1>0:
    strong=strong+(math.factorial(num1%10))
    num1=num1//10
if strong==num:
    print("The number is Strong Number")
else:
    print("The number is not Strong Number")

# Question 3 (Condition Checking for different cases)

# s="@&*"
# p="1234567890"
# string1=input()
# box1=False
# box2=False
# for i in string1:
#     if i in s:
#         box1=True
#     elif i in p:
#         box2=True
#     else:
#         continue
# if box1 and box2:
#     print("both are available")
# elif box1:
#     print("only special Character")
# elif box2:
#     print("only numeric character")
# else:
#     print("not available")