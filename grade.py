class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def calculate_average(self):
        total_sum = 0
        count = 0
        for grades in self.grades.values():
            total_sum += sum(grades)
            count += len(grades)
        return total_sum / count if count != 0 else 0

    def calculate_letter_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def calculate_gpa(self):
        average = self.calculate_average()
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

def find_student(students, name):
    for student in students:
        if student.name == name:
            return student
    return None

def main():
    students = []

    while True:
        print("Choose an option:")
        print("1. Add a new student")
        print("2. Add a grade to a student")
        print("3. Calculate a student's average grade")
        print("4. Display a student's overall grade information")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the program.")
            break

        if choice == '1':
            name = input("Enter the student's name: ")
            students.append(Student(name))
            print("Student added.")
        elif choice == '2':
            name = input("Enter the student's name: ")
            student = find_student(students, name)
            if student:
                subject = input("Enter the subject: ")
                try:
                    grade = float(input("Enter the grade: "))
                    student.add_grade(subject, grade)
                    print("Grade added.")
                except ValueError:
                    print("Invalid grade! Please enter a numeric value.")
            else:
                print("Student not found.")
        elif choice == '3':
            name = input("Enter the student's name: ")
            student = find_student(students, name)
            if student:
                average = student.calculate_average()
                print(f"Average grade for {name}: {average:.2f}")
            else:
                print("Student not found.")
        elif choice == '4':
            name = input("Enter the student's name: ")
            student = find_student(students, name)
            if student:
                average = student.calculate_average()
                letter_grade = student.calculate_letter_grade()
                gpa = student.calculate_gpa()
                print(f"Overall grade information for {name}:")
                print(f"Average Grade: {average:.2f}")
                print(f"Letter Grade: {letter_grade}")
                print(f"GPA: {gpa:.2f}")
            else:
                print("Student not found.")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
