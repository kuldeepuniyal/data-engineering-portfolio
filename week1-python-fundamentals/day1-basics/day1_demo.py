print("Hello, I am Kuldeep and I am learning Python!")
name = "Kuldeep"
age = 28
print(f"My name is {name} and I am {age} years old")

# Variables and types
employee_name = "Kuldeep Uniyal"
employee_id = 101
salary = 75000.50
is_active = True
department = None

print(f"Name type: {type(employee_name)}")  # str
print(f"Salary type: {type(salary)}")        # float


# String operations
first_name = employee_name.split(" ")[0]
print(f"First name: {first_name}")

# Type conversion
salary_text = str(salary)
print(f"Salary as string: {salary_text}")

# Arithmetic
annual_bonus = salary * 0.10
total_comp = salary + annual_bonus
print(f"Total compensation: {total_comp}")

# Comparison and logic
is_senior = salary > 50000 and is_active
print(f"Is senior: {is_senior}") 

# None check
if department is None:
    print("Department not assigned yet")


    print(f"Employee {employee_id}: {employee_name} | Salary: ₹{salary:,.2f} | Active: {is_active}")
