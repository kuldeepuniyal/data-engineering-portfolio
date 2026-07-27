import csv
import json
import logging

# ---- CONFIGURE LOGGING: console + file ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),           # prints to console
        logging.FileHandler("pipeline.log") # writes to pipeline.log
    ]
)
# ---- CUSTOM EXCEPTIONS ----
class DataQualityError(Exception):
    """Base class for data quality issues."""
    pass

raw_data = [
    {"id": "1", "name": "Kuldeep", "email": "kuldeep@email.com", "age": "28", "salary": "75000", "dept": "Analytics", "join_date": "2023-01-15"},
    {"id": "2", "name": "", "email": "amit@email.com", "age": "25", "salary": "82000", "dept": "Engineering", "join_date": "2023-03-20"},
    {"id": "3", "name": "Priya", "email": "priya.email.com", "age": "30", "salary": "69000", "dept": "Analytics", "join_date": "2022-07-10"},
    {"id": "4", "name": "Rahul", "email": "rahul@email.com", "age": "-5", "salary": "91000", "dept": "Engineering", "join_date": "2023-06-01"},
    {"id": "5", "name": "Neha", "email": "neha@email.com", "age": "22", "salary": "", "dept": "Marketing", "join_date": "2023-09-15"},
    {"id": "6", "name": "Sita", "email": "", "age": "35", "salary": "78000", "dept": "Analytics", "join_date": "bad_date"},
    {"id": "7", "name": "Vikram", "email": "vikram@email.com", "age": "28", "salary": "not_a_number", "dept": "Engineering", "join_date": "2023-04-20"},
    {"id": "8", "name": "Kavita", "email": "kavita@email.com", "age": "200", "salary": "71000", "dept": "Marketing", "join_date": "2023-08-10"},
    {"id": "9", "name": "Raj", "email": "raj@email.com", "age": "26", "salary": "69000", "dept": "", "join_date": "2023-05-25"},
    {"id": "10", "name": "Meera", "email": "meera@email.com", "age": "", "salary": "88000", "dept": "Engineering", "join_date": "2023-11-01"},
]


def write_raw_csv(filepath: str, data: list):
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    logging.info(f"Written {filepath}")
def read_and_clean(filepath: str) -> tuple:
    clean_records = []
    error_records = []

    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_id = row.get("id", "unknown")

                # Convert salary — add logging.error in the except block
                try:
                    row["salary"] = int(row["salary"]) if row["salary"] else None
                except ValueError:
                    logging.error(f"Row {row_id}: cannot convert salary='{row['salary']}' to int")
                    row["salary"] = None
                    # log the error here — include row_id, field name, bad value

                # Convert age — same pattern
                try:
                    row["age"] = int(row["age"]) if row["age"] else None
                except ValueError:
                    logging.error(f"Row {row_id}: cannot convert age='{row['age']}' to int")
                    row["age"] = None
                    # log the error here

                # Fix empty name and dept — add logging.warning when defaulted
                if row["name"] == "":
                    logging.warning(f"Row {row_id}: name is empty, defaulted to 'Unknown'")
                    row["name"] = "Unknown"
                    # log a warning here
                if row["dept"] == "":
                    logging.warning(f"Row {row_id}: dept is empty, defaulted to 'Unassigned'")
                    row["dept"] = "Unassigned"
                    # log a warning here

                if row["salary"] is not None and row["age"] is not None:
                    clean_records.append(row)
                else:
                    error_records.append(row)

    except FileNotFoundError:
        logging.critical(f"File not found: {filepath}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        raise
    
    return clean_records, error_records

def save_json(filepath: str, data: list):
    try:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Written {filepath}")# log success here
    except (IOError, PermissionError) as e: 
        logging.critical(f"Failed to write {filepath}: {e}")
        raise# log critical here, then decide: raise or return?

def generate_summary(clean: list, errors: list) -> dict:
    total = len(clean) + len(errors)
    
    if total > 0 and len(errors) / total > 0.5:
        raise DataQualityError(
            f"Data quality too low: {len(errors)}/{total} records failed validation"
        )
    
    if clean:
       avg_salary = sum(rec["salary"] for rec in clean) / len(clean)
    else:
       avg_salary = 0
    # Count records per department
    records_per_dept = {}
    for rec in clean:
        dept = rec["dept"]
        records_per_dept[dept] = records_per_dept.get(dept, 0) + 1
    
    summary = {
        "total": len(clean) + len(errors),
        "clean": len(clean),
        "errors": len(errors),
        "avg_salary": avg_salary,
        "records_per_dept": records_per_dept
    }
    return summary
    


def run_pipeline(input_csv: str, output_json: str, error_json: str):
    logging.info(f"Pipeline started for {input_csv}")
    clean, errors = read_and_clean(input_csv)
    logging.info(f"Processed {len(clean) + len(errors)} records — Clean: {len(clean)}, Errors: {len(errors)}")
    save_json(output_json, clean)
    save_json(error_json, errors)
    try:
        summary = generate_summary(clean, errors)
    except DataQualityError as e:
        logging.critical(f"Pipeline aborted: {e}")
        raise
    logging.info(f"Pipeline finished. Summary: {summary}")


# ---- ACTUALLY RUN THE PIPELINE (no indentation — top level) ----
write_raw_csv("raw_data.csv", raw_data)
run_pipeline("raw_data.csv", "clean_data.json", "errors.json")