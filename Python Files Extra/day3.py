# Even or Not

a=int(input("enter a number"))
if a==0:
    print("more than zero")
elif a%2==0 :
    print("Even")
else:
    print("Odd")

# Positive or Not

b= int(input("enter a number "))

if b>0:
    print("positive")
else:
    print("negative")

# Greatest of three
# method 1
x= int(input("enter 1st number"))
y=int(input("enter 2nd number"))
z=int(input("enter 3rd number "))
p=max(x,y,z)
print(p)

# method 2

if (x>y) and (x>z):
    print(x)
elif (y>x) and (y>z):
    print(y)
else:
    print(z)

# Vowel or NOT

char=input("enter your character")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char == 'I' or char =='O' or char=="U":
    print("It is vowel")
else:
    print("Consonant")


