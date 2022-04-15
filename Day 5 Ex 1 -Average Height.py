# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#print(n+1)
avg=0
for sum_h in student_heights:
   # print(sum_h)
    avg=sum_h+avg
print (round(avg/(n+1)))


#Write your code below this row 👇




