student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
   
  
    if student_scores[name] in range(91,101):
        student_grades[name]="Outstanding"
    if student_scores[name] in range(81,91):
        student_grades[name]="Exceeds Expectations"
    if student_scores[name] in range(71,81):
        student_grades[name]="Acceptable"
    if student_scores[name]==70 or student_scores[name]<70:
        student_grades[name]="Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)