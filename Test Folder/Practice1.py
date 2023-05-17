for i in range(2, 4):
    print(i, end=" ")
    print ("\n")

a = 12
if a < 2:
    print("Holberton\n")
elif a % 2 == 0:
    print("C is fun\n")
else:
    print("School\n")


if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")


if 12 == 48/4:
    print("Holberton\n")
else:
    print("School\n")

for i in range(4):
    print(i, end=" ")

a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton\n")
    else:
        print("C is fun\n")
else:
    print("School\n")


for i in range(0, 3):
    print(i, end=" \n")


a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
a.get('projects')[3]

for i in [1, 3, 4, 2]:
     print(i, end=" ")