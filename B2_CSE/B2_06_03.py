# loop

for i in range(10):
    print("hi :))")

for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

s="Mayukhjit"


for i in range(len(s)):
    print(s[i])

for char in s:
    print(char)


# Question 1

num=int(input('Enter a number: '))
sum1 = 0

for i in range(1,num+1):
    sum1 = sum1+i

print("sum is",sum1)


# Question 2

p=int(input("Enter the no of inputs you want to add : "))
sum1=0
for i in range(p):
    p=int(input())
    sum1=sum1+p
print("sum of numbers is ",sum1)

# Question 3

s=input('Enter a string: ')
p="aeiouAEIOU"
count=0
for char in s:
    if char in p:
        print(char)
        count=count+1
print("Number of Vowels are/is :",count)























