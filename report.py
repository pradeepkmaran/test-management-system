# 4. Report generation
import student, attendance

students = student.students

def report_absent_students(test_type, num_absences):
  result = []
  countabs = {}
  for reg_no in students:
    count = 0
    countabs[reg_no]=0
    for (t, subject), absentees in attendance.attendance.items():
      if t == test_type and (students[reg_no]["name"] in absentees):
        countabs[reg_no]+=1
    if countabs[reg_no] >= num_absences:
      result.append(students[reg_no]["name"])
  return result

def report_student_attendance(stud_name):
  result = []
  for (test_type, subject), absentees in attendance.attendance.items():
    if stud_name in absentees:
      result.append({"test_type": test_type, "subject": subject})
  return result

def report_absent_in_subject(subject_code):
  result = []
  for (test_type1, subject1), absentees1 in attendance.attendance.items():
    if subject1 == subject_code:
      for (test_type2, subject2), absentees2 in attendance.attendance.items():
        if test_type1 != test_type2 and subject2 == subject_code:
          for student in absentees1:
            if student in absentees2 and student not in result:
              result.append(student)
  return result