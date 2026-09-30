# Student Record Management System 🎓

**Course Code:** CSE3011 - Python Programming  
**Technology Stack:** Python 3, Tkinter GUI, SQLite3 Database, CSV File Handling, OOP  

---

## 1. Project Title
**Student Record Management System**

---

## 2. Project Description
The **Student Record Management System** is a desktop application built using Python, Tkinter, and SQLite3. It provides an intuitive Graphical User Interface (GUI) for educational institutions to create, view, search, update, delete, and export student academic records. 

Designed specifically for the **CSE3011 Python Programming syllabus**, this project focuses on fundamental Python principles including Object-Oriented Programming (OOP), modular architecture, input validation, robust database connectivity, and CSV file handling without relying on third-party frameworks.

---

## 3. Key Features
1. **Add Student Record:** Insert student details (Student ID, Full Name, Age, Course, Email, Marks) with real-time validation.
2. **View All Students:** Display records in an interactive, formatted table (`ttk.Treeview`) with custom headers and vertical scrollbars.
3. **Search Student:** Search records dynamically by Student ID or Student Name.
4. **Update Student:** Select a row in the directory table to auto-fill input fields and update record details seamlessly.
5. **Delete Student:** Remove student entries safely with an interactive confirmation prompt (`messagebox.askyesno`).
6. **Export Records to CSV:** Save current database records to an external `.csv` spreadsheet file using a native file save dialog.
7. **Clear Form Fields:** One-click reset for all form fields and selection states.
8. **Exit Application:** Clean application termination with user confirmation.

---

## 4. Technologies Used
- **Programming Language:** Python 3.x (Built-in standard libraries only)
- **GUI Framework:** `tkinter` & `tkinter.ttk` (Built-in)
- **Database Engine:** `sqlite3` (Built-in relational database engine)
- **File Processing:** `csv` & `os` modules
- **Data Validation:** `re` (Regular Expressions) module

---

## 5. CSE3011 Syllabus Concepts Used

| Syllabus Topic | Implementation Detail in Project |
| :--- | :--- |
| **Classes and Objects (OOP)** | `Student` class in `student.py`, `DatabaseManager` class in `database.py`, and `StudentApp` class in `gui.py`. |
| **Instance Methods** | `to_dict()`, `to_tuple()` methods in `Student`; CRUD methods in `DatabaseManager`. |
| **Functions & Modules** | Modular structure (`student.py`, `database.py`, `gui.py`, `export.py`, `main.py`). |
| **Lists and Dictionaries** | Used for managing database query result sets and input dictionary conversions (`to_dict()`). |
| **Exception Handling (`try-except`)** | Catches `sqlite3.Error`, `sqlite3.IntegrityError`, `ValueError`, and file permission errors gracefully. |
| **File Handling & CSV** | Uses `with open()` context managers to read/write external CSV files via `csv.writer`. |
| **SQLite Connectivity** | Executes parameterized SQL queries (`CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`) with connection context managers. |
| **Tkinter GUI & Events** | Custom widgets (Labels, Entries, Buttons, Treeview) and event binding (`<<TreeviewSelect>>`, `<Return>`). |
| **Input Validation** | Uses Regular Expressions (`re`) and string methods to check non-empty fields, positive numeric bounds, and email patterns. |

---

## 6. How to Install and Run

### Prerequisites
- Python 3.7 or higher installed on your computer.

### Step-by-Step Execution Guide

1. **Open Command Prompt / Terminal:**
   ```bash
   cd student_management
   ```

2. **Run the Application:**
   ```bash
   python main.py
   ```

> **Note:** The SQLite database file (`students.db`) and table will be created automatically in the project folder upon first execution.

---

## 7. Project Structure

```text
student_management/
│
├── main.py          # Application entry point & root loop initialization
├── student.py       # Student data model class & validation routines
├── database.py      # SQLite3 connection manager & CRUD SQL operations
├── gui.py           # Tkinter interface layout, styling & event handlers
├── export.py        # CSV export handler using standard library
├── students.db      # SQLite relational database storage (auto-generated)
└── README.md        # Detailed project documentation & Viva Q&A guide
```

---

## 8. How the Database Works
- **Database Engine:** Embedded SQLite3 file-based database (`students.db`).
- **Table Name:** `students`
- **Database Schema:**
  ```sql
  CREATE TABLE IF NOT EXISTS students (
      student_id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER NOT NULL,
      course TEXT NOT NULL,
      email TEXT NOT NULL,
      marks REAL NOT NULL
  );
  ```
- **Primary Key:** `student_id` acts as a unique constraint. Duplicate ID insertions trigger a handled `sqlite3.IntegrityError`.
- **Query Parameterization:** All SQL operations use placeholder tuples (`?`) to prevent SQL Injection vulnerabilities and ensure safe execution.

---

## 9. Sample Screenshots Layout

### Main Dashboard Layout
```text
+-----------------------------------------------------------------------------------------+
|                               🎓 STUDENT RECORD MANAGEMENT SYSTEM                         |
+------------------------------------+----------------------------------------------------+
|  Student Details Form              |  Student Records Directory                         |
|  --------------------              |  -------------------------                         |
|  Student ID:  [ STU101           ] |  Search (ID/Name): [         ] [🔍 Search] [🔄 All]|
|  Full Name:   [ Alice Smith      ] |  +------------+-------------+-----+--------+------+ |
|  Age:         [ 20               ] |  | Student ID | Name        | Age | Course | Marks| |
|  Course:      [ B.Tech CSE       ] |  +------------+-------------+-----+--------+------+ |
|  Email:       [ alice@email.com  ] |  | STU101     | Alice Smith | 20  | B.Tech | 92.5 | |
|  Marks (%):   [ 92.5             ] |  +------------+-------------+-----+--------+------+ |
|                                    |                                                    |
|  [➕ Add]  [✏️ Update]              |                                                    |
|  [🗑️ Delete] [🧹 Clear]             |  [📥 Export to CSV]            [❌ Exit Application]|
+------------------------------------+----------------------------------------------------+
```

---

## 10. Possible Future Improvements
1. **Student Photo Upload:** Store student avatar image paths and display them in the GUI.
2. **Grade System:** Automatically compute Letter Grades (A, B, C, D, F) based on entered marks.
3. **Advanced Filtering:** Filter records by Course or Age bracket.
4. **PDF Report Generation:** Generate individual student report cards in PDF format.

---

## 11. Viva Questions & Answers (CSE3011 Professor Q&A)

### Q1: What is the purpose of `main.py` and `if __name__ == "__main__":`?
> **Answer:** `main.py` serves as the application entry point. The check `if __name__ == "__main__":` ensures that the main window is launched only when `main.py` is executed directly, and not when imported as a module in another script.

### Q2: Why did you separate the code into multiple files (`student.py`, `database.py`, `gui.py`, etc.)?
> **Answer:** This demonstrates **Modular Programming** and **Separation of Concerns (SoC)**. `student.py` manages the data structure and validation, `database.py` manages persistence, `gui.py` handles user interaction, and `export.py` handles file I/O. This makes the code readable, reusable, and easy to maintain.

### Q3: How does SQLite prevent duplicate Student IDs?
> **Answer:** `student_id` is defined as `PRIMARY KEY` in SQL schema. When an insertion with an existing ID is attempted, SQLite raises a `sqlite3.IntegrityError`, which our code catches to display a friendly warning messagebox to the user.

### Q4: Why use parameterized SQL queries (`?`) instead of string formatting (`f"INSERT INTO ... VALUES ('{id}')"`)?
> **Answer:** Parameterized queries use placeholder `?` marks which automatically sanitize inputs. String formatting leaves the application open to **SQL Injection attacks** and syntax errors caused by special characters in names (e.g., O'Connor).

### Q5: How does event-driven programming work in Tkinter?
> **Answer:** In Tkinter, the main application loop `root.mainloop()` continuously listens for user interactions (mouse clicks, keypresses). We bind events like `command=self.add_student_action` on buttons or `self.tree.bind("<<TreeviewSelect>>", ...)` on treeview rows to trigger specific callback functions when triggered.

### Q6: How is file handling implemented in the CSV export function?
> **Answer:** The `export_to_csv()` function uses Python's `with open(...)` context manager statement. This guarantees that the file stream is automatically closed even if an exception occurs during writing. The built-in `csv.writer` formats tuples into standard CSV rows.
