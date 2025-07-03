import pandas as pd
import numpy as np

# Settings  
NUM_STUDENTS = 1000
NUM_MAJOR_SUBJECTS = 4  # Number of primary subjects

# Sample first and last names for realism
first_names = [
    "Aiden", "Olivia", "Ethan", "Sophia", "Liam", "Emma", "Noah", "Ava", "Mason", "Isabella", 
    "Lucas", "Mia", "Caden", "Charlotte", "Elijah", "Amelia", "Oliver", "Harper", "Jacob", "Evelyn"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", 
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", 
    "Martin", "Lee"
]

# Create student names
rng = np.random.default_rng()
firsts = rng.choice(first_names, NUM_STUDENTS)
lasts = rng.choice(last_names, NUM_STUDENTS)
names = [f"{first} {last}" for first, last in zip(firsts, lasts)]

# Other columns
student_ids = [f"S{1001 + i}" for i in range(NUM_STUDENTS)]
ages = rng.integers(18, 25, NUM_STUDENTS)
genders = rng.choice(['Male', 'Female', 'Other'], NUM_STUDENTS, p=[0.48, 0.48, 0.04])
years = rng.choice(['First', 'Second', 'Third', 'Fourth'], NUM_STUDENTS)
departments = rng.choice(['Engineering', 'Business', 'Arts', 'Science'], NUM_STUDENTS)
iq_scores = rng.normal(110, 15, NUM_STUDENTS).astype(int)
daily_study_hours = rng.uniform(1, 6, NUM_STUDENTS).round(1)

# Build DataFrame
df = pd.DataFrame({
    "StudentID": student_ids,
    "Name": names,
    "Gender": genders,
    "Age": ages,
    "Year": years,
    "Department": departments,
    "IQ_Score": iq_scores,
    "Daily_Study_Hours": daily_study_hours,
})

# Add major subject grades
letter_grades = ['A', 'B', 'C', 'D', 'E', 'F']
for subj_num in range(1, NUM_MAJOR_SUBJECTS + 1):
    grade_col = f"MajorSubject{subj_num}_Grade"
    df[grade_col] = rng.choice(
        letter_grades, NUM_STUDENTS, p=[0.18, 0.25, 0.24, 0.17, 0.10, 0.06]
    )

# Sports involvement
df["Sports_Involvement"] = rng.choice(['Yes', 'No'], NUM_STUDENTS, p=[0.4, 0.6])

# Expected result column
df["Expected_Result"] = ((df["Daily_Study_Hours"] / df["IQ_Score"]) * 100).round(2)

# Output
df.to_csv("college_student_data.csv", index=False)
print("College student data CSV with real names generated successfully.")