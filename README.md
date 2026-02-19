# PUC Study Tracker

## Video Demo
https://www.youtube.com/watch?v=YOUR_VIDEO_LINK_HERE

## Description

PUC Study Tracker is a command-line based academic management system developed to help Pre-University (PUC) students efficiently track their subjects, marks, and attendance records. The purpose of this project is to provide a structured and persistent system that allows students to monitor their academic performance in a simple yet effective way. Many students manually track marks and attendance, which can lead to miscalculations and disorganization. This project solves that problem by automating calculations and organizing records in a clean, modular structure.

The application allows users to add subjects, record marks for each subject, record attendance details, and generate subject-specific performance reports. It calculates average marks, determines grades according to defined boundaries, and computes attendance percentages. All records are stored persistently so that data is not lost when the program closes.

The program is menu-driven and operates inside a continuous loop. The menu repeatedly displays options to the user until the exit option is selected. This design ensures that users can perform multiple operations in one session without restarting the program.

---

## Features

- Add new subjects  
- Prevent duplicate subject entries  
- Add marks for individual subjects  
- Record attendance (classes attended and total classes)  
- Calculate average marks automatically  
- Assign grades based on average  
- Calculate attendance percentage  
- View all stored subjects  
- View detailed subject performance reports  
- Persistent data storage  
- Unit testing for grading logic  

---

## Project Structure and File Explanation

### main.py

This is the entry point of the program. It contains the menu system and the main loop that keeps the application running. When the program starts, it displays a list of numbered options. Based on the user’s selection, it calls functions from other modules.

The loop continues until the user selects the exit option. This looping mechanism ensures the program remains interactive and user-friendly. Input handling and output formatting are managed here to keep the user interface clean and readable.

---

### database.py

This file is responsible for handling data storage and retrieval. It manages all subject information, including marks and attendance records. The database layer ensures that data is saved and loaded properly between program executions.

One important design decision implemented here is duplicate prevention. Before adding a new subject, the program checks whether the subject already exists. If it does, the system avoids creating a duplicate entry. This protects data integrity and prevents confusion during report generation.

Data is stored in a structured format, allowing easy updates when marks or attendance are added.

---

### analytics.py

This module handles all calculations and performance analysis. Separating analytics from the main interface was a deliberate design decision to improve modularity and maintainability.

It includes:

- A function to calculate average marks  
- A function to calculate attendance percentage  
- A function to calculate grade  

The grading system follows these boundaries:

- 90 and above → A  
- 75 to 89 → B  
- 60 to 74 → C  
- 50 to 59 → D  
- Below 50 → F  

This grading logic uses conditional statements to determine the correct grade. Boundary values are carefully handled to ensure accurate results.

---

### test_suite.py

This file contains unit tests for validating grading functionality. It checks whether the `calculate_grade()` function produces correct results for different input values, including boundary cases. Testing improves reliability and ensures that future changes do not unintentionally break the grading system.

---

### requirements.txt

This file lists dependencies required to run the project. Since the project mainly uses Python’s standard library, minimal external libraries are required.

---

## Algorithm and Workflow

1. The program starts and loads stored data.  
2. A menu is displayed to the user.  
3. The user selects an option.  
4. Based on the option:
   - A subject is added.
   - Marks are recorded.
   - Attendance is updated.
   - Subjects are displayed.
   - A subject report is generated.
5. When generating reports, the analytics module calculates average marks, grade, and attendance percentage.
6. Updated data is saved to the database.
7. The loop repeats until the user exits.

This structured approach ensures logical flow and consistent data handling.

---

## Design Decisions

A key design decision was separating responsibilities across multiple files. Instead of placing all logic in one script, the project follows modular programming principles. Each file has a clearly defined purpose: interface handling, data management, analytics, and testing. This improves readability, scalability, and maintainability.

Another important decision was implementing duplicate subject prevention. Without this check, users could accidentally create multiple entries for the same subject, leading to inaccurate reports.

The grading logic was designed using clear boundary checks. Careful attention was given to ensure that scores exactly on grade boundaries (such as 75 or 90) are assigned correctly.

---

## Limitations

The project currently operates only through a command-line interface. It does not include a graphical user interface. Input validation is basic and assumes correct numeric input for marks and attendance. Additionally, the system supports a single-user environment and does not include authentication.

---

## Future Improvements

- Add a graphical user interface (GUI)  
- Improve input validation and error handling  
- Add subject editing and deletion options  
- Support multiple user accounts  
- Add data export features (CSV or PDF)  
- Include performance trend visualization  

---

## Conclusion

PUC Study Tracker demonstrates fundamental programming concepts such as loops, conditionals, file handling, modular design, and unit testing. The project reflects structured problem-solving and practical application of computer science principles. By organizing subjects, automating calculations, and generating performance reports, this system provides a reliable academic tracking tool for students.

This project highlights clean code organization, thoughtful design decisions, and consistent logic implementation while maintaining simplicity and usability.
