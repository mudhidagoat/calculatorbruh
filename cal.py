num1 = float(input("skriv det første nummer: "))
op = input("skriv dit beregningsform: ")
num2 = float(input('skriv det andet nummer: '))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)      
elif op == "*":
    print(num1 * num2)
else:
    print("du skal write to tal kom nu")

