"""
main.py - Entry point for Student Record Management System
Syllabus Concepts Used:
- Modules/imports
- Main execution check (__name__ == '__main__')
- Event loop starting (root.mainloop())
"""

import tkinter as tk
from gui import StudentApp

def main():
    """
    Main function to launch the Tkinter GUI application.
    """
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
