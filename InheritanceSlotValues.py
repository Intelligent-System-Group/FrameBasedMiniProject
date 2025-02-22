class PassengerCar:
    """Superclass: Passenger car - defines general passenger car attributes."""
    engine_type_choices = ["In-line 4 cylinder", "V6"]
    drivetrain_type_choices = ["Rear wheel drive", "Front wheel drive", "Four wheel drive"]
    transmission_type_choices = ["5-speed manual", "4-speed automatic"]

    def __init__(self, engine_type=None, horsepower=None, drivetrain_type=None, transmission_type=None, fuel_consumption_mpg=None, seating_capacity=None):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.drivetrain_type = drivetrain_type
        self.transmission_type = transmission_type
        self.fuel_consumption_mpg = fuel_consumption_mpg
        self.seating_capacity = seating_capacity

    def __str__(self):
        return f"Passenger Car (Generic):\n" + \
               f"  Engine Type: {self.engine_type}\n" + \
               f"  Horsepower: {self.horsepower}\n" + \
               f"  Drivetrain: {self.drivetrain_type}\n" + \
               f"  Transmission: {self.transmission_type}\n" + \
               f"  Fuel Consumption (mpg): {self.fuel_consumption_mpg}\n" + \
               f"  Seating Capacity: {self.seating_capacity}\n"


class Mazda(PassengerCar):
    """Class: Mazda - inherits from PassengerCar, adds Mazda-specific attributes."""
    country_of_manufacture = "Japan"  # Class-level attribute, common to all Mazdas

    def __init__(self, engine_type=None, horsepower=None, drivetrain_type=None, transmission_type=None, fuel_consumption_mpg=None, seating_capacity=None):
        super().__init__(engine_type, horsepower, drivetrain_type, transmission_type, fuel_consumption_mpg, seating_capacity) # Inherit from PassengerCar

    def __str__(self):
        base_str = super().__str__().replace("Generic", "Mazda") # Reuse base string and modify
        return base_str + f"  Country of Manufacture: {self.country_of_manufacture}\n"


class Mazda626(Mazda):
    """Class: Mazda 626 - inherits from Mazda, adds Mazda 626 specific attributes."""
    model = "626" # Class-level attribute

    def __init__(self, engine_type=None, horsepower=125, drivetrain_type=None, transmission_type=None, fuel_consumption_mpg=22, seating_capacity=5, country_of_manufacture="Japan"):
        # Note: Some defaults are set based on the image for Mazda 626
        super().__init__(engine_type, horsepower, drivetrain_type, transmission_type, fuel_consumption_mpg, seating_capacity) # Inherit from Mazda
        # We could override country_of_manufacture here if needed, but it's already "Japan" from Mazda class

    def __str__(self):
        base_str = super().__str__().replace("Mazda", "Mazda 626") # Reuse and modify
        return base_str + f"  Model: {self.model}\n"


class MazdaDR1216(Mazda626):
    """Instance (represented as a class for frame-based system): Mazda DR-1216 - inherits from Mazda 626, adds instance-specific attributes."""
    instance_model = "DR-1216" # To distinguish it as a specific model instance

    def __init__(self, engine_type="In-line 4 cylinder", horsepower=125, drivetrain_type="Front wheel drive", transmission_type="4-speed automatic", fuel_consumption_mpg=28, seating_capacity=5, country_of_manufacture="Japan", colour=None, owner="None"):
        # Note:  Defaults and specific values based on the "INSTANCE" frame in the image
        super().__init__(engine_type, horsepower, drivetrain_type, transmission_type, fuel_consumption_mpg, seating_capacity, country_of_manufacture) # Inherit from Mazda 626
        self.colour = colour
        self.owner = owner

    def __str__(self):
        base_str = super().__str__().replace("Mazda 626", "Mazda DR-1216 (Instance)") # Modify for instance
        return base_str + \
               f"  Model (Instance): {self.instance_model}\n" + \
               f"  Colour: {self.colour}\n" + \
               f"  Owner: {self.owner}\n"


# Create instances and print them
generic_car = PassengerCar(engine_type="V6", drivetrain_type="Rear wheel drive", horsepower=80, transmission_type="5-speed manual", fuel_consumption_mpg=15, seating_capacity=4)
print(generic_car)

mazda_car = Mazda(engine_type="Rotary") # Country is already set in class, but can override
print(mazda_car)

mazda_626_car = Mazda626(transmission_type="5-speed manual", drivetrain_type="Front wheel drive") #  Overrides transmission from default in Mazda class
print(mazda_626_car)

mazda_dr_1216_car = MazdaDR1216(colour="Sage Green Metallic", owner="Mr Black") # Instance with specific colour
print(mazda_dr_1216_car)