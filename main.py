from calculus_core import derivative, integrate, limit, solve_equation, partial_derivative

print("классный математический калькулятор")
print("1 - производная")
print("2 - интеграл")
print("3 - предел")
print("4 - решить уравнение")
print("5 - частные производные")
print("выход - выход из калькулятора")

while True:
    print()
    choice = input("выберите операцию(цифру): ")
    
    if choice == "выход":
        print("до новых встреч!")
        break
    
    if choice == "1":
        expr = input("выражение: ")
        var = input("переменная: ")
        result = derivative(expr, var)
        print("производная:", result)
    
    elif choice == "2":
        expr = input("выражение: ")
        var = input("переменная: ")
        result = integrate(expr, var)
        print("интеграл:", result)
    
    elif choice == "3":
        expr = input("выражение: ")
        var = input("переменная: ")
        point = input("точка: ")
        result = limit(expr, var, point)
        print("предел:", result)
    
    elif choice == "4":
        expr = input("уравнение: ")
        var = input("переменная: ")
        result = solve_equation(expr, var)
        print("решение:", result)
    
    elif choice == "5":
        expr = input("выражение: ")
        vars = input("переменные через пробел: ")
        result = partial_derivative(expr, vars)
        print("частные производные:", result)
    
    else:
        print("не понятно, попробуйте еще раз")