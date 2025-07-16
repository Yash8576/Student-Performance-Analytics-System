import pandas as pd

# Load data
students = pd.read_csv('../data/students.csv')
grades = pd.read_csv('../data/grades_clean.csv')
attendance = pd.read_csv('../data/attendance_clean.csv')

# Merge all datasets
merged = pd.merge(grades, attendance, on=['StudentID', 'CourseCode', 'Semester'])
final_data = pd.merge(merged, students, on='StudentID')

# Save to Excel for Power BI import
final_data.to_excel('../reports/summary_metrics.xlsx', index=False)
print("Merged data saved to Excel.")