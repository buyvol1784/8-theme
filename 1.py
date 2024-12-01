try:
    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в метрах: "))

    print(f"Введенный вес: {weight} кг")
    print(f"Введенный рост: {height} м")

    bmi = (1.3 * weight) / (height ** 2.5)

    if bmi < 18.5:
        interpretation = "Недостаточная масса тела"
    elif bmi < 25:
        interpretation = "Нормальная масса тела"
    elif bmi < 30:
        interpretation = "Избыточная масса тела (предожирение)"
    else:
        interpretation = "Ожирение"

    print(f"Ваш ИМТ: {bmi:.2f}")
    print(f"Интерпретация: {interpretation}")

except ValueError:
    print("Ошибка: Пожалуйста, введите числовые значения для веса и роста.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль. Проверьте введенные данные для роста.")
except Exception as e:
    print(f"Произошла ошибка: {e}")