import csv
import json
import logging
from datetime import datetime

# ---- CONFIGURE LOGGING ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ---- CUSTOM EXCEPTIONS ----
class DataQualityError(Exception):
    """Base class for data quality issues."""
    pass


# ---- FUNCTIONS WITH ERROR HANDLING ----
def convert_to_int(value, field_name: str, row_id):
    """Safely convert a value to int with logging."""
    try:
        if value == "" or value is None:
            logging.warning(f"Row {row_id}: {field_name} is empty")
            return None
        return int(value)
    except ValueError as e:
        logging.error(f"Row {row_id}: cannot convert {field_name}='{value}' to int — {e}")
        return None


def process_file(input_file: str):
    """Read a CSV, process each row with error handling."""
    logging.info(f"Starting to process {input_file}")
    
    clean_records = []
    error_records = []

    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                row_id = row.get("id", "unknown")
                
                # Convert types with error handling
                row["salary"] = convert_to_int(row["salary"], "salary", row_id)
                row["age"] = convert_to_int(row["age"], "age", row_id)
                
                # Classify
                if row["salary"] is not None and row["age"] is not None:
                    clean_records.append(row)
                    logging.debug(f"Row {row_id}: clean")
                else:
                    error_records.append(row)
        
        logging.info(f"Done. Clean: {len(clean_records)}, Errors: {len(error_records)}")
        return clean_records, error_records

    except FileNotFoundError:
        logging.critical(f"File not found: {input_file}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        raise


# ---- CREATE SAMPLE DATA AND RUN ----
sample_data = [
    {"id": "1", "name": "Kuldeep", "age": "28", "salary": "75000"},
    {"id": "2", "name": "Amit", "age": "", "salary": "82000"},
    {"id": "3", "name": "Priya", "age": "30", "salary": "not_a_number"},
    {"id": "4", "name": "Rahul", "age": "-5", "salary": "91000"},
]

with open("demo_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "salary"])
    writer.writeheader()
    writer.writerows(sample_data)

clean, errors = process_file("demo_data.csv")
print(f"\nClean records: {len(clean)}")
print(f"Error records: {len(errors)}")