# SANCHAYA Object-Oriented Student Management System

A robust, command-line **Student Management System** built in Python. This project demonstrates core **Object-Oriented Programming (OOP)** principles, **CRUD operations**, and **persistent file storage** using CSV files.

## 🚀 Features

* **Create (Register):** Add new student records with validation for duplicate IDs and data types.
* **Read (View & Search):** Display all registered students or search for specific records instantly by Student ID.
* **Update / Delete:** Safely remove student records from active memory and disk storage.
* **Persistent Storage:** Automatically saves and loads student records to/from a local `students.csv` file so data is never lost when closing the application.
* **Defensive Error Handling:** Gracefully handles invalid numeric inputs (like text entered for age or marks) without crashing.

---

## 🛠️ Tech Stack & Concepts Applied

* **Language:** Python 3
* **OOP Concepts:** Classes, instance methods, encapsulation, object composition (`StudentManagementSystem` managing a collection of `Student` objects).
* **Built-in Modules:** `csv` (for structured data serialization), `os` (for file path checks).
* **Control Flow:** `while` loops, context managers (`with` statement), exception handling (`try-except`).

---

## 📂 Project Structure

```text
student-management-system/
│
├── student_system.py      # Main application script containing classes and CLI loop
├── students.csv           # Auto-generated persistent data file
└── README.md              # Project documentation

How to Run?
1. Clone the repository:
Bash
git clone [https://github.com/your-username/student-management-system.git](https://github.com/your-username/student-management-system.git)
cd student-management-system

2. Run the application:
Bash
python student_system.py

3. Follow the on-screen terminal menu to add, view, search, or delete student records!

Project Takeaway:
Built as part of an independent Python engineering curriculum to master class architecture, memory management, and file input/output workflows.
