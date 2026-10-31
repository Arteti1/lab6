"""
Юніт-тести для Лабораторної роботи № 6 (Варіант 11: пакет dice).
"""
import unittest
from src.dice.single_die import roll_die
from src.dice.multiple_dice import roll_dice


class TestDicePackage(unittest.TestCase):

    def test_roll_die(self):
        """Перевірка кидка одного кубика (результат має бути від 1 до 6)."""
        result = roll_die()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_roll_dice_sum(self):
        """Перевірка суми кидків кількох кубиків."""
        # Якщо кидаємо 3 кубики, мінімальна сума = 3, максимальна = 18
        result = roll_dice(3)
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 18)

    def test_roll_dice_invalid_count(self):
        """Перевірка генерації помилки при невірній кількості кубиків."""
        with self.assertRaises(ValueError):
            roll_dice(0)
        with self.assertRaises(ValueError):
            roll_dice(-2)


if __name__ == '__main__':
    unittest.main()