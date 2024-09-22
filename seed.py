from sqlalchemy.orm import sessionmaker
from models import engine, Class, Subject, Score, Teacher, Student, Grade

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Seed data for Subjects
subject1 = Subject(subject_name="Mathematics")
subject2 = Subject(subject_name="English")
subject3 = Subject(subject_name="Science")

# Seed data for Teachers
teacher1 = Teacher(first_name="Bon", last_name="Jovi", subject=subject1)
teacher2 = Teacher(first_name="Dwayne", last_name="John", subject=subject2)
teacher3 = Teacher(first_name="Davie", last_name="Jones", subject=subject3)

# Seed data for Classes
class1 = Class(class_name="Grade 1", teacher=teacher1)
class2 = Class(class_name="Grade 2", teacher=teacher2)

# Seed data for Students
student1 = Student(first_name="Alice", last_name="Brown", date_of_birth="2012-05-15", gender="F", student_class=class1)
student2 = Student(first_name="Bob", last_name="Green", date_of_birth="2011-09-23", gender="M", student_class=class1)
student3 = Student(first_name="Charlie", last_name="Black", date_of_birth="2013-03-11", gender="M", student_class=class2)

# Seed data for Scores (example of assessments and scores for the students)
score1 = Score(student=student1, subject=subject1, score=85, max_score=100)
score2 = Score(student=student2, subject=subject1, score=90, max_score=100)
score3 = Score(student=student1, subject=subject2, score=78, max_score=100)
score4 = Score(student=student3, subject=subject3, score=88, max_score=100)

# Seed data for Grades (example of final grades for students)
grade1 = Grade(student=student1, subject=subject1, grade=85)
grade2 = Grade(student=student2, subject=subject1, grade=90)
grade3 = Grade(student=student3, subject=subject3, grade=88)

# Add all data to the session
session.add_all([subject1, subject2, subject3, teacher1, teacher2, teacher3, class1, class2,
                 student1, student2, student3, score1, score2, score3, score4, grade1, grade2, grade3])

# Commit the session to the database
session.commit()

# Close the session
session.close()
