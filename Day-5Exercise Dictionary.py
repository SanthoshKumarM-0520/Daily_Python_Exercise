"""You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
Hint"""
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for i in student_scores:
  if student_scores[i]>90 and student_scores[i]<=100:
    student_grades[i]="Outstanding"
  elif student_scores[i]>80 and student_scores[i]<=90:
    student_grades[i]="Exceeds Expectations"
  elif student_scores[i]>70 and student_scores[i]<=80:
    student_grades[i]="Acceptable"
  else:
    student_grades[i]="Fail"
print(student_grades)    
