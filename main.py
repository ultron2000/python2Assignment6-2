
import student_maintanence as s


def display_menu():
    print("COMMAND MENU")
    print("1 - List all students")
    print("2 - Add a student")
    print("3 - Update a student")
    print("4 - Delete a student")
    print('0 - Exit program')
    print()


def main():
    print('Welcome')

    students = []
    next_student_id = 1

    display_menu()

    while True:
        command = input("Command: ")
        if command == "1":
            s.list_students(students)
        elif command == "2":
            s.add_students(students, next_student_id)
            next_student_id += 1
        elif command == '3':
            s.update_student(students)
        elif command == "4":
            s.delete_student(students)
        elif command == "0":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
