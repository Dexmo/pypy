class Battery:
    """ Simple class with battery model"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has battery with " + str(self.battery_size) + "kWh.")


my_battery = Battery(battery_size=60)
my_battery.describe_battery()