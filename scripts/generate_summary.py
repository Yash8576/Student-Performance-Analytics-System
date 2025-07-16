import pandas as pd

df = pd.read_excel('../reports/summary_metrics.xlsx')

# Generate GPA-like metric
df['PerformanceScore'] = (df['Grade'] * 0.7) + (df['AttendancePercentage'] * 0.3)

summary = df.groupby(['Department']).agg({
    'PerformanceScore': 'mean',
    'StudentID': 'nunique'
}).rename(columns={
    'PerformanceScore': 'AvgPerformanceScore',
    'StudentID': 'TotalStudents'
})

print(summary)