records = [
    {"id": 1, "name": "Kuldeep", "email": "kuldeep@email.com", "age": 28, "salary": 75000, "dept": "Analytics"},
    {"id": 2, "name": "", "email": "amit@email.com", "age": 25, "salary": 82000, "dept": "Engineering"},
    {"id": 3, "name": "Priya", "email": "priya.email.com", "age": 30, "salary": 69000, "dept": "Analytics"},
    {"id": 4, "name": "Rahul", "email": "rahul@email.com", "age": -5, "salary": 91000, "dept": "Engineering"},
    {"id": 5, "name": "Neha", "email": "neha@email.com", "age": 22, "salary": -1000, "dept": "Marketing"},
    {"id": 6, "name": "Sita", "email": "", "age": 35, "salary": 78000, "dept": "Analytics"},
    {"id": 7, "name": "Vikram", "email": "vikram@email.com", "age": 28, "salary": None, "dept": "Engineering"},
    {"id": 8, "name": "Kavita", "email": "kavita@email.com", "age": 200, "salary": 71000, "dept": "Marketing"},
    {"id": 9, "name": "Raj", "email": "raj@email.com", "age": 26, "salary": 69000, "dept": ""},
    {"id": 10, "name": "Meera", "email": "meera@email.com", "age": None, "salary": 88000, "dept": "Engineering"},
]


valid_records = []
invalid_records = []

for index, rec in enumerate(records, start=1):
    errors = []    # empty list — collect all errors for THIS record
    
    # Check name
    if rec["name"] == "":
        errors.append("name is empty")
    
    # Check email — add your checks here
    if "@" not in rec["email"]:
        errors.append("ERRORS: email missing @")
        
    
    # Check age — add your checks here
    if rec["age"] is None or rec["age"]<=0 or rec["age"]>=120:
        errors.append("invalid age ")

    
    # Check salary — add your checks here
    if rec["salary"] is None or rec["salary"]<1:
        errors.append("invalid salary")

    
    # Check dept — add your checks here
    if rec["dept"]=="":
        errors.append("invalid department")

    
    # After ALL checks, decide if record is valid
    if errors:    # if errors list is not empty
        print(f"Row {index}: {rec['name'] or 'UNKNOWN'} — ERRORS: {', '.join(errors)}")
        invalid_records.append(rec)
    else:
        print(f"Row {index}: {rec['name']} — VALID")
        valid_records.append(rec)



print(f"\nValid: {len(valid_records)}")
for rec in valid_records:
    print(f"{rec["name"]}")
print(f"Invalid: {len(invalid_records)}")
for rec in invalid_records:
    print(f"{rec["name"]}")
