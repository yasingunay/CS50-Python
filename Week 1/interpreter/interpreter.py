expression = input("Expression: ")
try:
    x,y,z = expression.split(" ")
    x = float(x)
    z = float(z)
except ValueError:
    print("Invalid input. Please enter an expression in the format 'number operator number'.")
    


match y:
    case "+":
        print((x + z))
    case "-":
        print((x - z))
    case "*":
        print(x * z)
    case "/":
        if z != 0:
            print((x / z))
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please use one of the following: +, -, *, /.")