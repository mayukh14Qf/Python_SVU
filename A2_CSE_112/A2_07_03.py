
s="mayukhjit"

# String Slicing

print(s[5])
print(s[0:6])
print(s[:6])
print(s[2:])

print(s[0:6:2])
print(s[0:6:3])

print(s[-1:-6:-1])
print(s[::-1])

# Change to upper case
print(s.upper())

# Change to lower case
s1="MAYUKHJIT"
print(s1.lower())

# Find the index present or not , if not then it will return -1, else it will return the index position

print(s.find("a"))
print(s.find("z"))

# Check that particular character present or not, it will return true or false

char='z'
if char in s:
    print("Available")
else:
    print("Not Available")

# counting the presence of particular character in integer

print(s.count('y'))

#  \n for new line

s2 = "Bishal\'s \nDidi "

print(s2)

name=input()

print(f"the house is {name}")

print(s.count('z'))

# Question 1

s=input("Enter a string: ")

p=s[::-1]
print(p)

if p==s:
    print("Palindrome")
else:
    print("Not Palindrome")

#  Question 2

s=input("Enter a string: ")

sum1=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')+s.count('A')+s.count('E')+ s.count('I')+ s.count('O')+s.count('U')

print(sum1)
if sum1>5:
    print("more than 5 vowels")
elif sum1==5:
    print("exactly 5 vowels")
else:
    print("less than 5")
















