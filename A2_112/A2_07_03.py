
s="mayukhjit"

# print(s[5])
# print(s[0:6])
# print(s[:6])
# print(s[2:])

# print(s[0:6:2])
# print(s[0:6:3])
#
# print(s[-1:-6:-1])
# print(s[::-1])


# print(s.upper())
#
# s1="MAYUKHJIT"
# print(s1.lower())

# print(s.find("a"))
# print(s.find("z"))

# char='z'
# if char in s:
#     print("Available")
# else:
#     print("Not Available")

# print(s.count('y'))

# s2 = "Bishal\'s \nDidi "
#
# print(s2)

# name=input()
#
# print(f"the house is {name}")

# print(s.count('z'))

# Question 1

# s=input("Enter a string: ")
#
# p=s[::-1]
# print(p)
#
# if p==s:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




#  Question 2

s=input("Enter a string: ")

sum=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')+s.count('A')+s.count('E')+ s.count('I')+ s.count('O')+s.count('U')

print(sum)
if sum>5:
    print("more than 5 vowels")
elif sum==5:
    print("exactly 5 vowels")
else:
    print("less than 5")
















