# Ask the user for their name
user_name = input("Enter your name: ")
print(f"Welcome,{user_name}!")

# Ask for  two numbers (as input)
number1 = int(input("Enter first  number: "))
number2 = int(input("Enter second number: "))


# 3. Perform all 5 operations: addition, subtraction, multiplication, division, modulo
add = number1 + number2
sub = number1 - number2
product = number1 * number2


print(f"{number1}+{number2} = {add} {type(add).__name__}")
print(f"{number1}-{number2} = {sub} {type(sub).__name__}")
print(f"{number1}*{number2} = {product} {type(product).__name__}")

if number2 == 0:
    print("Cannot divide by zero")
else:
    div = number1 / number2
    mod = number1 % number2
    print(f"{number1}/{number2} = {div} {type(div).__name__}")
    print(f"{number1}%{number2} = {mod} {type(mod).__name__}")
