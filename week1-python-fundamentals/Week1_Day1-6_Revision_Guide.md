# Data Engineering Journey — Week 1 Revision Guide (Days 1-6)

*Python Fundamentals — Analyst to Engineer*

---

## Day 1: Variables, Types, Operators, Strings

### Core Concept
Python variables work like BigQuery columns, but flexible — no fixed type per variable.

```python
name = "Kuldeep"        # str
age = 28                 # int
salary = 75000.50        # float
is_active = True         # bool
nothing = None           # NoneType (like SQL NULL)
```

### Type Conversion (like CAST in SQL)
```python
str(28)        # "28"
int("28")      # 28
float("3.14")  # 3.14
```
`int("hello")` throws `ValueError` — same as a bad `CAST` in SQL.

### Operators
| SQL | Python | Meaning |
|---|---|---|
| `=` | `==` | equals (comparison) |
| `<>` / `!=` | `!=` | not equals |
| `AND` / `OR` / `NOT` | `and` / `or` / `not` | logical |
| `IS NULL` | `is None` | null check |

⚠️ **#1 beginner mistake:** using `=` (assignment) instead of `==` (comparison).

### Strings
```python
name.strip()          # like TRIM()
name.split(" ")        # like SPLIT()
" ".join(words)        # opposite of split
name.replace("a","b")  # like REPLACE()
f"Hello {name}"        # f-strings — best way to format output
```

### Key Gotcha
`/` always returns a **float** even with two ints (`10/2` → `5.0`). Use `//` for integer division.

**Artifact built:** Calculator with zero-division handling.

---

## Day 2: Lists, Dicts, Tuples, Sets

| Python | SQL/BigQuery analogy | Ordered? | Mutable? | Duplicates? |
|---|---|---|---|---|
| List `[]` | Column of values | Yes | Yes | Yes |
| Dict `{}` | Single row (key:value) | Yes | Yes | Keys: No |
| Tuple `()` | Frozen STRUCT | Yes | No | Yes |
| Set `{}` | SELECT DISTINCT | No | Yes | No |

### Lists
```python
names[0]          # first element (0-indexed)
names[-1]          # last element
names[1:3]          # slicing — like LIMIT/OFFSET
[s for s in salaries if s > 80000]     # list comprehension = SELECT...WHERE
```

### Dicts
```python
emp["name"]                  # direct access
emp.get("phone", "N/A")      # safe access with default
emp.keys() / emp.values() / emp.items()
{name: salary for name, salary in zip(names, salaries)}  # dict comprehension
```

**List of dicts = a table.** This pattern is everywhere in data engineering (API responses, JSON files, DB rows).

### Tuples
Immutable — used for data that shouldn't change (coordinates, config, DB connection params). Can be dict keys; lists cannot.

### Sets
```python
set(cities)              # deduplicates = SELECT DISTINCT
team_a | team_b           # UNION
team_a & team_b           # INTERSECT
team_a - team_b           # EXCEPT
```

### Key Gotcha
Dict lookup = **O(1)** (instant, like an indexed lookup). List search = **O(n)** (scans everything, like a full table scan). This is a very common interview question.

**Artifact built:** Employee data processor (filter, average salary per dept, top earners, dedup) — no pandas.

---

## Day 3: Control Flow — Loops, Conditionals, Logic

### if / elif / else (like CASE WHEN)
```python
if salary > 90000:
    level = "Senior"
elif salary > 70000:
    level = "Mid"
else:
    level = "Junior"
```
Python uses **indentation** instead of `BEGIN/END`. Ternary: `"High" if salary > 80000 else "Low"`.

### For Loops
```python
range(5)                          # 0,1,2,3,4
enumerate(names, start=1)          # index + value, like ROW_NUMBER()
zip(names, salaries, cities)       # loop multiple lists together, like a JOIN on index
for key, value in employee.items():  # loop through dict
```

### While Loops
```python
while count > 0:
    count -= 1
```

### break vs continue
- `break` → exit the loop immediately (like `LIMIT 1`)
- `continue` → skip current item, go to next (like a `WHERE` filter)

### Golden Pattern: Collect All Errors Per Record
```python
errors = []
if condition1: errors.append("msg1")
if condition2: errors.append("msg2")
if errors:
    # invalid — report ALL problems, not just the first
else:
    # valid
```
Never stop at the first error in real validation — collect everything wrong with a record.

### Key Gotcha
Never modify a list while iterating over it — indices shift and you skip elements. Build a new filtered list instead.

**Artifact built:** Data validation script (name/email/age/salary/dept checks, error collection pattern).

---

## Day 4: Functions — Writing Reusable Code

### Structure (like a SQL VIEW/stored function)
```python
def function_name(parameter):
    """Docstring explaining what this does."""
    # logic
    return result
```
**Parameter** = placeholder in the definition. **Argument** = actual value passed when calling.

### Default Parameters
```python
def greet(name, greeting="Hello"):   # greeting is optional
    print(f"{greeting}, {name}!")
```

### Return Values
A function with no `return` gives back `None`. Functions can return single values, tuples, dicts, etc.

### Lambda (one-line throwaway functions)
```python
sorted(employees, key=lambda emp: emp["salary"])
```
Use `def` for anything longer than one line; use lambda for quick, single-use logic (often with `sorted`, `key=`).

### Scope
Variables created inside a function stay inside — **except lists/dicts are mutable**, so modifying them in place (e.g. `.append()`) DOES affect the original object outside the function.

```python
def process(data):
    data.append(4)     # mutates the ORIGINAL list — not a copy!

nums = [1,2,3]
process(nums)
print(nums)   # [1,2,3,4]
```

### Type Hints & Docstrings
```python
def add_tax(salary: float) -> float:
    """Add 18% GST tax to salary."""
    return salary * 1.18
```
Type hints are just labels for humans/IDE — Python does not enforce them.

### Design Pattern Learned
Break one big script into small single-purpose functions (`validate_name`, `validate_email`...) called by one orchestrator function (`validate_record`). Benefits: reusability, easier debugging, each piece is independently testable.

**Artifact built:** Refactored Day 3 validator into clean functions with type hints/docstrings.

---

## Day 5: File Handling — CSV, JSON, Text

### Always Use `with open()`
```python
with open("file.csv", "r") as f:
    content = f.read()
# file auto-closes here, even if an error occurs
```
Modes: `"r"` read, `"w"` write (overwrites), `"a"` append.

**Never use `file.read()` on huge files** — loads everything into memory. Read line-by-line instead (streaming, like BigQuery processing rows incrementally).

### CSV
```python
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[...])
    writer.writeheader()
    writer.writerows(data)

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ...   # ⚠️ everything comes back as STRINGS — must convert types yourself
```

### JSON
```python
json.dump(data, file, indent=4)   # dict/list → FILE
json.load(file)                    # FILE → dict/list
json.dumps(data)                   # dict/list → STRING (used for APIs)
json.loads(json_string)            # STRING → dict/list
```
The `s` in `dumps`/`loads` = **string**.

### Type-Safe Conversion Pattern
```python
try:
    row["salary"] = int(row["salary"]) if row["salary"] else None
except ValueError:
    row["salary"] = None
```
This is Python's version of BigQuery's `SAFE_CAST` — convert if possible, `None` if not, never crash.

### ETL Pattern Built
`read_and_clean()` → `save_json()` → `generate_summary()` → `run_pipeline()` (orchestrator).
This is **Extract → Transform → Load** — the core shape of every data pipeline you'll build from here on.

**Artifact built:** CSV → JSON ETL pipeline with data cleaning, error/clean record splitting, and summary stats.

---

## Day 6: Error Handling + Logging

### Why It Matters
Real data is messy. Pipelines that crash on the first bad row wake you up at 3 AM. Error handling + logging = pipelines that survive bad data AND leave a trail for debugging.

### try / except / else / finally
```python
try:
    result = int("42")
except ValueError as e:
    print(f"Failed: {e}")      # runs only if error
else:
    print(f"Success: {result}") # runs only if NO error
finally:
    print("Always runs")        # cleanup — runs no matter what
```
**Catch specific exceptions**, never a bare `except:` — that hides real bugs.

### Custom Exceptions
```python
class DataQualityError(Exception):
    """Raised when data fails quality checks."""
    pass

raise DataQualityError("Too many records failed validation")
```
Use custom exceptions for **business rules** (e.g. "50% of data is bad") vs built-in exceptions for **technical failures** (e.g. `ValueError`, `FileNotFoundError`). Lets you catch exactly what you expect and let everything else fail loudly.

### Logging Module (replaces `print()`)
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),            # console
        logging.FileHandler("pipeline.log")  # file — permanent record
    ]
)
```

### Logging Levels — When to Use Which
| Level | Use for | Example from your pipeline |
|---|---|---|
| `DEBUG` | Fine-grained dev detail | "Processing row 47" |
| `INFO` | Normal milestones | "Pipeline started", "Written raw_data.csv" |
| `WARNING` | Recovered gracefully | "name is empty, defaulted to 'Unknown'" |
| `ERROR` | Row failed, pipeline continues | "cannot convert salary='not_a_number' to int" |
| `CRITICAL` | Pipeline cannot continue | "File not found: raw_data.csv" |

### Critical Rules Learned (from real bugs you fixed)
1. **Log the bad value BEFORE overwriting it** — once you reassign a variable, the original value is gone.
   ```python
   except ValueError:
       logging.error(f"Row {row_id}: cannot convert salary='{row['salary']}'")  # log first
       row["salary"] = None   # overwrite second
   ```
2. **`raise` inside `except` must stay indented inside that block** — otherwise it either runs unconditionally or crashes with "no active exception."
3. **Code that runs the pipeline (function calls) must NOT be indented inside the function definition** — or you get infinite recursion / it never actually executes.
4. **`raise` after `logging.critical()`** ensures the program actually stops instead of silently continuing with a broken state — logging gives visibility, `raise` gives control flow. You need both.

### Full Production Pattern
```python
def save_json(filepath: str, data: list):
    try:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Written {filepath} ({len(data)} records)")
    except (IOError, PermissionError) as e:
        logging.critical(f"Failed to write {filepath}: {e}")
        raise
```

**Artifact built:** Production-grade version of the Day 5 pipeline — dual logging (console + file), custom `DataQualityError`, try/except on every I/O operation, full row-level traceability.

---

## Cross-Cutting Threads (What Connects All 6 Days)

Your Day 5-6 pipeline used **every single concept** from the week:
- **Day 1** types → converting CSV strings to int/float
- **Day 2** dicts/lists → each row is a dict, all rows are a list of dicts
- **Day 3** control flow → validating each field, collecting errors
- **Day 4** functions → breaking the pipeline into reusable, testable pieces
- **Day 5** file I/O → CSV in, JSON out
- **Day 6** error handling → pipeline survives bad data, logs explain what happened

This is the shape of **every real data pipeline** you'll ever build, at any scale.

---

## Common Interview Questions Bank (From This Week)

1. What's the difference between `=` and `==`?
2. Why is `10/3` a float but `10//3` isn't?
3. Dict lookup vs list search — time complexity and why?
4. When would you use a tuple instead of a list?
5. `.sort()` vs `sorted()` — what's the real difference?
6. What is `break` vs `continue`?
7. Why should you never modify a list while iterating over it?
8. Parameter vs argument — what's the difference?
9. Why are lists/dicts different from numbers/strings when passed into functions (mutable vs immutable)?
10. Why use `with open()` instead of `open()` directly?
11. `json.dump()` vs `json.dumps()` — when do you use each?
12. How would you process a 50GB CSV that doesn't fit in memory?
13. WARNING vs ERROR — how do you decide which to log?
14. Why use a custom exception instead of `return False`?
15. Why `raise` again after logging inside an `except` block?

---

## What's Next: Day 7

**Week 1 Capstone Project — Data Quality Checker**
A CLI tool that takes a CSV, checks for nulls/duplicates/type mismatches/outliers, and generates a JSON quality report. Combines everything from Days 1-6 into your first real portfolio piece.

---

*Generated as a revision reference — Data Engineering 12-Week Mastery Plan*
