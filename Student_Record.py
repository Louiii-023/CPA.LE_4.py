import os
def doc_path():
  return os.path.expanduser("~/Documents")
def register_student(doc_path):
    print("=====STUDENT REGISTER=====")
    student_no = input("Student No.: ")
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    middle_initial = input("Middle Initial: ")
    program = input("Program: ")
    age = input("Age: ")
    gender = input("Gender: ")
    birthday = input("Birthday: ")
    con_no = input("Contact Number: ")

    data = [
       f"Student No.: {student_no}"
       f"Full Name : {last_name}, {first_name}, {middle_initial}"
       f"Program: {program}"
       f"Age: {age}"
       f"Gender: {gender}"
       f"Birthday: {birthday}"
       f"Contact Number: {con_no}"
       ]
    file_path = os.path.join(doc_path, f"{student_no}.txt")

    try:
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        print(f"✅ Student record saved to {file_path}")
    except Exception as e:
        print(f"❌ Error saving student record: {e}")

def open_student_record(doc_path):
    print("===== OPEN STUDENT RECORD =====")
    student_no = input("Enter Student No.: ")
    file_path = os.path.join(doc_path, f"{student_no}.txt")

    try:
        with open(file_path, "r") as f:
            print("\n===== STUDENT RECORD =====")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("X Student record not found.")
    except Exception as e:
          print(f"X Error reading student record: {e}")

def search_by_name(doc_path):
    print("===== SEARCH BY NAME =====")
    search_name = input("Enter name to search (Last Name or First Name): ").lower()
    found = False

    try:
        for file_name in os.listdir(doc_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(doc_path, file_name)
                with open(file_path, "r") as f:
                    content = f.read().lower()
                    if search_name in content:
                        print(f"\nRecord found in file: {file_name}")
                        print("-----")
                        print(content)
                        found = True
        if not found:
            print("X No records found with that name.")
    except Exception as e:
        print(f"❌ Error searching records: {e}")
def update_record(doc_path):
    print("===== UPDATE RECORD =====")
    student_no = input("Enter Student No. to update: ")
    file_path = os.path.join(doc_path, f"{student_no}.txt")
    if not os.path.exists(file_path):
        print("❌ Student record not found.")
        return

    print("Enter new details for the student:")
    register_student(doc_path)

def delete_record(doc_path):
    print("===== DELETE RECORD =====")
    student_no = input("Enter Student No. to delete: ")
    file_path = os.path.join(doc_path, f"{student_no}.txt")

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"✅ Record for Student No. {student_no} deleted.")
        else:
            print("❌ Student record not found.")
    except Exception as e:
        print(f"❌ Error deleting record: {e}")

def main_menu():
    while True:
        print("\n===== MAIN =====")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Search by Name")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        choice = input("Enter your Option: ")

        if choice == "1":
            register_student(doc_path())
        elif choice == "2":
            open_student_record(doc_path())
        elif choice == "3":
            search_by_name(doc_path())
        elif choice == "4":
            update_record(doc_path())
        elif choice == "5":
            delete_record(doc_path())
        elif choice == "6":
            print("Goodbye!")
            break
        else: 
            print("❌ Invalid choice. Please try again.")
   

main_menu()


       



