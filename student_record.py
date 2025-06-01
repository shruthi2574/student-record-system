import os

# File to store student records
FILE_NAME = "students.txt"

def add_student():
    with open(FILE_NAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        file.write(f"{roll},{name},{branch}\n")
        print("✅ Student added successfully!\n")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found.\n")
        return
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        print("📋 Student Records:")
        for line in lines:
            roll, name, branch = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Branch: {branch}")
        print()

def search_student():
    roll_to_find = input("Enter Roll Number to search: ")
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, branch = line.strip().split(",")
            if roll == roll_to_find:
                print(f"🎯 Found: Roll: {roll}, Name: {name}, Branch: {branch}\n")
                found = True
                break
    if not found:
        print("❌ Student not found.\n")

def delete_student():
    roll_to_delete = input("Enter Roll Number to delete: ")
    lines = []
    found = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            roll, _, _ = line.strip().split(",")
            if roll != roll_to_delete:
                file.write(line)
            else:
                found = True
    if found:
        print("🗑️ Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")

def update_student():
    roll_to_update = input("Enter Roll Number to update: ")
    lines = []
    updated = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            roll, name, branch = line.strip().split(",")
            if roll == roll_to_update:
                new_name = input("Enter new name: ")
                new_branch = input("Enter new branch: ")
                file.write(f"{roll},{new_name},{new_branch}\n")
                updated = True
            else:
                file.write(line)
    if updated:
        print("✅ Student updated successfully!\n")
    else:
        print("❌ Student not found.\n")

def main():
    while True:
        print("📚 Student Record System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
