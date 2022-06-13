import sqlite3

conn = sqlite3.connect("python_db.db")
c = conn.cursor()

with conn:
    c.execute("""
    CREATE TABLE
    employees (
        name text,
        surname text,
        salary integer
    )
    """)

database = "employees"
employees = [
    {"name": "Tomas","surname": "Tomauskas", "salary": 1000},
    {"name": "Antanas","surname": "Bevardis", "salary": 1500},
    {"name": "Jonas","surname": "Antanauskas", "salary": 1200},
    {"name": "Romas","surname": "Tomauskas", "salary": 1300},
]


# for employee in employees:
#     print(employee)           

with conn:
    for employee in employees:
        # a = f"INSERT INTO {database} VALUES ({employee['name']},{employee['surname']}, {employee['salary']})"
        print(f"inserting {employee}")
        c.execute(f"INSERT INTO {database} VALUES ({employee['name']},{employee['surname']}, {employee['salary']})")

with conn:
    c.execute(f"INSERT INTO {database}  VALUES ('Tomas', 'Tomauskas', 1000)")
    c.execute(f"INSERT INTO {database}  VALUES ('Antanas', 'Bevardis', 1500)")
    c.execute(f"INSERT INTO {database}  VALUES ('Jonas', 'Antanauskas', 1200)")
    c.execute(f"INSERT INTO {database}  VALUES ('Romas', 'Tomauskas', 1300)")





with conn:
    c.execute("SELECT * From employees")
    print(c.fetchall())


while True:
    print("Įveskite darbuotoją")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde:")
    atlyginimas = int(input("atlyginimas :"))

    with conn:
        c.execute(f"INSERT INTO employees VALUES ('{vardas}', '{pavarde}', {atlyginimas})")

    with conn:
        c.execute("SELECT * FROM employees")
        print(c.fetchall())