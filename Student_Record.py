import os

# Function to get the path to the Documents folder
def doc_path():
  return os.path.expanduser("~/Documents")

# Function to register a new student and save their record to a file
def register_student(doc_path):
    print("=====STUDENT REGISTER=====")
    student_no = input("Student No.: ")  # Get student number
    last_name = input("Last Name: ")  # Get last name
    first_name = input("First Name: ")  # Get first name
    middle_initial = input("Middle Initial: ")  # Get middle initial
    program = input("Program: ")  # Get program
    age = input("Age: ")  # Get age
    gender = input("Gender: ")  # Get gender
    birthday = input("Birthday: ")  # Get birthday
    con_no = input("Contact Number: ")  # Get contact number

    # Prepare student data to save
    data = [
       f"Student No.: {student_no}"
       f"Full Name : {last_name}, {first_name}, {middle_initial}"
       f"Program: {program}"
       f"Age: {age}"
       f"Gender: {gender}"
       f"Birthday: {birthday}"
       f"Contact Number: {con_no}"
       ]
    file_path = os.path.join(doc_path, f"{student_no}.txt")  # File path for the record

    try:
        # Write student data to the file
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        print(f"✅ Student record saved to {file_path}")
    except Exception as e:
        print(f"❌ Error saving student record: {e}")

# Function to open and display a student's record
def open_student_record(doc_path):
    print("===== OPEN STUDENT RECORD =====")
    student_no = input("Enter Student No.: ")  # Get student number
    file_path = os.path.join(doc_path, f"{student_no}.txt")  # File path for the record

    try:
        # Read and display the student record
        with open(file_path, "r") as f:
            print("\n===== STUDENT RECORD =====")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("X Student record not found.")
    except Exception as e:
          print(f"X Error reading student record: {e}")

# Function to search for a student record by name
def search_by_name(doc_path):
    print("===== SEARCH BY NAME =====")
    search_name = input("Enter name to search (Last Name or First Name): ").lower()  # Get name to search
    found = False

    try:
        # Iterate through all files in the directory
        for file_name in os.listdir(doc_path):
            if file_name.endswith(".txt"):  # Check if the file is a student record
                file_path = os.path.join(doc_path, file_name)
                with open(file_path, "r") as f:
                    content = f.read().lower()
                    if search_name in content:  # Check if the name is in the file content
                        print(f"\nRecord found in file: {file_name}")
                        print("-----")
                        print(content)
                        found = True
        if not found:
            print("X No records found with that name.")
    except Exception as e:
        print(f"❌ Error searching records: {e}")

# Function to update an existing student record
def update_record(doc_path):
    print("===== UPDATE RECORD =====")
    student_no = input("Enter Student No. to update: ")  # Get student number
    file_path = os.path.join(doc_path, f"{student_no}.txt")  # File path for the record
    if not os.path.exists(file_path):  # Check if the record exists
        print("❌ Student record not found.")
        return

    print("Enter new details for the student:")
    register_student(doc_path)  # Call register_student to overwrite the record

# Function to delete a student record
def delete_record(doc_path):
    print("===== DELETE RECORD =====")
    student_no = input("Enter Student No. to delete: ")  # Get student number
    file_path = os.path.join(doc_path, f"{student_no}.txt")  # File path for the record

    try:
        if os.path.exists(file_path):  # Check if the record exists
            os.remove(file_path)  # Delete the file
            print(f"✅ Record for Student No. {student_no} deleted.")
        else:
            print("❌ Student record not found.")
    except Exception as e:
        print(f"❌ Error deleting record: {e}")

# Main menu function to navigate through the program
def main_menu():
    while True:
        print("\n===== MAIN =====")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Search by Name")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        choice = input("Enter your Option: ")  # Get user choice

        if choice == "1":
            register_student(doc_path())  # Register a new student
        elif choice == "2":
            open_student_record(doc_path())  # Open a student record
        elif choice == "3":
            search_by_name(doc_path())  # Search for a student by name
        elif choice == "4":
            update_record(doc_path())  # Update a student record
        elif choice == "5":
            delete_record(doc_path())  # Delete a student record
        elif choice == "6":
            print("Goodbye!")  # Exit the program
            break
        else: 
            print("❌ Invalid choice. Please try again.")  # Handle invalid input
   

main_menu()  # Start the program
