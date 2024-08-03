'''
Task 2: Event Management System Enhancement

Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

'''

class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self):
        participant = input("Enter the name of the participant: ")
        self.participants += 1
        return self.participants
        print(f"{participant} has been added. ")
    
    def get_participant_count(self):
        print(f"There are now {self.participants} participants. ")

event = Event("Baking Class", "08/02/2024", 12)

while True:
    action = input("\nWould you like to [add] a participant or get the current participant [count]? (Type 'exit' to exit the program.) \n")
    if action == 'exit':
        break

    try:
        if action == 'add':
            event.add_participant()
        elif action == 'count':
            event.get_participant_count()

    except Exception as e:
        print(f"An error occurred: {e}")
    