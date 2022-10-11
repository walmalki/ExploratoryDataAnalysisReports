import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_excel('hr_employee_attrition.xlsx', sheet_name='HR Employee Attrition')
profile = ProfileReport(df, title='HR Employee Attrition')
profile.to_file('index.html')
