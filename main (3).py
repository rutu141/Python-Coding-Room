
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(len(names))
random_index=random.randrange(len(names))
#print(random_index)
random_name=names[random_index]
#print(random_name)
print(random_name+" is going to buy the meal today!")