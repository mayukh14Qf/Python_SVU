# Question 1

# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input("enter 3rd number"))
#
# d=max(a,b,c)
# print("greatest of three",d)

# Question 2

# s=input("enter your String")
# char1=s[0]
# print(char1)
# p="AEIOUaeiou"
#
# if char1 in p:
#     print("it is Vowel")
# else:
#     print("it is Not Vowel")


# question 3

# s= input("enter a string")
# p=len(s)
# if p%2==0 :
#     print(s[int((p/2)-1)],s[int(p/2)])
# else:
#     print(s[int(((p+1)/2))-1])



# Question 4

first=int(input("enter 1st number : "))
second=int(input("enter 2nd number : "))

last=first%10
digits=second//10

print(last,digits)

if digits%last==0:
    print("Integer")
else:
    print("Not Integer")










