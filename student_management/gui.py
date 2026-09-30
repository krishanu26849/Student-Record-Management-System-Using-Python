"""
gui.py - Tkinter Graphical User Interface Module
Syllabus Concepts Used:
- Tkinter GUI framework (Window, Frames, Labels, Entry, Buttons, Treeview, Scrollbar)
- Event-driven programming (Button commands, <<TreeviewSelect>> event binding)
- Dialog boxes (messagebox, filedialog)
- Object-Oriented Programming (StudentApp class)
- Integration of Database, Student Model, and Export Modules
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from database import DatabaseManager
from student import Student
from export import export_to_csv

class StudentApp:
    """
    Main GUI Application class for Student Record Management System.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System - CSE3011 Project")
        self.root.geometry("1100x650")
        self.root.minsize(950, 580)
        
        # Initialize Database Manager
        self.db = DatabaseManager()

        # Apply basic theme/styling
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Configure custom colors and fonts for Treeview
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#2563EB", foreground="white")
        self.style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        self.style.map("Treeview", background=[("selected", "#3B82F6")], foreground=[("selected", "white")])

        # Setup GUI Widgets
        self.create_header()
        self.create_main_frames()
        self.create_form_widgets()
        self.create_table_widgets()

        # Load initial data into table
        self.load_students()

    def create_header(self):
        """
        Creates the top title header banner.
        """
        header_frame = tk.Frame(self.root, bg="#1E3A8A", height=60)
        header_frame.pack(side=tk.TOP, fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="🎓 STUDENT RECORD MANAGEMENT SYSTEM",
            font=("Helvetica", 18, "bold"),
            bg="#1E3A8A",
            fg="white",
            pady=12
        )
        title_label.pack()

    def create_main_frames(self):
        """
        Creates split layout frames (Left for inputs, Right for table/search).
        """
        main_container = tk.Frame(self.root, bg="#F3F4F6", padx=10, pady=10)
        main_container.pack(fill=tk.BOTH, expand=True)

        # Left Frame for Entry Form and Actions
        self.left_frame = tk.LabelFrame(
            main_container,
            text=" Student Details Form ",
            font=("Helvetica", 11, "bold"),
            bg="white",
            fg="#1F2937",
            padx=15,
            pady=15,
            relief=tk.RIDGE
        )
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))

        # Right Frame for Search and Treeview Table
        self.right_frame = tk.LabelFrame(
            main_container,
            text=" Student Records Directory ",
            font=("Helvetica", 11, "bold"),
            bg="white",
            fg="#1F2937",
            padx=15,
            pady=15,
            relief=tk.RIDGE
        )
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_form_widgets(self):
        """
        Creates input form fields and action buttons in the left panel.
        """
        # Form Fields Configuration
        fields = [
            ("Student ID:", "entry_id"),
            ("Full Name:", "entry_name"),
            ("Age:", "entry_age"),
            ("Course:", "entry_course"),
            ("Email Address:", "entry_email"),
            ("Marks (%):", "entry_marks")
        ]

        self.entries = {}

        for idx, (label_text, var_name) in enumerate(fields):
            lbl = tk.Label(self.left_frame, text=label_text, font=("Helvetica", 10, "bold"), bg="white", fg="#374151")
            lbl.grid(row=idx*2, column=0, sticky="w", pady=(5, 2))

            entry = tk.Entry(self.left_frame, font=("Helvetica", 10), width=28, relief=tk.SOLID, bd=1)
            entry.grid(row=idx*2+1, column=0, sticky="ew", pady=(0, 8))
            self.entries[var_name] = entry

        # Form Action Buttons Frame
        btn_frame = tk.Frame(self.left_frame, bg="white", pady=10)
        btn_frame.grid(row=12, column=0, sticky="ew")

        # Add Button
        btn_add = tk.Button(
            btn_frame, text="➕ Add Student", font=("Helvetica", 10, "bold"),
            bg="#16A34A", fg="white", activebackground="#15803D", activeforeground="white",
            relief=tk.RAISED, cursor="hand2", command=self.add_student_action, width=24, pady=4
        )
        btn_add.pack(pady=4)

        # Update Button
        btn_update = tk.Button(
            btn_frame, text="✏️ Update Student", font=("Helvetica", 10, "bold"),
            bg="#2563EB", fg="white", activebackground="#1D4ED8", activeforeground="white",
            relief=tk.RAISED, cursor="hand2", command=self.update_student_action, width=24, pady=4
        )
        btn_update.pack(pady=4)

        # Delete Button
        btn_delete = tk.Button(
            btn_frame, text="🗑️ Delete Student", font=("Helvetica", 10, "bold"),
            bg="#DC2626", fg="white", activebackground="#B91C1C", activeforeground="white",
            relief=tk.RAISED, cursor="hand2", command=self.delete_student_action, width=24, pady=4
        )
        btn_delete.pack(pady=4)

        # Clear Button
        btn_clear = tk.Button(
            btn_frame, text="🧹 Clear Fields", font=("Helvetica", 10, "bold"),
            bg="#6B7280", fg="white", activebackground="#4B5563", activeforeground="white",
            relief=tk.RAISED, cursor="hand2", command=self.clear_fields, width=24, pady=4
        )
        btn_clear.pack(pady=4)

    def create_table_widgets(self):
        """
        Creates Search frame, Treeview table, and bottom utility buttons.
        """
        # Top Search Frame inside Right Panel
        search_frame = tk.Frame(self.right_frame, bg="white", pady=5)
        search_frame.pack(fill=tk.X, pady=(0, 10))

        lbl_search = tk.Label(search_frame, text="Search (ID/Name):", font=("Helvetica", 10, "bold"), bg="white")
        lbl_search.pack(side=tk.LEFT, padx=(0, 5))

        self.entry_search = tk.Entry(search_frame, font=("Helvetica", 10), width=25, relief=tk.SOLID, bd=1)
        self.entry_search.pack(side=tk.LEFT, padx=5)
        # Bind Return key to trigger search
        self.entry_search.bind("<Return>", lambda event: self.search_student_action())

        btn_search = tk.Button(
            search_frame, text="🔍 Search", font=("Helvetica", 9, "bold"),
            bg="#0D9488", fg="white", relief=tk.RAISED, cursor="hand2",
            command=self.search_student_action, padx=10
        )
        btn_search.pack(side=tk.LEFT, padx=5)

        btn_reset = tk.Button(
            search_frame, text="🔄 Show All", font=("Helvetica", 9, "bold"),
            bg="#4F46E5", fg="white", relief=tk.RAISED, cursor="hand2",
            command=self.load_students, padx=10
        )
        btn_reset.pack(side=tk.LEFT, padx=5)

        # Treeview Table & Scrollbar Container
        table_container = tk.Frame(self.right_frame, bg="white")
        table_container.pack(fill=tk.BOTH, expand=True)

        columns = ("student_id", "name", "age", "course", "email", "marks")
        self.tree = ttk.Treeview(table_container, columns=columns, show="headings", selectmode="browse")

        # Define Column Headings and Widths
        self.tree.heading("student_id", text="Student ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.heading("course", text="Course")
        self.tree.heading("email", text="Email")
        self.tree.heading("marks", text="Marks (%)")

        self.tree.column("student_id", width=100, anchor=tk.CENTER)
        self.tree.column("name", width=150, anchor=tk.W)
        self.tree.column("age", width=60, anchor=tk.CENTER)
        self.tree.column("course", width=120, anchor=tk.W)
        self.tree.column("email", width=180, anchor=tk.W)
        self.tree.column("marks", width=80, anchor=tk.CENTER)

        # Vertical Scrollbar
        scrollbar = ttk.Scrollbar(table_container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind event when row selected in Treeview
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Bottom Utility Buttons Frame (Export & Exit)
        bottom_frame = tk.Frame(self.right_frame, bg="white", pady=10)
        bottom_frame.pack(fill=tk.X, pady=(10, 0))

        btn_export = tk.Button(
            bottom_frame, text="📥 Export to CSV", font=("Helvetica", 10, "bold"),
            bg="#D97706", fg="white", activebackground="#B45309", activeforeground="white",
            relief=tk.RAISED, cursor="hand2", command=self.export_csv_action, padx=15, pady=4
        )
        btn_export.pack(side=tk.LEFT, padx=5)

        btn_exit = tk.Button(
            bottom_frame, text="❌ Exit Application", font=("Helvetica", 10, "bold"),
            bg="#374151", fg="white", activebackground="#1F2937", activeforeground="white",
            relief=tk.RAISED, cursor="hand2", command=self.exit_app, padx=15, pady=4
        )
        btn_exit.pack(side=tk.RIGHT, padx=5)

    def load_students(self, records=None):
        """
        Populates the Treeview table with records from database.
        """
        # Clear existing items in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        if records is None:
            records = self.db.fetch_all_students()

        for record in records:
            self.tree.insert("", tk.END, values=record)

    def get_form_data(self):
        """
        Helper method to retrieve text values from entry fields.
        """
        return (
            self.entries["entry_id"].get().strip(),
            self.entries["entry_name"].get().strip(),
            self.entries["entry_age"].get().strip(),
            self.entries["entry_course"].get().strip(),
            self.entries["entry_email"].get().strip(),
            self.entries["entry_marks"].get().strip()
        )

    def add_student_action(self):
        """
        Callback handler for Adding a new Student.
        """
        s_id, name, age_str, course, email, marks_str = self.get_form_data()

        # Validate inputs
        is_valid, msg = Student.validate_inputs(s_id, name, age_str, course, email, marks_str)
        if not is_valid:
            messagebox.showwarning("Validation Error", msg)
            return

        student = Student(s_id, name, int(age_str), course, email, float(marks_str))
        success, message = self.db.add_student(student)

        if success:
            messagebox.showinfo("Success", message)
            self.load_students()
            self.clear_fields()
        else:
            messagebox.showerror("Error", message)

    def update_student_action(self):
        """
        Callback handler for Updating selected Student record.
        """
        s_id, name, age_str, course, email, marks_str = self.get_form_data()

        if not s_id:
            messagebox.showwarning("Warning", "Please select or specify a Student ID to update.")
            return

        # Validate inputs
        is_valid, msg = Student.validate_inputs(s_id, name, age_str, course, email, marks_str)
        if not is_valid:
            messagebox.showwarning("Validation Error", msg)
            return

        student = Student(s_id, name, int(age_str), course, email, float(marks_str))
        success, message = self.db.update_student(student)

        if success:
            messagebox.showinfo("Success", message)
            self.load_students()
            self.clear_fields()
        else:
            messagebox.showerror("Error", message)

    def delete_student_action(self):
        """
        Callback handler for Deleting a Student.
        """
        s_id = self.entries["entry_id"].get().strip()

        if not s_id:
            messagebox.showwarning("Warning", "Please select a student from the table or enter Student ID to delete.")
            return

        # Confirmation popup
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Student ID '{s_id}'?")
        if confirm:
            success, message = self.db.delete_student(s_id)
            if success:
                messagebox.showinfo("Success", message)
                self.load_students()
                self.clear_fields()
            else:
                messagebox.showerror("Error", message)

    def search_student_action(self):
        """
        Callback handler for searching student by ID or Name.
        """
        query = self.entry_search.get().strip()
        if not query:
            messagebox.showinfo("Info", "Please enter a Student ID or Name to search.")
            self.load_students()
            return

        results = self.db.search_students(query)
        self.load_students(results)

        if not results:
            messagebox.showinfo("Search Results", f"No records found matching '{query}'.")

    def clear_fields(self):
        """
        Resets all input entry fields and selection.
        """
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.entries["entry_id"].config(state="normal")
        self.entry_search.delete(0, tk.END)
        
        # Deselect item in treeview if any selected
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.selection_remove(selected_item)

    def on_tree_select(self, event):
        """
        Fills form input fields when a user clicks/selects a row in Treeview.
        """
        selected_items = self.tree.selection()
        if not selected_items:
            return

        selected_item = selected_items[0]
        values = self.tree.item(selected_item, "values")

        if values:
            self.clear_fields()
            self.entries["entry_id"].insert(0, values[0])
            self.entries["entry_name"].insert(0, values[1])
            self.entries["entry_age"].insert(0, values[2])
            self.entries["entry_course"].insert(0, values[3])
            self.entries["entry_email"].insert(0, values[4])
            self.entries["entry_marks"].insert(0, values[5])

    def export_csv_action(self):
        """
        Callback handler to export current dataset to CSV file.
        """
        records = self.db.fetch_all_students()
        if not records:
            messagebox.showwarning("Warning", "No records found in database to export!")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Export Student Records to CSV"
        )

        if filepath:
            success, message = export_to_csv(records, filepath)
            if success:
                messagebox.showinfo("Export Success", message)
            else:
                messagebox.showerror("Export Error", message)

    def exit_app(self):
        """
        Prompt confirmation before exiting application.
        """
        confirm = messagebox.askyesno("Exit Application", "Are you sure you want to exit?")
        if confirm:
            self.root.destroy()
