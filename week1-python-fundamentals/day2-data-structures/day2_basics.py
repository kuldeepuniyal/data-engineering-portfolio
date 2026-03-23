# Employee data — list of dicts (think of it as a table)
employees = [
    {"name": "Kuldeep", "dept": "Analytics", "salary": 75000},
    {"name": "Amit", "dept": "Engineering", "salary": 82000},
    {"name": "Priya", "dept": "Analytics", "salary": 69000},
    {"name": "Rahul", "dept": "Engineering", "salary": 91000},
    {"name": "Neha", "dept": "Marketing", "salary": 65000},
    {"name": "Sita", "dept": "Analytics", "salary": 78000},
]

# 1. Get all unique departments — like SELECT DISTINCT dept
departments=set(emp["dept"] for emp in employees)
print(f"departments:{departments}")

# 2. Filter by department — like WHERE dept = 'Analytics'
analytics_team = [emp for emp in employees if emp["dept"] == "Analytics"]
print(f"Analytics team: {analytics_team}")

# 3. Get all salaries — like SELECT salary FROM employees
all_salaries = [emp["salary"] for emp in employees]
print(f"Average salary: {sum(all_salaries) / len(all_salaries)}")

# 4. Find highest paid — like ORDER BY salary DESC LIMIT 1
highest_paid = max(employees, key=lambda emp: emp["salary"])
print(f"Highest paid: {highest_paid['name']} at ₹{highest_paid['salary']:,}")