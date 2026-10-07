import pandas as pd
d={'Name':["Amit","Priya","Rahul","Sneha","Vikas","Neha","Rohan","Pooja"],'Age':[21,22,20,23,21,22,24,20],'Department':["IT","HR","IT","Finance","HR","IT","Finance","IT"],'City':["Pune","Mumbai","Nashik","Pune","Bhusawal","Mumbai","Pune","Nashik"],'Salary':[25000,28000,22000,32000,27000,30000,35000,24000]}
df=pd.DataFrame(d)
print(df)
print("=======Display Only Name Column=======")
df1=df.iloc[:,0]
print(df1)

print("=======Display Name & Salary Column=======")
print(df[['Name','Salary']])

print("=======Display Row At Index 3=======")
ind=df.loc[3]
print(ind)

print("=======Display Row At Position 4=======")
ind2=df.iloc[4]
print(ind2)

print("=======Display Name,Department,Salary=======")
print(df.loc[2,['Name','Department','Salary']])

print("=======Display Frist Five Rows=======")
print(df.head(5))

print("=======Display Rows From Index 2 To 5=======")
print(df.loc[2:5])

print("=======Display Last Three Rows======")
print(df.loc[5:])

print("=======Display Row 1 To 6 And Only Columns Name,Age,City=======")
print(df.loc[1:6,['Name','Age','City']])

print("=======Display Every Alternate Row=======")
print(df.iloc[::2])

print("=======Display The First 4 Rows And First 3 Columns=======")
print(df.loc[:4,['Name','Age','Department']])
print(df.iloc[:4,:3])

print("=======Display All Employees Salary Greater Than 2500=======")
emp_g=(df[df['Salary']>25000])
print(emp_g)

print("=======Display Employee Age Is Equal To 22=======")
emp_a=(df[df['Age']==22])
print(emp_a)

print("=======Display Employees From The IT Department=======")
emp_d=(df[df['Department']=="IT"])
print(emp_d)

print("=======Display Employees Live Pune=======")
emp_c=(df[df['City']=="Pune"])
print(emp_c)

print("=======Employee Salary Between 25K & 30K=======")
emp_s=(df[(df['Salary']>25000)&(df['Salary']<30000)])
print(emp_s)

print("=======Split DataFrame Into Two Parts=======")
df1=df.iloc[:4]
df2=df.iloc[4:]
print("First Data Frame")
print(df1)
print("Second Data Frame")
print(df2)

print("=======Crate Two Data Frame Name,Age,Department=======")
df3=df.iloc[:,0:3]
df4=df.iloc[:,3:5]
print("Data Frame First Name,Age,Department")
print(df3)
print("Data Frame Second City,Salary")
print(df4)

print("=======Department Based Splitting=======")
it=(df[df['Department']=="IT"])
print("IT Employees")
print(it)
hr=(df[df['Department']=="HR"])
print("HR Employees")
print(hr)
finance=(df[df['Department']=="Finance"])
print("Finance Employee")
print(finance)

print("=======Challenge Task=======")
d=df[(df['Department']=="IT")&(df['Salary']>24000)][['Name','City','Salary']]
print(d)




