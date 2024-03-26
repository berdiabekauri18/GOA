#Union

from typing import Union

def some_calculation(x: Union[int, float], y: Union[int, float]) -> int:
    return (x + y) ** 2

def some_calculation(x: int | float, y: int | float) -> int:
    return (x + y) ** 2