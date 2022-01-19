import sqlite3


def create():
    connection = sqlite3.connect('employees.db')
    cursor = connection.cursor()
    cursor.executescript('''
                DROP TABLE IF EXISTS departments;
                DROP TABLE IF EXISTS employees;
                CREATE TABLE IF NOT EXISTS departments
                 ( department_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  department_name VARCHAR
                );
                CREATE TABLE IF NOT EXISTS employees
                ( employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name VARCHAR NOT NULL,
                  last_name VARCHAR NOT NULL,
                  department_id INTEGER,
                  CONSTRAINT fk_departments
                  FOREIGN KEY (department_id)
                  REFERENCES departments(department_id)
                  ON DELETE CASCADE
                  ON UPDATE CASCADE
                );
                PRAGMA foreign_keys=ON''')  # ON DELETE SET NULL
    cursor.execute('''INSERT OR IGNORE INTO departments(department_id, department_name) VALUES(null, "department1");''')
    cursor.execute('''INSERT OR IGNORE INTO departments(department_id, department_name) VALUES(null, "department2");''')
    cursor.execute('''INSERT OR IGNORE INTO departments(department_id, department_name) VALUES(null, "department3");''')
    cursor.execute(
        '''INSERT OR IGNORE INTO employees(employee_id, first_name, last_name, department_id) 
        VALUES(null, "Vilmantas", "Rey", 1);''')
    cursor.execute(
        '''INSERT OR IGNORE INTO employees(employee_id, first_name, last_name, department_id) 
        VALUES(null, "Samar", "Ongaro", 2);''')
    cursor.execute(
        '''INSERT OR IGNORE INTO employees(employee_id, first_name, last_name, department_id) 
        VALUES(null, "Rainier", "Solos", 3);''')
    cursor.execute(
        '''INSERT OR IGNORE INTO employees(employee_id, first_name, last_name, department_id) 
        VALUES(null, "Marlena", "Bureau", 1);''')
    connection.commit()
    connection.close()


class Database:
    def __init__(self, path):
        self.path = path
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            self.cursor.execute('PRAGMA foreign_keys=ON;')
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def query(self, query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    def get_result(self, query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return None


if __name__ == '__main__':
    create()
    with Database("employees.db") as db:
        print(db.get_result('SELECT * FROM departments'))
        print(db.get_result('SELECT first_name, last_name FROM employees'))
        print(db.get_result('SELECT employees.first_name, employees.last_name, departments.department_name\
                        FROM employees INNER JOIN departments on  departments.department_id = employees.department_id '
                            'WHERE departments.department_id = 1 ;'))
        db.query('DELETE FROM employees WHERE employee_id = 1')
        print(db.get_result('SELECT employees.first_name, employees.last_name, departments.department_name\
                FROM employees INNER JOIN departments on  departments.department_id = employees.department_id '
                            'WHERE departments.department_id = 1;'))
        db.query('DELETE FROM departments WHERE department_id = 1;')
        print(db.get_result('SELECT * FROM departments'))
        print(db.get_result('SELECT * FROM employees'))
        db.query('UPDATE departments SET department_id = 5 WHERE department_id = 2;')
        print(db.get_result('SELECT * FROM departments'))
        print(db.get_result('SELECT * FROM employees'))
