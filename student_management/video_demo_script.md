# Video Recording Script & Demonstration Guide 🎥
**Project:** Student Record Management System (CSE3011 Python Programming)

---

## 🛠️ Step 1: Recommended Screen Recorders
- **Windows Built-in:** Press `Win + Alt + R` (Windows Game Bar) or `Win + Shift + R` (Snipping Tool Screen Recorder).
- **Free Software:** OBS Studio or Loom.

---

## ⏱️ Step 2: Step-by-Step Video Script (Target Length: 2 to 3 Minutes)

### 🎬 Scene 1: Introduction & Project Structure (0:00 - 0:25)
* **What to show on screen:** Your VS Code editor or Command Prompt showing the `student_management` folder.
* **What to say:**
  > "Hello Professor, this is my CSE3011 Python Programming project: the **Student Record Management System**. The project is built using pure Python, Tkinter for the GUI, SQLite3 for database persistence, CSV handling, and Object-Oriented Programming principles without external frameworks."
  > "As you can see, the codebase is modularly structured into `main.py`, `student.py` for data models and validation, `database.py` for SQL CRUD operations, `gui.py` for the interface, and `export.py` for CSV generation."

---

### 🚀 Scene 2: Launching & Database Creation (0:25 - 0:45)
* **What to show on screen:** Open terminal inside `student_management` and run:
  ```bash
  python main.py
  ```
* **What to say:**
  > "I will now launch the application by running `python main.py`. Notice how the system automatically initializes the SQLite database `students.db` and creates the `students` table if it doesn't already exist."

---

### ➕ Scene 3: Input Validation & Adding Records (0:45 - 1:25)
* **What to show on screen:** 
  1. Try clicking **Add Student** with empty fields -> **Show Tkinter Warning Popup**.
  2. Enter invalid marks (e.g. `150`) -> **Show Validation Warning Popup**.
  3. Enter valid data for Student 1 and click **Add Student**:
     - **ID:** `STU101` | **Name:** `Alice Smith` | **Age:** `20` | **Course:** `B.Tech CSE` | **Email:** `alice@example.com` | **Marks:** `92.5`
  4. Add Student 2:
     - **ID:** `STU102` | **Name:** `Bob Jones` | **Age:** `21` | **Course:** `B.Tech ECE` | **Email:** `bob@example.com` | **Marks:** `78.0`
* **What to say:**
  > "First, I'll demonstrate input validation. If I leave fields empty or enter invalid marks over 100, the app catches the error and displays a warning dialog. Now I will add two valid student records, Alice and Bob. Upon clicking Add, the database is updated and the record appears in our formatted Treeview table."

---

### 🔍 Scene 4: Searching Records (1:25 - 1:45)
* **What to show on screen:**
  1. Type `Bob` in the search box -> click **Search**. (Only Bob's record appears).
  2. Type `101` in search box -> press **Enter** key. (Only Alice appears).
  3. Click **Show All** to reset the view.
* **What to say:**
  > "Next is the search feature. We can search records dynamically by Student ID or Name. Searching for 'Bob' filters the table instantly. Clicking 'Show All' resets the directory view."

---

### ✏️ Scene 5: Selection, Updating & Deleting Records (1:45 - 2:20)
* **What to show on screen:**
  1. Click on **Alice Smith** in the Treeview table -> fields auto-fill in the left form panel!
  2. Change Marks from `92.5` to `95.0` -> click **Update Student**.
  3. Add a temporary student `STU999` -> click on it -> click **Delete Student** -> click **Yes** on confirmation dialog.
* **What to say:**
  > "To update a student, I simply click their row in the directory. Event binding auto-populates the input fields. I'll update Alice's marks to 95.0 and click Update. For deleting, selecting a record and clicking Delete prompts a confirmation dialog before safely removing it from SQLite."

---

### 📥 Scene 6: Exporting to CSV File (2:20 - 2:45)
* **What to show on screen:**
  1. Click **Export to CSV**.
  2. Choose filename `student_report.csv` and click **Save**.
  3. Open `student_report.csv` in Excel, Notepad, or VS Code to show the exported headers and rows.
* **What to say:**
  > "Now I will test the export feature. Clicking 'Export to CSV' opens a file dialog. I'll save it as `student_report.csv`. Opening the CSV file shows that our records have been exported with proper headers."

---

### 🧹 Scene 7: Clear & Exit (2:45 - 3:00)
* **What to show on screen:**
  1. Click **Clear Fields**.
  2. Click **Exit Application** -> click **Yes** on confirmation popup.
* **What to say:**
  > "Finally, the 'Clear Fields' button resets all entry inputs, and clicking 'Exit Application' cleanly closes the window after user confirmation. Thank you!"

---

## 📋 Sample Test Data to Use During Recording

| Student ID | Full Name | Age | Course | Email Address | Marks (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `STU101` | `Alice Smith` | `20` | `B.Tech CSE` | `alice@example.com` | `92.5` |
| `STU102` | `Bob Jones` | `21` | `B.Tech ECE` | `bob@example.com` | `78.0` |
| `STU103` | `Charlie Brown`| `22` | `B.Tech IT` | `charlie@example.com`| `85.4` |
