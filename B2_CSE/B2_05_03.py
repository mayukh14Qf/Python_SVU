# Leap Year

year=int(input("Enter your year : "))

import calendar

if calendar.isleap(year):
    print("The year is Leap year")
else:
    print("not leap year")

# Question 1

s=input('Enter a string: ')
p=s[::-1]
if s==p:
    print("Palindrome")
else:
    print("Not Palindrome")

print(s[0:4:2])
print(s[0:])
print(s[:4])
print(s[-1:-4:-1])
print(s[-1:-6:-2])

# Question 2

s=input("Enter another string: ")
p=len(s)
if p%2==0:
    print(s[0:int(p/2)])
else:
    print(s[0:int((p+1)/2)])

# Check present or Not

s="123"
if "3" not in s:
    print("false")










