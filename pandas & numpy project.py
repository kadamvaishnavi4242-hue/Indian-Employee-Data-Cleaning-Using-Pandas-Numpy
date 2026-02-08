import numpy as np
import pandas as pd
#read the data
df=pd.read_csv(r"C:\Users\kadam\Downloads\indian_employee_data (1) - indian_employee_data (1).csv",encoding="latin1")
print(df.head(5))
#find a missing value
print("missing values in each column")
print(df.isnull().sum())
#numeric conversion
df["Salary (INR)"]=pd.to_numeric(df["Salary (INR)"],errors="coerce")
df["Performance Rating"]=pd.to_numeric(df["Performance Rating"],errors="coerce")
#handle the missing values
df["Salary (INR)"].fillna(df["Salary (INR)"].mean(),inplace=True)
df["Performance Rating"].fillna(df["Performance Rating"].median(),inplace=True)
print(df)
#remove duplicates
print(df.drop_duplicates(inplace=True))
#find the nan values
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(numeric_only=True))
print(df)
#replace negative salary by mean
df["Salary (INR)"]=np.where(df["Salary (INR)"]<0,
                            df["Salary (INR)"].mean(),
                             df["Salary (INR)"])

salary_mean=df["Salary (INR)"].mean()
salary_std=df["Salary (INR)"].std()
lower_bound=salary_mean-(3*salary_std)
upper_bound=salary_mean+(3*salary_std)
print(lower_bound)
print(upper_bound)
#removve rows where salary is too high or too low
df=df[(df["Salary (INR)"]>=lower_bound) &(df["Salary (INR)"]<=upper_bound)]
print(df)
df.to_csv("cleaned_indian_employee data.csv",index=False)
print("data cleaning completed!")
