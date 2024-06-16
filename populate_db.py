import sqlite3

def insert_dummy_data():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Insert dummy data into employers table
    cursor.execute("INSERT INTO employers (name, email) VALUES ('Tech Solutions Inc', 'techsolutions@example.com')")
    cursor.execute("INSERT INTO employers (name, email) VALUES ('Data Innovations Ltd', 'datainnovations@example.com')")
    cursor.execute("INSERT INTO employers (name, email) VALUES ('Cloud Systems Co', 'cloudsystems@example.com')")

    # Insert dummy data into employees table
    cursor.execute("INSERT INTO employees (name, email, employer_id) VALUES ('John Doe', 'john.doe@example.com', 1)")
    cursor.execute("INSERT INTO employees (name, email, employer_id) VALUES ('Jane Smith', 'jane.smith@example.com', 2)")
    cursor.execute("INSERT INTO employees (name, email, employer_id) VALUES ('Michael Brown', 'michael.brown@example.com', 3)")

    # Insert dummy data into projects table
    cursor.execute("INSERT INTO projects (name, description, employer_id) VALUES ('Web Development', 'Building responsive web applications', 1)")
    cursor.execute("INSERT INTO projects (name, description, employer_id) VALUES ('Data Analytics', 'Analyzing customer data for insights', 2)")
    cursor.execute("INSERT INTO projects (name, description, employer_id) VALUES ('Cloud Migration', 'Migrating legacy systems to cloud infrastructure', 3)")

    # Insert dummy data into tasks table
    cursor.execute("INSERT INTO tasks (name, description, project_id) VALUES ('Frontend Development', 'Designing and implementing UI components', 1)")
    cursor.execute("INSERT INTO tasks (name, description, project_id) VALUES ('Data Cleaning', 'Preparing data for analysis', 2)")
    cursor.execute("INSERT INTO tasks (name, description, project_id) VALUES ('Infrastructure Setup', 'Setting up cloud servers and networks', 3)")

    # Insert dummy data into timesheets table
    cursor.execute("INSERT INTO timesheets (date, hours_worked, employee_id, task_id) VALUES ('2023-06-10', 8.5, 1, 1)")
    cursor.execute("INSERT INTO timesheets (date, hours_worked, employee_id, task_id) VALUES ('2023-06-11', 7.5, 2, 2)")
    cursor.execute("INSERT INTO timesheets (date, hours_worked, employee_id, task_id) VALUES ('2023-06-12', 6.0, 3, 3)")

    conn.commit()
    conn.close()
    print("Dummy data inserted successfully.")

if __name__ == "__main__":
    insert_dummy_data()
