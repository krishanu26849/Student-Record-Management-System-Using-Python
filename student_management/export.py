"""
export.py - CSV File Handler Module
Syllabus Concepts Used:
- File handling (reading/writing files with 'with' open syntax)
- CSV handling using built-in csv module
- Lists and Tuples iteration
- Exception handling using try/except
"""

import csv
import os

def export_to_csv(records, filename):
    """
    Exports a list of student records to a CSV file.
    
    Parameters:
        records (list): List of student tuples (student_id, name, age, course, email, marks)
        filename (str): Target filepath for the CSV output
        
    Returns:
        tuple: (success: bool, message: str)
    """
    if not records:
        return False, "No student records available to export!"

    try:
        # Define CSV table headers
        headers = ["Student ID", "Name", "Age", "Course", "Email", "Marks"]

        # Open file safely using context manager
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # Write header row
            writer.writerow(headers)
            # Write record rows
            writer.writerows(records)

        return True, f"Successfully exported {len(records)} record(s) to '{os.path.basename(filename)}'!"

    except PermissionError:
        return False, "Permission denied! Please check if the target file is currently open."
    except Exception as e:
        return False, f"Failed to export CSV: {e}"
