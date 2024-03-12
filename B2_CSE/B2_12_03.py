# Question 1 (Sum of the Digits)

num1= int(input("Enter a number"))
sum1=0
while num1>0:
    sum1=sum1+(num1 % 10)
    num1=num1//10
print(sum1)

# Question 2 ( Fibonacci series )

range1=int(input("Enter your range"))
b1=0
b2=1
print(b1,end=",")
print(b2,end=",")
for i in range(2,range1):
    c=b1+b2
    print(c,end=",")
    b1=b2
    b2=c

# Question 3 ( Factorial of a number)

num3=int(input("Enter a number: "))

fac=1
while num3>0:
    fac=fac*num3
    num3=num3-1
print(fac)

# Question 4 (Perfect Number)

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


# Question 5 ( Reverse of a number)

num5=int(input("Enter a number"))
rev=0
while num5>0:
    rev=(rev*10)+(num5%10)
    num5=num5//10
print(rev)


# Difference between // and %

print(1//10)
print(1 %10)



