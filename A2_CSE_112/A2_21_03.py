# Question 1 (prime Number)

num= int(input('Enter a number: '))
counter=0
for m in range(1,num+1):
    if num%m==0:
        counter=counter+1
if counter==2:
    print('It is a prime number')
else:
    print('It is not a prime number')

# Question 2 ( Fibonacci series )

range1=int(input("Enter your range"))
b1=0
b2=1
print(b1,end=" ")
print(b2,end=" ")
for i in range(2,range1):
    c=b1+b2
    print(c,end=" ")
    b1=b2
    b2=c

# Question 3 ( Factorial of a number)

num3=int(input("Enter a number: "))

fac=1
while num3>0:
    fac=fac*num3
    num3=num3-1
print(fac)

# Question 4 ( Armstrong Number)

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

# Question 5 ( Prime up to a range)

range1=int(input("Enter your Range"))
for i in range(1, range1+1):
    counter=0
    for j in range(1, i+1):
        if i % j==0:
            counter+=1
    if counter==2:
        print(i)