# console-based-application-for-managing-a-system-

INTRODUCTION

This Python code is a console-based application for managing a system where administrators can register users (both admins and students), view registered users, and delete student records. Students can update their profiles, view extracurricular activity (ECA) details, view examination grades.




METHODOLOGY

The methodology of this code revolves around object-oriented programming (OOP) principles and follows a modular approach for better code organization and re-usability. Here's a breakdown of the methodology:

Object-Oriented Design:
	The code is organized into classes, namely ‘User’, ‘Student’, and ‘Admin’, representing the different types of users in the system. 
	Each class encapsulates data (attributes) and behavior (methods) related to its respective user type.
	Inheritance is utilized where the ‘Student ’and Admin classes inherit from the User class to reuse       common attributes and methods.
Separation of Concerns:
	Different functionalities are implemented as methods within their respective classes. For example, user registration logic is encapsulated within the Admin class.
	Input/output operations, file handling, and data persistence are separated into separate functions like:login(),create_empty_files(),write_users(), save_eca(), and save_grade().


User Authentication and Input Handling:
	The login() function handles user authentication based on the provided username and password.
	Input from the user is collected using the input() function and validated where necessary to ensure correctness.


File Handling and Data Persistence:
	Data related to users, grades, and ECAs are stored in text files (users.txt, grades.txt, eca.txt, password.txt).
	File handling operations like reading, writing, and updating user data are encapsulated within functions such as write_users() and delete_user().


Visual Presentation:
	ASCII art generated using the Figlet library is used to create visually appealing headers and banners for login screens and information displays.
	Colorized output is achieved using the colorama library, enhancing the readability and visual appeal of the console application.


User Interaction:
	The main program (main()) orchestrates user interactions based on their roles (admin or student) and the selected menu options.
	Users are presented with menus and prompted to input their choices, with corresponding actions executed based on the input.


Error Handling:
	Basic error handling is implemented to handle invalid inputs and edge cases, such as incorrect usernames or passwords.

Initialization and Setup:
	The code begins with initialization steps such as setting up colorama for colored output, initializing Figlet for ASCII art, and creating empty files if they don't exist.

Overall, the methodology emphasizes modularity, encapsulation, and separation of concerns to create a well-structured and maintainable console-based application for user management and information handling.
REVIEW OF THE TECHNOLOGY

Let's review the technology used in this code:

Colorama:
	Colorama is used for colored output in the console. It provides an easy way to add colored text and background in Python terminal applications.
	The init(autoreset=True) function is called to automatically reset the colors after each print statement, ensuring consistent color handling.


Pyfiglet:
	Pyfiglet is utilized to create ASCII art for visually appealing headers and banners.
	The Figlet class is used to render text in ASCII art with different font styles.


PrettyTable:
	PrettyTable is employed for generating formatted tables to display user information in a structured and readable format.
	Tables are created using the PrettyTable class, allowing customization of column headers and data alignment.



OS Module:
	The os module is utilized for file operations, such as checking file existence and creating empty files.
	Functions like os.path.exists() and open() are used to manage files and directories.


UUID Module:
	The UUID module is used to generate unique identifiers (UUIDs) for student IDs during user registration.
	The uuid.uuid4() function generates a random UUID.


Object-Oriented Programming (OOP):
	The code follows an OOP approach, defining classes such as User, Student, and Admin to encapsulate related data and behavior.
	Inheritance is used to inherit properties and methods from the base User class to more specific subclasses (Student and Admin).


Input Handling:
	User input is collected using the input() function and processed accordingly to perform actions like login, registration, and data modification.




Data Persistence:
	User data, grades, and ECA (Extra-Curricular Activities) records are stored in text files (users.txt, grades.txt, eca.txt).
	Functions like write_users(), save_grade(), and save_eca() handle data storage and retrieval operations.


Authentication:
	User authentication is implemented using username-password pairs, with validation performed during login attempts.


Error Handling:
	Basic error handling is included to handle invalid inputs and edge cases, ensuring robustness and graceful error recovery.
	Overall, the technology stack employed in this code facilitates the development of a functional user management system with features like user registration, data viewing, modification, and deletion, all accessible via a command-line interface.
