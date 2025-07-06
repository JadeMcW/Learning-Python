def get_subject_grade(subject_name):
   subject_grade = int(input(f"Enter grade for {subject_name}: "))
   print(f"Grade for {subject_name}: {subject_grade}")
   return subject_grade 

get_subject_grade("Math")
