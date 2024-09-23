from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import Student, Teacher, Class, Score, Grade, engine

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

"""*****************************************************************************************"""

# Function to view all students
def view_students():
    try:
        students = session.query(Student).all()
        #return this if students table empty
        if not students:
            print("\n  No students found in the database.")
            return

        students_dict = {}
        student_list = []

        print("\n--- List of Students ---")
        for student in students:
            student_info = (student.first_name, student.last_name, student.student_class.class_name, student.date_of_admission)  # Tuple with name, class, and date_of_admission
            students_dict[student.id] = student_info  # Dictionary with student ID as key
            student_list.append(student_info)  # Add tuple to list
            print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Class: {student.student_class.class_name}, Date of Admission: {student.date_of_admission}")

        # Output example as tuples and list
        print("\n--- Students as a List of Tuples ---")
        print(student_list)
        # Output example  as dictionary
        print("\n--- Students as a Dictionary ---")
        print(students_dict)

    except SQLAlchemyError as e:
        print(f" An error occurred while fetching students: {e}")

"""****************************************************************************"""

# Function to add a new student with error handling
def add_student():
    try:
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        date_of_birth = input("Enter student's date of birth (YYYY-MM-DD): ")
        gender = input("Enter student's gender (M/F): ").upper()

        if gender not in ['M', 'F']:
            raise ValueError("Invalid gender entered. Please use 'M' or 'F'.")

        class_id = int(input("Enter student's class ID: "))
        date_of_admission = input("Enter student's date of admission (YYYY-MM-DD): ")

        new_student = Student(
            first_name=first_name, 
            last_name=last_name, 
            date_of_birth=date_of_birth, 
            gender=gender, 
            class_id=class_id,
            date_of_admission=date_of_admission  # Date of admission added
        )
        session.add(new_student)
        session.commit()
        print(f" Student {first_name} {last_name} added successfully!")

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except SQLAlchemyError as e:
        print(f" An error occurred while adding the student: {e}")
        session.rollback()

"""****************************************************************************"""

# Function to delete a student by ID with error handling
def delete_student():
    try:
        student_id = int(input("Enter the student ID to delete: "))
        student = session.query(Student).filter_by(id=student_id).first()

        if student is None:
            print(f"\n No student found with ID: {student_id}.")
            return

        session.delete(student)
        session.commit()
        print(f"\n Student ID: {student_id} has been deleted successfully.")

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except SQLAlchemyError as e:
        print(f" An error occurred while deleting the student: {e}")
        session.rollback()

"""****************************************************************************"""

# Function to view all teachers with error handling
def view_teachers():
    try:
        teachers = session.query(Teacher).all()
        if not teachers:
            print("\n No teachers found in the database.")
            return

        teacher_dict = {}

        print("\n--- List of Teachers ---")
        for teacher in teachers:
            teacher_info = (teacher.first_name, teacher.last_name, teacher.subject.subject_name, teacher.date_of_admission)  # Tuple with name, subject, and date_of_admission
            teacher_dict[teacher.id] = teacher_info  # Dictionary with teacher ID as key
            print(f"ID: {teacher.id}, Name: {teacher.first_name} {teacher.last_name}, Subject: {teacher.subject.subject_name}, Date of Admission: {teacher.date_of_admission}")

        # Output the dictionary
        print("\n--- Teachers as a Dictionary ---")
        print(teacher_dict)

    except SQLAlchemyError as e:
        print(f" An error occurred while fetching teachers: {e}")

"""****************************************************************************"""

# Function to add a new teacher with error handling
def add_teacher():
    try:
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        subject_id = int(input("Enter teacher's subject ID: "))
        date_of_admission = input("Enter teacher's date of admission (YYYY-MM-DD): ")

        new_teacher = Teacher(
            first_name=first_name, 
            last_name=last_name, 
            subject_id=subject_id,
            date_of_admission=date_of_admission  # Date of admission added
        )
        session.add(new_teacher)
        session.commit()
        print(f" Teacher {first_name} {last_name} added successfully!")

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except SQLAlchemyError as e:
        print(f" An error occurred while adding the teacher: {e}")
        session.rollback()

"""****************************************************************************"""       

# Function to delete a teacher by ID with error handling
def delete_teacher():
    try:
        teacher_id = int(input("Enter the teacher ID to delete: "))
        teacher = session.query(Teacher).filter_by(id=teacher_id).first()

        if teacher is None:
            print(f"\n No teacher found with ID: {teacher_id}.")
            return

        session.delete(teacher)
        session.commit()
        print(f"\n Teacher ID: {teacher_id} has been deleted successfully.")

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except SQLAlchemyError as e:
        print(f" An error occurred while deleting the teacher: {e}")
        session.rollback()

"""****************************************************************************"""        

# Function to view student grades with error handling
def view_student_grades():
    try:
        student_id = int(input("Enter the student's ID to view grades: "))
        grades = session.query(Grade).filter_by(student_id=student_id).all()

        if not grades:
            print(f"\n  No grades found for Student ID: {student_id}.")
            return

        grade_list = []

        print(f"\n--- Grades for Student ID: {student_id} ---")
        for grade in grades:
            grade_info = {
                "subject": grade.subject.subject_name,
                "grade": grade.grade
            }  # Dictionary with subject and grade
            grade_list.append(grade_info)
            print(f"Subject: {grade.subject.subject_name}, Grade: {grade.grade}")
        
        # Output the list of dictionaries
        print("\n--- Grades as a List of Dictionaries ---")
        print(grade_list)

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except SQLAlchemyError as e:
        print(f" An error occurred while fetching grades: {e}")

"""****************************************************************************"""

# Function to view student scores with error handling
def view_student_scores():
    try:
        student_id = int(input("Enter the student's ID to view scores: "))
        scores = session.query(Score).filter_by(student_id=student_id).all()

        if not scores:
            print(f"\n No scores found for Student ID: {student_id}.")
            return

        score_list = []

        print(f"\n--- Scores for Student ID: {student_id} ---")
        for score in scores:
            score_info = (score.subject.subject_name, score.score, score.max_score)  # Tuple with subject, score, and max score
            score_list.append(score_info)
            print(f"Subject: {score.subject.subject_name}, Score: {score.score}/{score.max_score}")
        
        # Output the list of tuples
        print("\n--- Scores as a List of Tuples ---")
        print(score_list)

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except SQLAlchemyError as e:
        print(f" An error occurred while fetching scores: {e}")
