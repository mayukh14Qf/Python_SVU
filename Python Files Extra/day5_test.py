# Question 2

ab=int(input("enter base in cm"))
bc=int(input("enter height in cm"))
ca=int(input("enter hypotenuse in cm"))
if ((ab)**2)+((bc)**2)==((ca)**2):
    print("it is Right Angle Triangle")
else:
    print("not a right angle")

#Question 3

num1=int(input())
num2=int(input())
digit1=num1%10
digit2=num2%10
print(digit2+digit1)


# Question 4
s=input("enter a String")
p=s[::-1]
if s==p :
    print("Palindrome")
else:
    print("Not a palindrome")

#Question 5

c='c'
b=99
print(ord(c))
print(chr(b))

