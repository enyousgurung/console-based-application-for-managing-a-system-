from colorama import init, Fore, Style  # Import colorama for colored output
from pyfiglet import Figlet  # Import Figlet for ASCII art
from prettytable import PrettyTable  # Import PrettyTable library for tabular data
import os  # Import os module for file operations
import uuid  # Import uuid module for generating unique IDs

# Initialize colorama for colored output
init(autoreset=True)

# Initialize Figlet with the 'standard' font for ASCII art
f = Figlet(font='standard')

class User:
    def __init__(self, username, role, email):
        self.username = username
        self.role = role
        self.email = email

class Student(User):
    def __init__(self, username, role, email, student_id, grades, eca, phone_number):
        super().__init__(username, role, email)
        self.student_id = student_id
        self.grades = grades
        self.eca = eca
        self.phone_number = phone_number

    def update_profile(self, new_username, new_email, new_phone_number):
        if new_username.strip() != '':
            self.username = new_username
        if new_email.strip() != '':
            self.email = new_email
        if new_phone_number.strip() != '':
            self.phone_number = new_phone_number

    def add_grade(self, grade):
        self.grades.append(grade)

    def add_eca(self, eca_description):
        self.eca = eca_description

    def get_student_info(self):
        grades_str = ', '.join(map(str, self.grades))
        return [self.username, self.role, self.email, self.student_id, grades_str, self.eca, self.phone_number]

    def view_eca(self):
        if self.eca:
            print("ECA Details:")
            print(self.eca)
        else:
            print("No ECA details available.")

    def view_grades(self):
        if self.grades:
            print("Examination Grades:")
            for grade in self.grades:
                print(grade)
        else:
            print("No examination grades available.")

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, 'admin', '')
        self.password = password

    def authenticate(self, username, password):
        return username == self.username and password == self.password

    def register_user(self, new_username, role, email, password, phone_number, grades=None, eca=None):
        if role == 'student':
            new_user_id = str(uuid.uuid4())[:8]
            new_user = [new_username, role, email, password, new_user_id, phone_number]
            write_users([new_user])
            if grades:
                save_grade(new_user_id, grades)
            if eca:
                save_eca(new_user_id, eca)

            print(Fore.GREEN + "User registered successfully!")
        else:
            print(Fore.RED + "Only admin can register new users.")

    def view_users(self):
        if self.role == 'admin':
            with open('users.txt', 'r') as file:
                lines = file.readlines()

            table = PrettyTable(['Username', 'Role', 'Email', 'Student ID'])  # Modified table header
            for line in lines:
                user_data = line.strip().split(',')
                if user_data and len(user_data) >= 3:  # Check if user_data contains at least 3 elements and is not empty
                    table.add_row([user_data[0], user_data[1], user_data[2], user_data[4]])  # Include student ID in the row
                elif user_data:
                    print(Fore.RED + f"Invalid user data: {user_data}. Skipping...")
                    continue

            print(Fore.BLUE + f"\n{f.renderText('Users Enrolled')}")
            print(table)
        else:
            print(Fore.RED + "Only admin can view registered users.")

    def delete_user(self, student_id):  # Changed parameter to student ID
        if self.role == 'admin':
            with open('users.txt', 'r') as file:
                lines = file.readlines()
            with open('users.txt', 'w') as file:
                for line in lines:
                    user_data = line.strip().split(',')
                    if user_data and user_data[4] != student_id:  # Check student ID for deletion
                        file.write(line)
            print(Fore.GREEN + f"User with ID '{student_id}' deleted successfully!")  # Notify by student ID
        else:
            print(Fore.RED + "Only admin can delete users.")

def write_users(users):
    with open('users.txt', 'a') as file:
        for user in users:
            file.write(','.join(user) + '\n')

def save_eca(student_id, eca_description):
    with open('eca.txt', 'a') as file:
        file.write(f"{student_id},{eca_description}\n")

    print(Fore.GREEN + "ECA record saved successfully!")

def save_grade(student_id, grade):
    with open('grades.txt', 'a') as file:
        file.write(f"{student_id},{grade}\n")
    print(Fore.GREEN + "Grade record saved successfully!")

def create_empty_files():
    file_names = ['users.txt', 'grades.txt', 'eca.txt', 'students.txt']
    for file_name in file_names:
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                pass

def login():
    print(Fore.BLUE + f"\n{Figlet(font='starwars').renderText('Login')}")

    print(Fore.YELLOW + "1. Admin Login")
    print("2. Student Login")
    choice = input(Fore.YELLOW + "Enter your choice: ")

    if choice == '1':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        admin = Admin("enyous@gmail.com", "enyous")
        if admin.authenticate(username, password):
            return username, password, 'admin'
        else:
            print(Fore.RED + "Invalid username or password.")
            return None

    elif choice == '2':
        username = input("Enter student username: ")
        password = input("Enter student password: ")

        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_data = line.strip().split(',')
                if user_data[0] == username and user_data[3] == password:
                    return username, password, 'student'

        print(Fore.RED + "Error: Invalid username or user not registered.")
        return None

    else:
        print(Fore.RED + "Invalid choice.")
        return None

def modify_student_record(student):
    print(Fore.YELLOW + f"\n{f.renderText('Modify Student Record')}")

    print(Fore.YELLOW + "\n1. Add Grade\n2. Add ECA Record\n3. Update Profile\n4. Back")
    choice = input(Fore.YELLOW + "Enter your choice: ")

    if choice == '1':
        grade = input("Enter grade: ")
        try:
            grade = int(grade)
            student.add_grade(grade)
            save_grade(student.student_id, grade)
        except ValueError:
            print(Fore.RED + "Error: Please enter a valid grade (numeric value).")

    elif choice == '2':
        eca_description = input("Enter ECA description: ")
        student.add_eca(eca_description)
        save_eca(student.student_id, eca_description)

    elif choice == '3':
        new_username = input("Enter new username: ")
        new_email = input("Enter new email: ")
        new_phone_number = input("Enter new phone number: ")
        student.update_profile(new_username, new_email, new_phone_number)

        # Update the user's information in the database
        with open('users.txt', 'r') as file:
            lines = file.readlines()

        with open('users.txt', 'w') as file:
            for line in lines:
                user_data = line.strip().split(',')
                if user_data and user_data[4] == student.student_id:  # Check student ID for modification
                    user_data[0] = new_username
                    user_data[2] = new_email
                    user_data[5] = new_phone_number
                    line = ','.join(user_data) + '\n'
                file.write(line)

    elif choice == '4':
        return

    else:
        print(Fore.RED + "Invalid choice.")

def display_student_info(student):
    print(Fore.YELLOW + f"\n{f.renderText('Student Information')}")
    print(Fore.YELLOW + f"\nUsername: {student.username}")
    print(f"Role: {student.role}")
    print(f"Email: {student.email}")
    print(f"Student ID: {student.student_id}")
    print(f"Grades: {student.grades}")
    print(f"ECA: {student.eca}")
    print(f"Phone Number: {student.phone_number}")

def main():
    create_empty_files()

    user_data = login()

    if user_data:
        username, password, role = user_data
        if role == 'admin':
            admin = Admin(username, password)
            print(Fore.GREEN + "Login successful! Welcome, Admin", username)

            admin.view_users()

            while True:
                print(Fore.YELLOW + "\n1. Register a new user\n2. Modify student record\n3. Delete student record\n4. View Users\n5. Exit")
                choice = input(Fore.YELLOW + "Enter your choice: ")

                if choice == '1':
                    new_username = input("Enter new username: ")
                    new_role = input("Enter role (admin/student): ")
                    new_email = input("Enter email: ")
                    new_password = input("Enter password: ")
                    new_phone_number = input("Enter phone number: ")
                    grades = input("Enter grades (comma-separated): ")
                    eca = input("Enter ECA description: ")
                    admin.register_user(new_username, new_role, new_email, new_password, new_phone_number, grades.split(','), eca)

                elif choice == '2':
                    student_id = input("Enter student ID to modify: ")
                    student = Student(username, role, '', student_id, [], '', '')  # Pass student ID
                    modify_student_record(student)

                elif choice == '3':
                    student_id = input("Enter student ID to delete: ")
                    admin.delete_user(student_id)  # Delete by student ID

                elif choice == '4':
                    admin.view_users()

                elif choice == '5':
                    print(Fore.GREEN + "Exiting...")
                    break

                else:
                    print(Fore.RED + "Invalid choice. Please try again.")

        elif role == 'student':
            student = Student(username, role, '', '', [], '', '')
            print(Fore.GREEN + "Login successful! Welcome, Student", username)

            display_student_info(student)

            while True:
                print(Fore.YELLOW + "\n1. Update profile\n2. View ECA details\n3. View examination grades\n4. Add ECA Details\n5. Add Examination Details\n6. Exit")
                choice = input(Fore.YELLOW + "Enter your choice: ")

                if choice == '1':
                    new_username = input("Enter new username: ")
                    new_email = input("Enter new email: ")
                    new_phone_number = input("Enter new phone number: ")
                    student.update_profile(new_username, new_email, new_phone_number)

                elif choice == '2':
                    student.view_eca()

                elif choice == '3':
                    student.view_grades()

                elif choice == '4':
                    eca_description = input("Enter ECA description: ")
                    student.add_eca(eca_description)
                    save_eca(student.student_id, eca_description)

                elif choice == '5':
                    grade = input("Enter grade: ")
                    try:
                        grade = int(grade)
                        student.add_grade(grade)
                        save_grade(student.student_id, grade)
                    except ValueError:
                        print(Fore.RED + "Error: Please enter a valid grade (numeric value).")

                elif choice == '6':
                    print(Fore.GREEN + "Exiting Student Dashboard...")
                    break

                else:
                    print(Fore.RED + "Invalid choice. Please try again.")

    else:
        print(Fore.RED + "Invalid role or user not registered. Exiting...")

if __name__ == "__main__":
    main()