# Pattern 1
# * * * *
# * * * *
# * * * *
# * * * *
# * * * *

n=int(input("Enter your limit"))

for i in range(0,n):
    for j in range(0,4):
        print("* ",end="")
    print()

# pattern 2

# *
# * *
# * * *
# * * * *
# * * * * *

n=int(input("Enter your limit"))

for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()

# Pattern 3 (Method 1)
# * * * * *
# * * * *
# * * *
# * *
# *

n=int(input("Enter your limit"))

for i in range(0,n):
    for j in range(0,n-i):
        print("* ",end="")
    print()

# Pattern 3 (Method 2)

n=int(input("Enter the limit"))

for i in range (n,0,-1):
    for j in range (0,i):
        print("* ",end="")
    print()

# pattern 4

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=int(input("Enter your limit"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# pattern 5

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1

n=int(input("Enter your limit"))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()


# Special Short Method for patterns

n=5

for i in range(1,n+1):
    print("* "*i)
for i in range(0,n+1):
    print("* "*(n-i))

for i in range(n,0,-1):
    print("* "*i)
