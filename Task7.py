import pandas as pd 

df = pd.DataFrame ({

    'name': ['Arun', 'Akhil', 'Charan', 'Neeraj', 'Vishu', 'Harish', 'Ganesh', 'kalyan'],
    'department': ['IT', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'salary': [92000, 52000, 60000, 75000, 50000, 80000, 90000, 47000]
})

percentage = df['salary'].quantile(0.75)
print(percentage)
high_salary = df[df['salary'] > percentage]
print(high_salary)
