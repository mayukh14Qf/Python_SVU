# Question 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num1=int(input("enter your limit "))

for i in range(1,num1+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Question 2

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

num2=int(input("enter your limit "))

for i in range(0,num2):
    for j in range(1,num2-i+1):
        print(j,end=" ")
    print()

# Question 3

# a
# a b
# a b c
# a b c d
# a b c d e

num3=int(input("Enter your limit: "))

for i in range(1,num3+1):
    for j in range(0,i):
        print(chr(97+j),end=" ")
    print()

# Question 4

# INPUT:aaaabbbccddd
# OUTPUT:a4b3c2d3

s=input("enter a string")
p=''
i=0
while i<len(s):
    count1=0
    while(i<len(s)-1) and (s[i]==s[i+1]):
        count1=count1+1
        i=i+1
    p=p+s[i]+str(count1+1)
    i=i+1
print(p)

# Question 5

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

num4=int(input("enter a limit"))
k=1
i=1
while i<num4+1:
    j=0
    while j<i:
        print(k,end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()



