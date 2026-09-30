"""
student.py - Student Data Model and Validation Logic
Syllabus Concepts Used:
- Classes and Objects (OOP)
- Instance methods
- Static methods
- Basic Input Validation & Exception Handling
"""

import re

class Student:
    """
    Represents a Student entity in the Student Record Management System.
    """
    def __init__(self, student_id, name, age, course, email, marks):
        """
        Constructor to initialize student attributes.
        """
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.age = int(age)
        self.course = str(course).strip()
        self.email = str(email).strip()
        self.marks = float(marks)

    def to_dict(self):
        """
        Converts student object data to a dictionary representation.
        Demonstrates use of Dictionaries.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "email": self.email,
            "marks": self.marks
        }

    def to_tuple(self):
        """
        Converts student object attributes to a tuple for database queries.
        Demonstrates use of Tuples.
        """
        return (self.student_id, self.name, self.age, self.course, self.email, self.marks)

    @staticmethod
    def validate_inputs(student_id, name, age_str, course, email, marks_str):
        """
        Validates user input fields before database operations.
        Returns (is_valid: bool, error_message: str)
        """
        # Check required fields
        if not student_id or not name or not age_str or not course or not email or not marks_str:
            return False, "All fields are required!"

        # Validate Student ID format (alphanumeric, no spaces)
        if not re.match(r'^[A-Za-z0-9_-]+$', student_id):
            return False, "Student ID should contain only letters, numbers, hyphens, or underscores."

        # Validate Age
        try:
            age = int(age_str)
            if age < 5 or age > 100:
                return False, "Age must be between 5 and 100."
        except ValueError:
            return False, "Age must be a valid integer."

        # Validate Email
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return False, "Please enter a valid email address (e.g., student@example.com)."

        # Validate Marks
        try:
            marks = float(marks_str)
            if marks < 0 or marks > 100:
                return False, "Marks must be between 0 and 100."
        except ValueError:
            return False, "Marks must be a valid numeric value."

        return True, ""
