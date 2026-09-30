"""
database.py - SQLite Database Management Module
Syllabus Concepts Used:
- SQLite Database Connectivity
- SQL Queries (CREATE, INSERT, SELECT, UPDATE, DELETE)
- Exception handling using try/except (sqlite3.Error)
- OOP (DatabaseManager class)
"""

import sqlite3
import os

class DatabaseManager:
    """
    Manages database connection and CRUD operations for Student records.
    """
    def __init__(self, db_name="students.db"):
        """
        Initializes the database connection and creates table if not exists.
        """
        # Ensure database is created in the project directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_name)
        self.create_table()

    def get_connection(self):
        """
        Creates and returns a database connection.
        """
        return sqlite3.connect(self.db_path)

    def create_table(self):
        """
        Creates the 'students' table if it does not already exist.
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        student_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        course TEXT NOT NULL,
                        email TEXT NOT NULL,
                        marks REAL NOT NULL
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database Error during table creation: {e}")

    def add_student(self, student):
        """
        Inserts a new student record into the database.
        Returns (success: bool, message: str)
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO students (student_id, name, age, course, email, marks)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, student.to_tuple())
                conn.commit()
                return True, "Student record added successfully!"
        except sqlite3.IntegrityError:
            return False, f"Student ID '{student.student_id}' already exists!"
        except sqlite3.Error as e:
            return False, f"Database error: {e}"

    def fetch_all_students(self):
        """
        Fetches all student records from the database.
        Returns a list of tuples.
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT student_id, name, age, course, email, marks FROM students ORDER BY name ASC")
                records = cursor.fetchall()
                return records
        except sqlite3.Error as e:
            print(f"Error fetching students: {e}")
            return []

    def search_students(self, query):
        """
        Searches for students by Student ID or Name matching the query.
        Returns a list of matching student tuples.
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                search_param = f"%{query.strip()}%"
                cursor.execute("""
                    SELECT student_id, name, age, course, email, marks 
                    FROM students 
                    WHERE student_id LIKE ? OR name LIKE ?
                    ORDER BY name ASC
                """, (search_param, search_param))
                records = cursor.fetchall()
                return records
        except sqlite3.Error as e:
            print(f"Error searching students: {e}")
            return []

    def update_student(self, student):
        """
        Updates an existing student record based on student_id.
        Returns (success: bool, message: str)
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE students 
                    SET name = ?, age = ?, course = ?, email = ?, marks = ?
                    WHERE student_id = ?
                """, (student.name, student.age, student.course, student.email, student.marks, student.student_id))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Student record updated successfully!"
                else:
                    return False, f"No student found with ID '{student.student_id}'."
        except sqlite3.Error as e:
            return False, f"Database error: {e}"

    def delete_student(self, student_id):
        """
        Deletes a student record by student_id.
        Returns (success: bool, message: str)
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
                conn.commit()
                if cursor.rowcount > 0:
                    return True, "Student record deleted successfully!"
                else:
                    return False, f"No student found with ID '{student_id}'."
        except sqlite3.Error as e:
            return False, f"Database error: {e}"
