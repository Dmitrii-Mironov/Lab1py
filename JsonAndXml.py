import json
import xml.etree.ElementTree as ET
from Vehicle import Car
from Vehicle import Motorcycle
from Vehicle import Truck
from Vehicle import Bus
from Vehicle import Bicycle
from Vehicle import Van
from Vehicle import Train

def create_vehicle(data):
    vehicle_type = data.pop('type')
    if vehicle_type == 'Car':
        return Car(**data)
    elif vehicle_type == 'Motorcycle':
        return Motorcycle(**data)
    elif vehicle_type == 'Truck':
        return Truck(**data)
    elif vehicle_type == 'Bus':
        return Bus(**data)
    elif vehicle_type == 'Bicycle':
        return Bicycle(**data)
    elif vehicle_type == 'Van':
        return Van(**data)
    elif vehicle_type == 'Train':
        return Train(**data)
    else:
        raise ValueError(f"Unknown vehicle type: {vehicle_type}")

def write_json(filename, vehicles):
    with open(filename, 'w') as f:
        json.dump([vehicle.__dict__ for vehicle in vehicles], f, indent=4)

def read_json(filename):
    with open(filename, 'r') as f:
        vehicles_data = json.load(f)
        return [create_vehicle(data) for data in vehicles_data]


def write_xml(filename, vehicles):
    root = ET.Element("vehicles")
    for vehicle in vehicles:
        vehicle_elem = ET.SubElement(root, vehicle.__class__.__name__)
        for key, value in vehicle.__dict__.items():
            ET.SubElement(vehicle_elem, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    vehicles = []

    for vehicle_elem in root:
        vehicle_data = {child.tag: child.text for child in vehicle_elem}
        vehicles.append(create_vehicle(vehicle_data))

    return vehicles

def load_vehicles_from_json(filename):
    return read_json(filename)

def load_vehicles_from_xml(filename):
    return read_xml(filename)

def save_vehicles_to_json(vehicles, filename):
    write_json(filename, vehicles)

def save_vehicles_to_xml(vehicles, filename):
    write_xml(filename, vehicles)
