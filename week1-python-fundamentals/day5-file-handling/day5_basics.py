# WRITING a text file
with open("hello.txt", "w") as file:
    file.write("Hello, Kuldeep!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# READING a text file
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)



with open("hello.txt", "r") as file:
    # Read entire file as one string
    content = file.read()
    print(content)



with open("hello.txt", "r") as file:
    # Read all lines as a list
    lines = file.readlines()
    print(lines)    # ["Hello, Kuldeep!\n", "This is line 2\n", "This is line 3\n"]

with open("hello.txt", "r") as file:
    # Read line by line — BEST for large files
    for line in file:
        print(line.strip())    # .strip() removes the \n at the end



import csv

employees = [
    {"name": "Kuldeep", "dept": "Analytics", "salary": 75000},
    {"name": "Amit", "dept": "Engineering", "salary": 82000},
    {"name": "Priya", "dept": "Analytics", "salary": 69000},
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "dept", "salary"])
    writer.writeheader()         # writes: name,dept,salary
    writer.writerows(employees)  # writes all rows


with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["salary"] = int(row["salary"])    # convert string to int
        print(f"{row['name']} earns ₹{row['salary']:,}")


import json

# Python dict
employee = {"name": "Kuldeep", "dept": "Analytics", "salary": 75000}

# WRITING dict to JSON file
with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)
    # indent=4 makes it readable (pretty-printed)

# READING JSON file back to dict
with open("employee.json", "r") as file:
    data = json.load(file)
    print(data["name"])    # "Kuldeep"
    print(type(data))      # <class 'dict'>

import json

employees = [
    {"name": "Kuldeep", "dept": "Analytics", "salary": 75000},
    {"name": "Amit", "dept": "Engineering", "salary": 82000},
]

# Write list of dicts to JSON
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

# Read back
with open("employees.json", "r") as file:
    data = json.load(file)
    for emp in data:
        print(emp["name"])

import json

# json.dump / json.load — works with FILES
with open("data.json", "w") as f:
    json.dump(data, f)

# json.dumps / json.loads — works with STRINGS (note the 's')
json_string = json.dumps({"name": "Kuldeep"})   # dict → string
data = json.loads(json_string)                     # string → dict



import os

# Get current working directory
print(os.getcwd())

# Join paths safely (works on Windows and Mac)
filepath = os.path.join("data", "employees.csv")
print(filepath)    # data\employees.csv (Windows) or data/employees.csv (Mac)

# Check if file exists
print(os.path.exists("employees.csv"))    # True or False

# Get file size
print(os.path.getsize("employees.csv"))   # size in bytes


from pathlib import Path

filepath = Path("data") / "employees.csv"
print(filepath.exists())       # True or False
print(filepath.suffix)         # .csv
print(filepath.stem)           # employees (filename without extension)


# Default encoding is UTF-8, but some files use different encodings
# This is common with data from older systems or different countries

# If you get a UnicodeDecodeError, try:
with open("data.csv", "r", encoding="utf-8") as file:
    content = file.read()

# If that fails:
with open("data.csv", "r", encoding="latin-1") as file:
    content = file.read()



import csv

# Process a huge CSV without loading it all into memory
row_count = 0
error_count = 0

with open("huge_file.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row_count += 1
        if row["salary"] == "":
            error_count += 1

print(f"Processed {row_count} rows, found {error_count} errors")
