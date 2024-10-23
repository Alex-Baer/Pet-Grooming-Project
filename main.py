from Pet import *
from Collections import *

Pet.instantiate_from_csv('Dogs.csv')
Pet.instantiate_from_csv('Cats.csv')
print("Our Current Grooming Schedule: ")
print(PetGroomerAppointment.groom_queue)
print("Has your pet been groomed with us before? (Y or N): ")
the_input = input()
# it repeats until the user inputs 'Q' in response to the following prompt: 'Has your pet been groomed
# with us before? (Y or N) or press Q to quit: ' using the variable 'the_input' to stop the while loop
# If the user inputs 'Y' then a list will show up of pets, and they will choose theirs by inputting their pet's name and
# the UI will show them a list of their pet's history. Then the UI will ask them if their pet is first in line to be
# groomed in the grooming schedule or if they want to make an appointment for their pet. If the input is 'A' the UI will
# collect the attributes of a 'PetGroomerAppointment' object through questions and user input making their pet a
# grooming appointment and putting said appointment in their pet's 'grooming_log'. If they input 'B' then the UI will
# call the 'pop()' and the 'peek()' functions on the 'grooming_queue' making sure their pet is first in the
# grooming_queue and removing their pet who was first in the grooming_queue from the grooming_queue.
# If they inputted 'N' for the first question they would be asked questions asking for the user to input the parameters
# for a Pet object which will then be stored in the list 'all_pets' the UI will then collect the attributes of a
# 'PetGroomerAppointment' object through questions and user input making their pet a grooming appointment
# and putting said appointment in their pet's 'grooming_log'.
while not(the_input.lower() == "q"):
    the_pet = None
    the_appointment = None
    if the_input.lower() == "y":
        Pet.all_pets.print_tree()
        print(" ")
        print("Enter your pets name from the alphabetical list above:")
        name = input()
        try:
            Pet.all_pets.get(name, Pet.all_pets.root)
        except:
            print("Your pet is not in our records please try again:")
        else:
            the_pet = Pet.all_pets.get(name, Pet.all_pets.root)
            print("Your pet's past/upcoming appointments: ")
            print(" ")
            print(the_pet.groom_log)
            print(" ")
            print("If you trying to make a new appointment for your pet enter the letter 'A' "
                  "if you are trying to check in your pet to be groomed and "
                  "your pet is first in line on our grooming schedule enter 'B'")
            the_answer = input()
            if the_answer.lower() == "a":
                print(f'At what date would you like your grooming appointment for your pet {the_pet.name} to occur?')
                the_date = input()
                print(f'What specifically would you like done to your pet {the_pet.name} during the grooming Session?')
                the_description = input()
                the_appointment = PetGroomerAppointment(the_pet.name, the_date, the_description)
                print("Thank you for the appointment we have successfully Scheduled it")
            elif the_answer.lower() == "b":
                if PetGroomerAppointment.groom_queue.front_node is None:
                    print("Hmm, it doesn't seem as though we have a grooming schedule yet. "
                          "Sign your pet up for a grooming session to start our schedule.")
                elif PetGroomerAppointment.groom_queue.front_node.data.pet_name == the_pet.name:
                    the_pet.groom_log.peek().is_completed = True
                    PetGroomerAppointment.groom_queue.pop()
                    print(" ")
                    print("Thank you letting us groom your pet, your pet is going to be ready to be picked up from its "
                          "grooming appointment in an hour")
                    print(" ")
                else:
                    print("Sorry your pet is not first in line on our schedule to be groomed yet please try again when "
                          "your pet is first in line")
    elif the_input.lower() == "n":
        print("Enter your pet's name: ")
        the_name = input()
        print("Enter some of your pet's qualities: ")
        the_temperament = input()
        print("Enter your pet's weight: ")
        the_weight = input()
        the_pet = Pet(the_name, the_temperament, the_weight)
        print(" ")
        print("Your pet has successfully been entered into our data records!")
        print(" ")
        print(f'At what date would you like your grooming appointment for your pet {the_pet.name} to occur?')
        the_date = input()
        print(f'What specifically would you like done to your pet {the_pet.name} during the grooming Session?')
        the_description = input()
        the_appointment = PetGroomerAppointment(the_pet.name, the_date, the_description)
        print("Thank you for the appointment we have successfully Scheduled it")
    print(" ")
    print("Our Current Grooming Schedule: ")
    print(" ")
    print(PetGroomerAppointment.groom_queue)
    print(" ")
    print("Has your pet been groomed with us before? (Y or N) or press Q to quit: ")
    the_input = input().lower()
print("Thank you for choosing The Yams Pet grooming and company you better choose us next time!")
