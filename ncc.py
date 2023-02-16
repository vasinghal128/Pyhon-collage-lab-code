# Enter age, hight, weight and tell that person is eligable for ncc or not
age = int(input("Enter your age"))

hight = float(input("Enter your hight"))

weight = int(input("Enter your weight"))

if age>18:
    if hight>5.8:
        if weight>60:
           print("You are eligable for ncc")
else:
    print("You are not eligable for ncc")



'''
Output

Enter your age19
Enter your hight5.9
Enter your weight61
You are eligable for ncc
'''
