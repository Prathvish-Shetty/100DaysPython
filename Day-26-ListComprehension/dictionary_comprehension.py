# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (index, row) in df.iterrows()}

import random

import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}

print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 35}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(f"{key} : {value}")

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a dataframe
for (key, value) in student_data_frame.items():
    print(f"{key} : {value}")

# loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    # print(f"{index} : {row}")
    # print(row.student)
    if row.student == "Angela":
        print(row.score)