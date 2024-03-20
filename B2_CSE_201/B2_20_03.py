# Pattern 6

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

limit=int(input("Enter the limit "))

for i in range(1, limit+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

# Pattern 7

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

limit=int(input("Enter the limit "))

for i in range(0,limit):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(0,limit-i):
        print("*",end=" ")
    print()

# Pattern 8

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

limit=int(input("Enter the limit "))

for i in range(0,limit):
    for j in range(0,limit-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

# Pattern 9 (Diamond pattern)
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

limit=int(input("Enter the the limit "))

for i in range(0,limit):
    for j in range(0,limit-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0, i):
        print("*",end=" ")
    print()
for i in range(0,limit):
    for j in range(0,i+1):
        print(" ",end=" ")
    for j in range(0,limit-i-1):
        print("*",end=" ")
    for j in range(limit-i-2):
        print("*",end=" ")
    print()
