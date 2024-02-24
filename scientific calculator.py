import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x):
    return math.log(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    elif choice in ('6', '7', '8', '9', '10'):
        num = float(input("Enter number: "))

        if choice == '6':
            print("Result:", square_root(num))
        elif choice == '7':
            print("Result:", logarithm(num))
        elif choice == '8':
            print("Result:", sin(num))
        elif choice == '9':
            print("Result:", cos(num))
        elif choice == '10':
            print("Result:", tan(num))
    else:
        print("Invalid Input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
