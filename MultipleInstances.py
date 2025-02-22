class ElectricVehicle:
    def __init__(self, motor, battery_type):
        self.motor = motor
        self.battery_type = battery_type

class SolarVehicle:
    def __init__(self, solar_panel_type, solar_cell_material):
        self.solar_panel_type = solar_panel_type
        self.solar_cell_material = solar_cell_material

class MuscleVehicle:
    def __init__(self, number_of_wheels, pedalling_manpower):
        self.number_of_wheels = number_of_wheels
        self.pedalling_manpower = pedalling_manpower

class MuscleSolarElectricVehicle(ElectricVehicle, SolarVehicle, MuscleVehicle):
    def __init__(self, motor, battery_type, solar_panel_type, solar_cell_material,
                 number_of_wheels, pedalling_manpower, weight, top_speed):
        ElectricVehicle.__init__(self, motor, battery_type)
        SolarVehicle.__init__(self, solar_panel_type, solar_cell_material)
        MuscleVehicle.__init__(self, number_of_wheels, pedalling_manpower)
        
        self.weight = weight
        self.top_speed = top_speed

    def display_info(self):
        print(f"Motor: {self.motor}")
        print(f"Battery Type: {self.battery_type}")
        print(f"Solar Panel Type: {self.solar_panel_type}")
        print(f"Solar Cell Material: {self.solar_cell_material}")
        print(f"Number of Wheels: {self.number_of_wheels}")
        print(f"Pedalling Manpower: {self.pedalling_manpower}")
        print(f"Weight: {self.weight} kg")
        print(f"Top Speed: {self.top_speed} km/h")

DidikMuscleCar = MuscleSolarElectricVehicle(
    motor="24V DC",
    battery_type="Sealed lead acid",
    solar_panel_type="BP140",
    solar_cell_material="Crystalline silicon",
    number_of_wheels=4,
    pedalling_manpower=2,
    weight=60,
    top_speed=35
)

DidikMuscleCar.display_info()

