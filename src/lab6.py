"""
Основна програма для Лабораторної роботи № 6.
Пакет 'dice': імітація кидків кубиків.
"""
import math
import requests
from dice.single_die import roll_die
from dice.multiple_dice import roll_dice


def main():
    """Основна функція для демонстрації використання модулів та пакетів."""
    print("=== Демонстрація пакету dice ===")
    
    # Використання функцій з власного пакета dice
    single_result = roll_die()
    print(f"Кидок одного кубика: {single_result}")

    try:
        multiple_result = roll_dice(3)
        print(f"Сума кидка трьох кубиків: {multiple_result}")
    except ValueError as e:
        print(f"Помилка: {e}")

    # Приклад використання модуля стандартної бібліотеки
    print(f"\nКвадратний корінь з 16 (math): {math.sqrt(16)}")

    # Приклад використання стороннього пакета
    try:
        response = requests.get("https://api.github.com", timeout=10)
        response.raise_for_status()
        print("Статус код запиту до GitHub API (requests):", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося підключитися до GitHub API: {e}")


if __name__ == "__main__":
    main()