import student, test, attendance, test, report

#creating student repository
while(True):
    addeditskip = int(input("Enter 1 to add, 2 to edit, 3 to Move to next step: "))
    print()
    if(addeditskip == 1):
        no_of_students = int(input("\nEnter number of students:"))
        for stud in range(no_of_students):
            reg_no = int(input("\nEnter register number of student {}:".format(stud+1)))
            stud_name = input("Enter name of the student {}:".format(stud+1))
            stud_email = input("Enter email of the student {}:".format(stud+1))
            student.add_student(reg_no, stud_name, stud_email)
    elif(addeditskip == 3):
        break
    else:
        edit = int(input("Enter 1 to edit name, 2 to edit email, 3 to edit both:"))
        if(edit == 1):
            edit_reg_no = int(input("\nEnter register number:"))
            edit_name = input("Enter new name:")
            student.edit_student(edit_reg_no, name=edit_name)
        elif(edit == 2):
            edit_reg_no = int(input("\nEnter register number:"))
            edit_email = input("Enter new email:")
            student.edit_student(edit_reg_no, email=edit_email)
        else:
            edit_reg_no = int(input("\nEnter register number:"))
            edit_name = input("Enter new name:")
            edit_email = input("Enter new email:")
            student.edit_student(edit_reg_no, edit_name, edit_email)
    print()
    
#creating testschedule database
while(True):
    addeditskip = int(input("\nEnter 1 to add test, 2 to edit test, 3 to Move to next step: "))
    print()
    if(addeditskip == 1):
        no_of_tests = int(input("Enter number of tests:"))
        for tes in range(no_of_tests):
            test_type = input("\nEnter the type of test {}:".format(tes+1))
            test_date = input("Enter date of test {}:".format(tes+1))
            sub_code = input("Enter subject code {}:".format(tes+1))
            sub_name = input("Enter the subject {}:".format(tes+1))
            test.add_test(test_type=test_type, date=test_date, subject_code=sub_code, subject_name=sub_name)
            print()
    elif(addeditskip == 3):
        break
    else:
        edit = int(input("""\nEnter 1 to edit test type, 2 to edit test date, 3 to edit subject code,
                4 to edit subject name, 5 to edit all:"""))
        if(edit == 1):
            edit_test_no = int(input("\nEnter test number:"))
            edit_test_type = input("Enter test_type:")
            test.edit_test(edit_test_no-1, test_type=edit_test_type)
        elif(edit == 2):
            edit_test_no = int(input("\nEnter test number:"))
            edit_test_date = input("Enter new date:")
            test.edit_test(edit_test_no-1, date=edit_test_date)
        elif(edit == 3):
            edit_test_no = int(input("\nEnter test number:"))
            edit_sub_code = input("Enter new subject code:")
            test.edit_test(edit_test_no-1, subject_code=edit_sub_code)
        elif(edit == 4):
            edit_test_no = int(input("\nEnter test number:"))
            edit_sub_name = input("Enter new subject name:")
            test.edit_test(edit_test_no-1, subject_name=edit_sub_name)
        else:
            edit_test_no = int(input("\nEnter test number:"))
            edit_test_type = input("Enter test_type:")
            edit_test_date = input("Enter new date:")
            edit_sub_code = input("Enter new subject code:")
            edit_sub_name = input("Enter new subject name:")
            edit_test_no -= 1
            test.edit_test(index= edit_test_no, test_type=edit_test_type, date=edit_test_date, subject_code=edit_sub_code, subject_name=edit_sub_name)
        print()

tests = test.tests

for tes in tests:
    abs = input("Enter absentees of {} {}:".format(tes["test_type"], tes["subject_code"])).split()
    attendance.mark_attendance(tes["test_type"], tes["subject_code"], abs)

test_list = []
for tes in test.tests:
    if(tes["test_type"] not in test_list):
        test_list.append(tes["test_type"])

print()
for tes_type in test_list:
    print("Absent students for {} with 3 or more absences:".format(tes_type), report.report_absent_students(tes_type, 3))

print()
reg_no = int(input("Enter the register number of student to know attendance status:"))
print(" Student {} was absent on:".format(student.students[reg_no]["name"]), report.report_student_attendance(student.students[reg_no]["name"]))

print()
sub_name = input("Enter the subject name to know absentees:")
print(report.report_absent_in_subject(sub_name))













"""
add_student("123", "John Doe", "johndoe@example.com")
add_student("124", "Jane Doe", "janedoe@example.com")

#Adding tests
add_test("CAT1", "2022-01-01", "MATH101", "Mathematics I")
add_test("CAT2", "2022-02-01", "MATH101", "Mathematics I")

# Marking attendance
mark_attendance("CAT1", "MATH101", ["123"])
mark_attendance("CAT2", "MATH101", ["123", "124"])

# Generating reports
print("Absent students for CAT1 with 3 or more absences:", report_absent_students("CAT1", 3))
print("Attendance for student 123:", report_student_attendance("123"))
print("Absent students in Mathematics I for 2 CATs:", report_absent_in_subject("MATH101"))
"""