# Find the largest number between three numbers
a = int(input("Enter First Number"))

b = int(input("Enter Second number"))

c = int(input("Enter Third number"))


if a>b:
    if a>c:
        print(a)
elif b>c:
    if b>a:
        print(b)
else:
    print(c)


'''
Output
Enter First Number20
Enter Second number30
Enter Third number15
30
'''
