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

class Truck(Vehicle): #грузовик
    def __init__(self, make: str, model: str, year: int, color: str, payload_capacity: int) -> None:
        super().__init__(make, model, year, color)
        self._payload_capacity: int = payload_capacity #грузоподьемность
    def load_payload(self, weight: int) -> Union[str, None]: #масса груза
        try:
            if weight <= 0:
                raise VehicleError("Weight must be greater than zero")
            if weight <= self._payload_capacity:
                return f"Loaded {weight} kg of payload"
            else:
                raise VehicleError("Payload exceeds capacity")#превышает
        except VehicleError as e:
            return str(e)
    def get_info(self):
        return f" {self.make} {self.model} {self.year} {self.color} with {self._payload_capacity} doors"
