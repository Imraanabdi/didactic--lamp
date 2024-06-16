
import sqlite3

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

# Employers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    employer_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employer_id) REFERENCES employers (id) ON DELETE SET NULL
)
''')

# Projects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    employer_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employer_id) REFERENCES employers (id) ON DELETE CASCADE
)
''')

# Tasks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    project_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
)
''')

# Timesheets table
cursor.execute('''
CREATE TABLE IF NOT EXISTS timesheets (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    hours_worked REAL NOT NULL,
    employee_id INTEGER,
    task_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees (id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE
)
''')

# Indices for better performance
cursor.execute('CREATE INDEX IF NOT EXISTS idx_employer_email ON employers (email)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_employee_email ON employees (email)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_timesheet_date ON timesheets (date)')

conn.commit()
conn.close()

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    employer_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employer_id) REFERENCES employers (id) ON DELETE CASCADE
)
''')
conn.commit()