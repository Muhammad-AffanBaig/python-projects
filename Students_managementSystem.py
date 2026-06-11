marks_students = {}
while(True):
    print("1. Add Student\n2. Search Student\n3. Show All Students\n4. Update Marks\n5. Exit")

    choice = int(input("Enter a choice: "))

    if(choice == 1):
        name_student = input("Enter a student name: ")
        marks = input("Enter marks: ")
        marks_students[name_student] = marks

    elif(choice == 2):
        found = False
        name_student = input("Enter a student name to search: ")

        for key in marks_students:
            if(name_student.lower() == key.lower()):
                found = True
                break

        if(found):
            print(key, "got", marks_students[key], "marks")
        else:
            print(name_student, "is not found")

    elif(choice == 3):
        for key, value in marks_students.items():
            print(key, 'got', value, 'marks')

    elif(choice == 4):
        name_student = input("Enter a student name: ")
        found = False

        for key in marks_students:
            if key.lower() == name_student.lower():
                found = True
                break

        if(found):
            marks = input("Enter new marks: ")
            marks_students[key] = marks
        else:
            print(name_student, "is not present in the current data")

    elif(choice == 5):
        break