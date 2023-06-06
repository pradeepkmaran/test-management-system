attendance = {}

def mark_attendance(test_type, subject_code, absentees):
  if (test_type, subject_code) not in attendance:
    attendance[(test_type, subject_code)] = []
  attendance[(test_type, subject_code)].extend(absentees)
