

def add_students(students, next_student_id):

    print('adding student')
    first_name = input(str('first-name'))
    last_name = input(str('last-name'))

    students.append([next_student_id, first_name, last_name])

    print(f'Successfully added: {next_student_id} {first_name} {last_name}')

    return


def delete_student(students):

    print('deleting')

    if len(students) == 0:
        print("There are no students in the list.\n")
        return

    print('testing 1')
    student_idd = input('Please enter a student ID: ')
    student_id = int(student_idd)
    print('testing 2')

    student_index = find_student_index(students, student_id)
    if student_index == -1:
        print(f'ID not found: {student_id}')
        return

    student = students[student_index]
    student_id, first_name, last_name = student

    print(f'Delete this student? {student_id} {first_name} {last_name}')
    confirm = input(str('Enter a Y or N: '))

    if confirm in ['Y', 'Yes']:
        student = students.pop(student_index)
        print(f'Student: {student_id} {first_name} {last_name} successfully deleted!')
    else:
        print('Cancelled deletion')


def find_student_index(students, student_id):

    for student in students:
        if student_id == student[0]:
            return students.index(student)

    return -1


def list_students(students):

    if len(students) == 0:
        print("There are no students in the list.\n")
        return

    for student in students:
        student_id, first_name, last_name = student
        print(f'{student_id} {first_name} {last_name}')
    return


def update_student(students):

    if len(students) == 0:
        print("There are no students in the list.\n")
        return

    student_id = input(int('Please enter a student ID: '))

    student_index = find_student_index(students, student_id)
    if student_index == -1:
        print(f'ID not found: {student_id}')
        return

    student = students[student_index]
    student_id, first_name, last_name = student

    print(f'Update this student? {student_id} {first_name} {last_name}')
    confirm = input(str('Enter a Y or N: '))
    old_first = student[1]
    old_last = student[2]

    if confirm in ['Y', 'Yes']:
        new_first = input(str(f'Please enter the new first name or press Enter to keep {old_first}: '))
        new_last = input(str(f'Please enter the new last name or press Enter to keep {old_last}: '))
        if new_first == '':
            print('First name unchanged.')
        else:
            student[1] = new_first

        if new_last == '':
            print('Last name unchanged.')
        else:
            student[2] = new_last

        if new_first == '' and new_last == '':
            print('No changes made.')
        else:
            student[1] = new_first
            student[2] = new_last

        print(f'Student: {student_id} {old_first} {old_last} successfully updated to {student[1]} {student[2]}!')
    else:
        print('Cancelled update')

    return








