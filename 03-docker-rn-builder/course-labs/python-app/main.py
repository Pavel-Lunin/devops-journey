import calendar

print("Добро пожаловать в программу, которая выводит календарь на выбранный месяц и год.")


def main():
    try:
        year = int(input("Введите год: "))
    except ValueError:
        print("Неверный год. Используйте число.")
        return

    try:
        month = int(input("Выберите месяц (1-12): "))
    except ValueError:
        print("Неверный месяц. Используйте число от 1 до 12.")
        return

    if month < 1 or month > 12:
        print("Месяц должен быть от 1 до 12.")
        return

    print()
    print(calendar.month(year, month))

    weekday_index = calendar.weekday(year, month, 1)
    weekday_names = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
    ]
    print(f"Первый день этого месяца: {weekday_names[weekday_index]}")


if __name__ == "__main__":
    main()
