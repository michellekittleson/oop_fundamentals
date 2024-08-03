'''
Task 1: Vehicle Registration System

Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. The, create a few instances of Vehicle and demonstrate changing the owner.

'''

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner

vehicles = {}

def register_vehicle(reg_num, type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Vehicle with registration number {reg_num} registered.")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner for vehicle {reg_num}.")
    else:
        print("Vehicle not found.")

while True:
    action = input("Would you like to [register] a vehicle or [update] the owner of a vehicle? (Type 'exit' to exit the program.)")
    if action == 'exit':
        break
    try:
        if action == 'register':
            reg_num = input("Enter registration number: ")
            type = input("Enter vehicle type: ")
            owner = input("Enter owner name: ")
            register_vehicle(reg_num, type, owner)
        elif action == 'update':
            reg_num = input("Enter registration number: ")
            new_owner = input("Enter the name of the new owner: ")
            update_vehicle_owner(reg_num, new_owner)
    except Exception as e:
        print(f"An error occurred: {e}")

print("System closed.")

'''
Demonstration from the Terminal:

Would you like to [register] a vehicle or [update] the owner of a vehicle? (Type 'exit' to exit the program.)register
Enter registration number: 1234
Enter vehicle type: Honda
Enter owner name: Patches
Vehicle with registration number 1234 registered.
Would you like to [register] a vehicle or [update] the owner of a vehicle? (Type 'exit' to exit the program.)update
Enter registration number: 1234
Enter the name of the new owner: Patrick
Updated owner for vehicle 1234.
Would you like to [register] a vehicle or [update] the owner of a vehicle? (Type 'exit' to exit the program.)exit
System closed.

'''