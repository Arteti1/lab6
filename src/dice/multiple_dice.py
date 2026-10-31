"""
Модуль для імітації кидка декількох шестигранних кубиків.
"""
from .single_die import roll_die


def roll_dice(num_dice: int) -> int:
    """
    Імітує кидок декількох шестигранних кубиків та повертає суму результатів.


    Returns:
        int: Сума результатів усіх кинутих кубиків.

    """
    if num_dice <= 0:
        raise ValueError("Кількість кубиків має бути більшою за 0")

    return sum(roll_die() for _ in range(num_dice))