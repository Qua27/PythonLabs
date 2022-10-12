from math import exp, sin, cos

print("Choose an operation from the list below:")
print("1. +\n2. -\n3. *\n4. /\n5. ^\n6. exp(x+y)\n7. sin(x+y)\n8. cos(x+y)")
choice = int(input())
print("Enter two numbers:")
a, b = map(float, input().split())
if choice == 1:
    print(a + b)
if choice == 2:
    print(a - b)
if choice == 3:
    print(a * b)
if choice == 4:
    if b == 0:
        print("Zero Division Error")
        exit(1)
    print(a / b)
if choice == 5:
    print(a ** b)
if choice == 6:
    print(exp(a + b))
if choice == 7:
    print(sin(a + b))
if choice == 8:
    print(cos(a + b))
