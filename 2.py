def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль недопустимо")
            result = num1 / num2
        else:
            raise ValueError("Некорректный оператор")

        print(f"Результат: {num1} {operator} {num2} = {result}")

    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите числа и корректный оператор.")
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}. Пожалуйста, убедитесь, что второе число не равно нулю.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

calculator()