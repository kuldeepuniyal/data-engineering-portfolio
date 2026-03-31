def validate_name(name: str) -> str:
    """Return error message if name is invalid, empty string if valid."""
    if name == "":
        return "name is empty"
    return ""

def validate_email(email: str) -> str:
    """Return error message if email is invalid, empty string if valid."""
    if email == "":
        return "email is empty"
    if "@" not in email:
        return "email missing @"
    return ""

def validate_age(age) -> str:
    """Return error message if age is invalid, empty string if valid."""
    if age is None:
        return "age is null"
    if age <= 0 or age >= 120:
        return f"invalid age ({age})"
    return ""

def validate_record(record: dict) -> dict:
    """
    Validate a single employee record.
    
    Returns:
        Dict with 'is_valid' and 'errors' keys
    """
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
    
    return {"is_valid": len(errors) == 0, "errors": errors}

# Using it
result = validate_record({"name": "Kuldeep", "email": "k@email.com", "age": 28})
print(result)  # {"is_valid": True, "errors": []}

result = validate_record({"name": "", "email": "bad.email", "age": -5})
print(result)  # {"is_valid": False, "errors": ["name is empty", "email missing @", "invalid age (-5)"]}