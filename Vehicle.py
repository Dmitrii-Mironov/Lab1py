from typing import List, Optional, Union

class VehicleError(Exception):
    pass

class Vehicle:
    def __init__(self, make: str, model: str, year: int, color: str) -> None:
        self.make: str = make #марка транспорта
        self.model: str = model
        self.year: int = year
        self.color: str = color

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, doors: int) -> None:
        super().__init__(make, model, year, color)
        self.type = "Car"
        self.doors: int = doors
    def honk_horn(self) -> str:
        return "Beep beep!"
    def get_info(self):
        return f" {self.type} {self.make} {self.model} {self.year} {self.color} with {self.doors} doors"

