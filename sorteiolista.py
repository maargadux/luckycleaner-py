import random
name1 = str(input("Name 1: "))
name2 = str(input("Name 2: "))
name3 = str(input("Name 3: "))
name4 = str(input("Name 4: "))
list = [name1, name2, name3, name4]
choics = random.choice(list)
print("the classmate who will erase the board is: ", choics)