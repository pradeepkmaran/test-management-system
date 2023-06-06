tests = list()
def add_test(test_type, date, subject_code, subject_name):
  tests.append({"test_type": test_type, "date": date, "subject_code": subject_code, "subject_name": subject_name})

def edit_test(index, test_type=None, date=None, subject_code=None, subject_name=None):
  if index >= 0 and index < len(tests):
    test = tests[index]
    if test_type:
      test["test_type"] = test_type
    if date:
      test["date"] = date
    if subject_code:
      test["subject_code"] = subject_code
    if subject_name:
      test["subject_name"] = subject_name

