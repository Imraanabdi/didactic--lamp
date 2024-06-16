from db import conn, cursor



class Timesheet:
    TABLE_NAME = "timesheets"

    def __init__(self, employee_id, date_worked, hours_worked, project_code, task_description):
        self.id = None
        self.employee_id = employee_id
        self.date_worked = date_worked
        self.hours_worked = hours_worked
        self.project_code = project_code
        self.task_description = task_description
        self.created_at = None

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (employee_id, date_worked, hours_worked, project_code, task_description)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.employee_id, self.date_worked, self.hours_worked, self.project_code, self.task_description))
        conn.commit()
        self.id = cursor.lastrowid
        return self

    def update(self):
        sql = f"""
            UPDATE {self.TABLE_NAME}
            SET employee_id = ?, date_worked = ?, hours_worked = ?, project_code = ?, task_description = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.employee_id, self.date_worked, self.hours_worked, self.project_code, self.task_description, self.id))
        conn.commit()
        return self

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date_worked": self.date_worked,
            "hours_worked": self.hours_worked,
            "project_code": self.project_code,
            "task_description": self.task_description,
            "created_at": self.created_at
        }

    @classmethod
    def find_one(cls, id):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE id = ?
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.row_to_instance(row)

    @classmethod
    def find_all(cls):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            ORDER BY date_worked DESC
        """
        rows = cursor.execute(sql).fetchall()
        return [cls.row_to_instance(row).to_dict() for row in rows]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        timesheet = cls(row[1], row[2], row[3], row[4], row[5])
        timesheet.id = row[0]
        timesheet.created_at = row[6]
        return timesheet

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER NOT NULL,
                date_worked DATE NOT NULL,
                hours_worked REAL NOT NULL,
                project_code TEXT NOT NULL,
                task_description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Timesheet table created successfully")

Timesheet.create_table()

