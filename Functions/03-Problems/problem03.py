def get_subject_grade(subject_name):
   subject_grade = int(input(f"Enter grade for {subject_name}: "))
   """ print(f"Grade for {subject_name}: {subject_grade}") """
   return subject_grade 

subjects_names = ["Math", "Science", "History", "Art"]
grades_list = []
 

for subject in subjects_names:
   grade = get_subject_grade(subject)
   grades_list.append(grade)

average_grade = sum(grades_list) / len(grades_list)

print(f"Grades entered: {grades_list}")
print(f"Average grade: {average_grade}")