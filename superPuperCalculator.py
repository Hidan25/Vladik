print("Welcome to Super Puper Calculator!")


def superPuperCalculator():
    num_1 = float(input("Enter your first number: "))
    num_2 = float(input("Enter your second number: "))
    action = input("Enter your operator (+, -, *, /): ")
    if action == "+":
        result = num_1 + num_2
    elif action == "-":
        result = num_1 - num_2
    elif action == "*":
        result = num_1 * num_2
    elif action == "/":
        if num_2 == 0:
            print("Nine!Nine!Nine!")
            return None
        else:
            result = num_1 / num_2
    else:
        print("Invalid operator!")
        return None
    return result


result = superPuperCalculator()
print(result)
