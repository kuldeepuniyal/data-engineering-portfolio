employees = [
    {"name": "Kuldeep", "dept": "Analytics", "salary": 75000, "city": "Ghaziabad"},
    {"name": "Amit", "dept": "Engineering", "salary": 82000, "city": "Delhi"},
    {"name": "Priya", "dept": "Analytics", "salary": 69000, "city": "Mumbai"},
    {"name": "Rahul", "dept": "Engineering", "salary": 91000, "city": "Delhi"},
    {"name": "Neha", "dept": "Marketing", "salary": 65000, "city": "Ghaziabad"},
    {"name": "Sita", "dept": "Analytics", "salary": 78000, "city": "Mumbai"},
    {"name": "Vikram", "dept": "Engineering", "salary": 95000, "city": "Bangalore"},
    {"name": "Kavita", "dept": "Marketing", "salary": 71000, "city": "Delhi"},
    {"name": "Raj", "dept": "Analytics", "salary": 69000, "city": "Ghaziabad"},
    {"name": "Meera", "dept": "Engineering", "salary": 88000, "city": "Mumbai"},
]

#Filter: Get all employees from the "Analytics" department. Print their names.
emp_name=[n["name"] for n in employees if n["dept"]=="Analytics"]
print(emp_name)
#Average salary per department: Calculate and print the average salary for each department.
dept_name=set(emp["dept"] for emp in employees)

for dept in dept_name:
    dept_salaries=[emp["salary"] for emp  in employees if emp["dept"]==dept]
    avg_salary=sum(dept_salaries)/len(dept_salaries)

    print(f"{dept}:avg salary={avg_salary}")

#Top earners: Find the top 3 highest-paid employees. Print their name and salary.
sorted_employees=sorted(employees,key=lambda emp: emp["salary"],reverse=True)
top3=sorted_employees[0:3]
for emp in top3:
    print(f"{emp['name']}:{emp['salary']}")


#Unique cities: Print all unique cities and how many there are.
cities=set(emp['city'] for emp in employees)
cities2=[emp['city'] for emp in employees]
print(cities)
print(len(cities))

#City-department matrix: For each city, show which departments have employees there
city_name=set(emp["city"] for emp in employees)

for city in city_name:
    dept_name=set(emp["dept"] for emp  in employees if emp["city"]==city)
    print(f"{city}:{','.join(dept_name)}")
#Deduplication: The salary list [75000, 82000, 69000, 91000, 65000, 78000, 95000, 71000, 69000, 88000] has a duplicate. Find which salary appears more than once and which employees share it.
salaries = [emp["salary"] for emp in employees]

for s in salaries:
    if salaries.count(s) > 1:
        name=[emp['name'] for emp in employees if emp['salary']==s]
        print(name)
        break

#Bonus challenge: Calculate the average salary per department using a dict comprehension in a single line.
dept_names = set(emp["dept"] for emp in employees)

avg_by_dept = {
    dept: sum(emp["salary"] for emp in employees if emp["dept"] == dept) / len([emp for emp in employees if emp["dept"] == dept])
    for dept in set(emp["dept"] for emp in employees)
}
print(avg_by_dept)