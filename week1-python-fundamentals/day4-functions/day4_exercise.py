records = [
    {
        "id": 1,
        "name": "Kuldeep",
        "email": "kuldeep@email.com",
        "age": 28,
        "salary": 75000,
        "dept": "Analytics",
    },
    {
        "id": 2,
        "name": "",
        "email": "amit@email.com",
        "age": 25,
        "salary": 82000,
        "dept": "Engineering",
    },
    {
        "id": 3,
        "name": "Priya",
        "email": "priya.email.com",
        "age": 30,
        "salary": 69000,
        "dept": "Analytics",
    },
    {
        "id": 4,
        "name": "Rahul",
        "email": "rahul@email.com",
        "age": -5,
        "salary": 91000,
        "dept": "Engineering",
    },
    {
        "id": 5,
        "name": "Neha",
        "email": "neha@email.com",
        "age": 22,
        "salary": -1000,
        "dept": "Marketing",
    },
    {
        "id": 6,
        "name": "Sita",
        "email": "",
        "age": 35,
        "salary": 78000,
        "dept": "Analytics",
    },
    {
        "id": 7,
        "name": "Vikram",
        "email": "vikram@email.com",
        "age": 28,
        "salary": None,
        "dept": "Engineering",
    },
    {
        "id": 8,
        "name": "Kavita",
        "email": "kavita@email.com",
        "age": 200,
        "salary": 71000,
        "dept": "Marketing",
    },
    {
        "id": 9,
        "name": "Raj",
        "email": "raj@email.com",
        "age": 26,
        "salary": 69000,
        "dept": "",
    },
    {
        "id": 10,
        "name": "Meera",
        "email": "meera@email.com",
        "age": None,
        "salary": 88000,
        "dept": "Engineering",
    },
]


def validate_name(name: str):
    if name == "":
        return "name is empty"
    return ""


def validate_email(email: str):
    if "@" not in email:
        return "email missing @"
    return ""


def validate_age(age):
    if age is None or age <= 0 or age >= 120:
        return f"invalid age ({age})"
    return ""


def validate_salary(salary):
    if salary is None or salary < 1:
        return "invalid salary"
    return ""


def validate_dept(dept: str):
    if dept == "":
        return "invalid dpt"
    return ""


def validate_records(record: dict):

    errors = []

    name_error = validate_name(record["name"])
    if name_error:
        errors.append(name_error)

    email_error = validate_email(record["email"])
    if email_error:
        errors.append(email_error)

    age_error = validate_age(record["age"])
    if age_error:
        errors.append(age_error)

    salary_error = validate_salary(record["salary"])
    if salary_error:
        errors.append(salary_error)

    dept_error = validate_dept(record["dept"])
    if dept_error:
        errors.append(dept_error)

    return {"is_valid": len(errors) == 0, "errors": errors}


def generate_report(records: list) -> dict:
    valid_records = []
    invalid_records = []

    for index, rec in enumerate(records, start=1):
        result = validate_records(rec)

        if result["is_valid"]:
            print(f"Row{index}: {rec['name']}- is valid")
            valid_records.append(rec)

        else:
            print(
                f"Row {index}: {rec['name'] or 'UNKNOWN'} — ERRORS: {', '.join(result['errors'])}"
            )
            invalid_records.append(rec)

    summary = {
        "total": len(records),
        "valid": len(valid_records),
        "invalid": len(invalid_records),
        "valid_records": valid_records,
        "invalid_records": invalid_records,
    }
    return summary


summary = generate_report(records)
print(
    f"\nTotal: {summary['total']}, Valid: {summary['valid']}, Invalid: {summary['invalid']}"
)
