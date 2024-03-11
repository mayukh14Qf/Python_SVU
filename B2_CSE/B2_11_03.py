# While loop

# var=0
# while var<10:
#     print(var)
#     var=var+1

# i=0
# while i <20:
#     i=i+2
#     print(i)


# prime Number ( For loop)

# num= int(input('Enter a number: '))
# counter=0
# for m in range(1,num+1):
#     if num%m==0:
#         counter=counter+1
# if counter==2:
#     print('It is a prime number')
# else:
#     print('It is not a prime number')


# Prime Number (While loop)

# num= int(input("Enter a number"))
# i=1
# counter=0
# while i<=num:
#     if num % i==0:
#         counter=counter+1
#     i=i+1
# if counter==2:
#     print('It is a prime number')
# else:
#     print('It is not a prime number')


# Question 2

# num1 = int(input('Enter a number: '))
#
# while num1>=10:
#     num1=int(num1//10)
# print(num1)

# Question 3

range1=int(input("Enter your Range"))
for i in range(1,range1+1,):
    counter=0
    for j in range(1,i+1):
        if i%j==0:
            counter+=1
    if counter==2:
        print(i)







