# Question 1 ( Strong Number)

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


# Question 2 (Perfect Number)

num4= int(input("Enter a number: "))

sum2=0
print("The prime Factors are :")
for i in range(1,num4):
    if num4%i==0:
        print(i)
        sum2=sum2+i
if sum2==num4:
    print("The number is Perfect")
else:
    print("The number is not Perfect")

