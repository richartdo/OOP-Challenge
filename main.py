from pet import Pet
import random

pets_list = ["Zuzu", "Pikachu", "Nimbus", "Kitty", "Maam"]

chosen_name = random.choice(pets_list)

pet = Pet(chosen_name)

print(f"Your pet is: {pet.name}")

pet.eat()
pet.play()
pet.sleep()
pet.train("roll over")
pet.train("play dead")
pet.get_status()



