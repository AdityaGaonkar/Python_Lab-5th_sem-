class Student:
    def __init__(self, name, rollno, branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch


def branchMatch(students, target_branch):
    matchStdents = []
    for student in students:
        if student.branch == target_branch:
            matchStdents.append(student)
    return matchStdents


def main():
    N = int(input("enter the number of students\n"))

    students = []
    for _ in range(0, N):
        name = input("enter the name\n")
        rollno = input("enter the roll no\n")
        branch = input("enter the branch\n")
        student = Student(name, rollno, branch)
        students.append(student)

    target_branch = input("enter the target branch\n")
    matching_students = branchMatch(students, target_branch)
    if matching_students:
        print("\nStudents on the branch ", target_branch)
        for student in matching_students:
            print(f"Name :{student.name},Rollno :{student.rollno},branch :{student.branch}")
    else:
        print("no student in that branch")


if __name__ == "__main__":
    main()
