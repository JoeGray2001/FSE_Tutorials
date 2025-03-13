import sqlite3

with sqlite3.connect("My_Database.db") as connection:
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL,
        hire_date TEXT
    );
    """
    cursor.execute(create_table_query)


def insert_single_record(name: str, department: str, salary: float, hire_date: str):
    with sqlite3.connect("My_Database.db") as connection:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO employees (name, department, salary, hire_date)
        VALUES (?, ?, ?, ?);
        """
        cursor.execute(insert_query, (name, department, salary, hire_date))
        connection.commit()
        print(f"Record for {name} inserted successfully.")

insert_single_record("Isco", "IT", 50000, "2021-01-01")

# Function to query employee data
def query_employee_data(department):
    with sqlite3.connect("My_Database.db") as connection:
        cursor = connection.cursor()
        query = "SELECT employee_id from employees WHERE department = ?;"
        cursor.execute(query, (department,))



def main():
    try:
        name, age, email = get_user_input()

        insert_single_record(name, age, email)
        pass