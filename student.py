students = {} 

def add_student(reg_num, name, email):  
  students[reg_num] = {"name": name, "email": email}

def edit_student(reg_num, name=None, email=None):
  student = students.get(reg_num)
  if student:
    if name:
      student["name"] = name
    if email:
      student["email"] = email

