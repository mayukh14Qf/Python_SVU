s="@&*"
p="1234567890"
string1=input()
box1=False
box2=False
for i in string1:
    if i in s:
        box1=True
    elif i in p:
        box2=True
    else:
        continue
if box1 and box2:
    print("both are available")
elif box1:
    print("only special Character")
elif box2:
    print("only numeric character")
else:
    print("not available")



