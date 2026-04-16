import csv
import json
import os

# ---- STEP 1: Create sample data ----
employees = [
    {"name": "Kuldeep", "dept": "Analytics", "salary": "75000", "city": "Ghaziabad"},
    {"name": "Amit", "dept": "Engineering", "salary": "82000", "city": "Delhi"},
    {"name": "Priya", "dept": "Analytics", "salary": "", "city": "Mumbai"},
    {"name": "Rahul", "dept": "Engineering", "salary": "91000", "city": ""},
    {"name": "Neha", "dept": "Marketing", "salary": "bad_data", "city": "Ghaziabad"},
]

# ---- STEP 2: Write to CSV ----

with open("raw_employee.csv","w",newline="") as file:
    writer=csv.DictWriter(file,fieldnames=["name","dept","salary","city"])
    writer.writeheader()
    writer.writerows(employees)
print("written raw_employees.csv")


# ---- STEP 3: Read CSV, clean data, handle errors ----

clean_records=[]
error_records=[]

with open("raw_employee.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        #try convert salary into integer
        try:
            row["salary"]=int(row["salary"]) if row["salary"] else None
        except ValueError:
            row["salary"]=None

        if row["city"]=="":
            row["city"]="unknown"

        if row["salary"] is not None:
            clean_records.append(row)
        else:
            error_records.append(row)


# ---- STEP 4: Write clean data to JSON ----
with open("clean_data.json","w") as file:
    json.dump(clean_records,file,indent=4)
print(f"written clean_data.json  ({len(clean_records)} records)")


# ---- STEP 5: Write errors to separate file ----
with open("error_records.json","w") as file:
    json.dump(error_records,file,indent=4)
print(f"error_.josn ({len(error_records)} recors)")





