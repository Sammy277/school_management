# ==================== School Management System using OOP ====================

# ---------- Abstraction & Encapsulation ----------
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute (Encapsulation)
        self.__age = age    # Private attribute

    def get_details(self):
        """Abstraction: Public method to show details without exposing private data"""
        return f"Name: {self.__name}, Age: {self.__age}"


# ---------- Inheritance ----------
class Staff(Person):
    def __init__(self, name, age, staff_id, department):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Staff ID: {self.staff_id}, Department: {self.department}"


class Teacher(Staff):
    def __init__(self, name, age, staff_id, department, subject):
        super().__init__(name, age, staff_id, department)
        self.subject = subject

    # ---------- Polymorphism ----------
    def get_details(self):
        return f"{super().get_details()}, Subject: {self.subject}"


class NonTeachingStaff(Staff):
    def __init__(self, name, age, staff_id, department, role):
        super().__init__(name, age, staff_id, department)
        self.role = role

    def get_details(self):
        return f"{super().get_details()}, Role: {self.role}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def get_details(self):
        return f"{super().get_details()}, Student ID: {self.student_id}, Grade: {self.grade}"


# ---------- School Class to Manage People ----------
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.people = []  # Stores students and staff

    def add_person(self, person):
        self.people.append(person)

    def display_all_people(self):
        print(f"\n=== {self.school_name} - People List ===")
        for person in self.people:
            print(person.get_details())


# ---------- Main Program ----------
def main():
    school = School("Greenfield High School")

    # Add Teachers
    school.add_person(Teacher("Alice Johnson", 30, "T001", "Science", "Physics"))
    school.add_person(Teacher("Michael Smith", 40, "T002", "Mathematics", "Algebra"))

    # Add Non-Teaching Staff
    school.add_person(NonTeachingStaff("Sarah Brown", 35, "NT001", "Administration", "Secretary"))
    school.add_person(NonTeachingStaff("John Doe", 45, "NT002", "Maintenance", "Electrician"))

    # Add Students
    school.add_person(Student("Emma Wilson", 15, "S001", "Grade 10"))
    school.add_person(Student("Liam Davis", 16, "S002", "Grade 11"))

    # Display all people
    school.display_all_people()


if __name__ == "__main__":
    main()