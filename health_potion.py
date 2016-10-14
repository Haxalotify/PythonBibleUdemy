import random

health = 50

#creating a difficulty, choose between 1, 2, 3. Higher the difficulty
#the less health potion_health will give
difficulty = 1

#int, converts to an integer instead of float known as casting
potion_health = int(random.randint(25, 50) / difficulty)

#using a potion to increase player health
health = health + potion_health
print(health)
