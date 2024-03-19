# Question 1

s=input("Enter a string: ")
a="aeiouAEIOU"

for i in s:
    if i in a:
        s=s.replace(i,'c')
        print(i)
print(s)

# Count number of digits (Method 1)

num1=int(input("Enter a number: "))

count=0
while num1>0:
    count=count+1
    num1=num1//10
print("Number of Digits ",count)

# Count number of digits (Method 2)

num2=int(input("Enter a number: "))
s=str(num2)

print("Number of Digits ",len(s))
