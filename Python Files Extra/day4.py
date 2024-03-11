# Question 1

year = int(input("enter your year"))

if (year % 4 == 0) and (year % 100 != 0):
    print("Leap year")
elif year % 400 == 0:
    print("leap year")
else:
    print("not A leap Year")

# 2nd Question

number = int(input("Enter your Number "))

if number > 90:
    print("Grade A+")
elif (number > 85) and (number < 90):
    print("Grade A")
elif (number > 81) and (number < 84):
    print("Grade B")
elif (number > 71) and (number < 79):
    print("Grade C")
elif (number > 51) and (number < 70):
    print("Grade D")
else:
    print("Fail")



# Question 3

s=input("enter your String")
char=s[0]
if char == 'a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char == 'I' or char =='O' or char=="U":
    print("Vowel")
else:
    print("Consonant")

# Question 4

num=int(input("Enter A number :"))
digit=num%10

if digit>5:
    print("It is greater than Five")
else:
    print("it is not greater than Five")




