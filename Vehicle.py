from typing import List, Optional, Union

class VehicleError(Exception):
    pass

class Vehicle:
    def __init__(self, make: str, model: str, year: int, color: str) -> None:
        self.make: str = make #марка транспорта
        self.model: str = model
        self.year: int = year
        self.color: str = color