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

class Scooter(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, battery_capacity: int) -> None:
        super().__init__(make, model, year, color)
        self._battery_capacity: int = battery_capacity #емкость аккумулятора
    def charge_battery(self) -> str:
        return "Scooter battery charged."
    def get_info(self):
        return f" {self.make} {self.model} {self.year} {self.color} with {self._battery_capacity} battery_capacity"

class Train(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, car_count: int) -> None:
        super().__init__(make, model, year, color)
        self._car_count: int = car_count #кол - во вагонов
    def whistle(self) -> str:
        return "Choo choo!"
    def get_info(self):
        return f" {self.make} {self.model} {self.year} {self.color} with {self._car_count} car_count"

class VehicleManager:
    def __init__(self) -> None:
        self.vehicles: List[Vehicle] = []

    def create_vehicle(self, vehicle: Vehicle) -> str:
        self.vehicles.append(vehicle)
        return f"{vehicle.make} {vehicle.model} added"

    def read_vehicles(self) -> List[str]:
        return [f"{v.year} {v.make} {v.model} ({v.color})" for v in self.vehicles] #генерптор списка

    def update_vehicle(self, index: int, make: Optional[str] = None, model: Optional[str] = None,
                       year: Optional[int] = None, color: Optional[str] = None,
                       payload_capacity: Optional[int] = None) -> str:
        try:
            vehicle = self.vehicles[index]
            if make:
                vehicle.make = make
            if model:
                vehicle.model = model
            if year:
                vehicle.year = year
            if color:
                vehicle.color = color
            if payload_capacity is not None and isinstance(vehicle, Truck):
                vehicle.payload_capacity = payload_capacity
            return f"Vehicle at index {index} updated"
        except IndexError:
            return "Vehicle not found"

    def delete_vehicle(self, index: int) -> str:
        try:
            removed_vehicle = self.vehicles.pop(index)
            return f"{removed_vehicle.make} {removed_vehicle.model} removed."
        except IndexError:
            return "Vehicle not found"

def main() -> None:
    from JsonAndXml import load_vehicles_from_json, load_vehicles_from_xml, save_vehicles_to_json, save_vehicles_to_xml

    # Создание списка транспортных средств
    vehicles = [
        Car(make="Toyota", model="Camry", year=2020, color="White", doors=4),
        Motorcycle(make="Yamaha", model="YZF-R3", year=2021, color="Black", engine_cc=800)
    ]

    # Сохранение в JSON
    save_vehicles_to_json(vehicles, 'vehicles.json')

    # Сохранение в XML
    save_vehicles_to_xml(vehicles, 'vehicles.xml')

    # Загрузка из JSON
    loaded_vehicles_json = load_vehicles_from_json("vehicles.json")
    print("Loaded from JSON:")
    for vehicle in loaded_vehicles_json:
        print(vehicle.get_info())

    # Загрузка из XML
    loaded_vehicles_xml = load_vehicles_from_xml("vehicles.xml")
    print("\nLoaded from XML:")
    for vehicle in loaded_vehicles_xml:
        print(vehicle.get_info())

if __name__ == "__main__":
    main()