'''
Partner, let's combine what you've learned.
    python_students = {"Ram", "Sita", "Hari", "Gita"}
    sql_students = {"Sita", "Hari", "Mina", "Raj"}
Write four print statements to find:
    Everyone who studies Python or SQL
    Students who study both
    Students who study Python but not SQL
    Students who study only one of the two subjects
Use the four operators you've just learned:
    |, &, -, ^
'''
python_students = {"Ram", "Sita", "Hari", "Gita"}
sql_students = {"Sita", "Hari", "Mina", "Raj"}
print(python_students | sql_students)
print(python_students & sql_students)
print(python_students - sql_students)
print(python_students ^ sql_students)