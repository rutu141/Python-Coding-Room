# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1+name2
#print(name)
length=len(name)
count_true=0
count_love=0

for i in range(length):
    #print(name[i])
    if name[i] =="t" or name[i]=="r" or name[i]=="u" or name[i]=="e" or name[i]=="T" or name[i]=="R" or name[i]=="U" or name[i]=="E":
        count_true=count_true+1
    if name[i]=="l" or name[i]=="o" or name[i]=="v" or name[i]=="e" or name[i]=="L" or name[i]=="O" or name[i]=="V" or name[i]=="E":
        count_love=count_love+1  
count_true=str(count_true)
count_love=str(count_love)
score=count_true+count_love
#print(score)
score=int(score)
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

