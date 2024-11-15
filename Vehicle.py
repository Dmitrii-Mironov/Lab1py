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

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, engine_cc: int) -> None:
        super().__init__(make, model, year, color)
        self.type = "Motorcycle"
        self.engine_cc: int = engine_cc #двигатель куб.см
    def rev_engine(self) -> str:
        return "Vroom vroom!"

    def get_info(self):
        return f" {self.type} {self.make} {self.model} {self.year} {self.color}with {self.engine_cc} engine_cc"

class Bicycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, gear_count: int) -> None:
        super().__init__(make, model, year, color)
        self._gear_count: int = gear_count #кол-во передач
    def ring_bell(self) -> str:
        return "Ring ring!"
    def get_info(self):
        return f" {self.make} {self.model} {self.year} {self.color} with {self._gear_count} gear_count"

class Bus(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, seats: int) -> None:
        super().__init__(make, model, year, color)
        self._seats: int = seats #кол-во мест
    def open_doors(self) -> str:
        return "Bus doors opened."
    def get_info(self):
        return f" {self.make} {self.model} {self.year} {self.color} with {self._seats} seats"

class Van(Vehicle): #фургон
    def __init__(self, make: str, model: str, year: int, color: str, cargo_capacity: int) -> None:
        super().__init__(make, model, year, color)
        self._cargo_capacity: int = cargo_capacity #грузоподьемность
    def load_cargo(self, weight: int) -> Union[str, None]:
        try:
            if weight <= 0:
                raise VehicleError("Weight must be greater than zero.")
            if weight <= self._cargo_capacity:
                return f"Loaded {weight} kg of cargo."
            else:
                raise VehicleError("Cargo exceeds capacity!")
        except VehicleError as e:
            return str(e)
    def get_info(self):
        return f" {self.make} {self.model} {self.year} {self.color} with {self._cargo_capacity} cargo_capacity"

