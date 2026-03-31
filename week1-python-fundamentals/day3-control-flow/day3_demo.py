# Employee Data Processing with Control Flow

employees = [
    {"name": "Kuldeep", "dept": "Analytics", "salary": 75000, "status": "active"},
    {"name": "Amit", "dept": "Engineering", "salary": 82000, "status": "active"},
    {"name": "Priya", "dept": "Analytics", "salary": -5000, "status": "active"},
    {"name": "Rahul", "dept": "Engineering", "salary": 91000, "status": "inactive"},
    {"name": "Neha", "dept": "", "salary": 65000, "status": "active"},
    {"name": "Sita", "dept": "Analytics", "salary": 78000, "status": "active"},
    {"name": "Vikram", "dept": "Engineering", "salary": None, "status": "active"},
]

print("=== Employee Validation Report ===\n")

valid_count = 0
error_count = 0

for index, emp in enumerate(employees, start=1):
    name = emp["name"]
    
    # Validate each employee
    if emp["salary"] is None:
        print(f"Row {index}: {name} — ERROR: salary is null")
        error_count += 1
        continue
    
    if emp["salary"] <= 0:
        print(f"Row {index}: {name} — ERROR: invalid salary ({emp['salary']})")
        error_count += 1
        continue
    
    if emp["dept"] == "":
        print(f"Row {index}: {name} — ERROR: missing department")
        error_count += 1
        continue
    
    if emp["status"] == "inactive":
        print(f"Row {index}: {name} — SKIPPED: inactive employee")
        continue
    
    # If we reach here, employee is valid
    level = "Senior" if emp["salary"] > 80000 else "Mid" if emp["salary"] > 70000 else "Junior"
    print(f"Row {index}: {name} — VALID ({level})")
    valid_count += 1

print(f"\n=== Summary ===")
print(f"Valid: {valid_count}")
print(f"Errors: {error_count}")
print(f"Total processed: {len(employees)}")