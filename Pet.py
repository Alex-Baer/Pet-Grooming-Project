# This program would be useful for pet groomers who are in need of a more organized way of creating schedules,
# an easier for their customers to schedule appointments and keep records


import csv
from Collections import *

# the "Pet" class represents a pet (either a cat or dog) and their attributes
# the attribute "name" represents a string of the name of the pet, the attribute "temperament" represents a string of
# what climates the pets live in, the attribute "weight" represents the weight of the pet,
# and lastly the attribute "groom_log" represents a list of the history of past groomings done to the pet


class Pet:
    all_pets = BinarySearchTree()

    def __init__(self, name: str, temperament, weight):
        self.name = name
        self.temperament = temperament
        self.weight = weight
        self.groom_log = Stack()
        Pet.all_pets.insert(self)

    def print_groom_history(self, n: int):
        output = ""
        counter = 0
        temp_node = self.groom_log.top_node
        while temp_node is not None and counter < n:
            output += temp_node.__repr__() + "\n"
            temp_node = temp_node.next_node
            counter += 1
        return output

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            # the list 'pets' become a list of every row in the csv file - each row is stored in as one object in 'pets'
            pets = list(reader)
        for pet in pets:
            # constructor that converts the csv rows in the list 'pets' and turns them into 'Pet' objects
            Pet(
                # 'Pet' class constructor parameters
                name=pet.get('Name'),
                temperament=pet.get('Temperament'),
                weight=pet.get('Minimum Weight'),
            )

    def __repr__(self):
        return f' - Pet Name: {self.name} - Weight: {self.weight}'


# The PetGroomerAppointment class represents individual appointments for pets (represented by the "Pet" class)
# to get professionally groomed and the attributes relating to said appointments
# The attribute "pet_name" is a string representing the name of the pet being groomed
# which can be used to find the pet object using the "get(self, name, node)" function.
# The attribute "groom_date" represents the planned time for the grooming appointment to take place, and description
# represents a summary of what specifically the owner wants to be done to the dog
class PetGroomerAppointment:
    groom_queue = Queue()

    def __init__(self, pet_name: str, groom_date: str, description: str):
        self.groom_date = groom_date
        self.pet_name = pet_name
        self.description = description
        self.is_completed = False
        PetGroomerAppointment.groom_queue.push(self)
        Pet.all_pets.get(self.pet_name, Pet.all_pets.root).groom_log.push(self)

    @classmethod
    def get_front(cls):
        return PetGroomerAppointment.groom_queue.front_node.data

    def groom(self):
        PetGroomerAppointment.get_front().is_completed = True
        PetGroomerAppointment.groom_queue.pop()

    def __repr__(self):
        return f' - Grooming Appointment: Date: {self.groom_date} - Pet Name: {self.pet_name} ' \
               f'- Grooming Description: {self.description} - ' \
               f'Has your grooming appointment been completed?: {self.is_completed}'
