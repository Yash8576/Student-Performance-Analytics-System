import pandas as pd

# Load raw data
grades = pd.read_csv('../data/grades.csv')
attendance = pd.read_csv('../data/attendance.csv')

# Clean missing values (mock behavior)
grades.fillna(0, inplace=True)
attendance.fillna(0, inplace=True)

# Save cleaned versions
grades.to_csv('../data/grades_clean.csv', index=False)
attendance.to_csv('../data/attendance_clean.csv', index=False)
print("Data cleaned and saved.")