from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///school.db"
engine = create_engine(db_url)

Base = declarative_base()

"""****************************************************************************"""

# create student table
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    gender = Column(String)
    date_of_admission = Column(String)
    class_id = Column(Integer, ForeignKey("classes.id"))  # foreign key to class table

    # Relationship to access the student's class
    student_class = relationship("Class", back_populates="students")
    # Relationship to access student's scores
    scores = relationship("Score", back_populates="student")
    # Relationship to access student's grades
    grades = relationship("Grade", back_populates="student")

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, class={self.student_class.class_name})>"

"""****************************************************************************"""

# create teachers table
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_admission = Column(String)
    subject_id = Column(Integer, ForeignKey("subjects.id"))  # foreign key to subjects table

    # Relationship to access the teacher's subject
    subject = relationship("Subject", back_populates="teachers")
    # Relationship to access the class that the teacher teaches
    classes = relationship("Class", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.first_name} {self.last_name}, subject_id={self.subject_id})>"

"""****************************************************************************"""

# create classes table
class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    class_name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))  # foreign key to teachers table

    # Relationship to access the teacher of the class
    teacher = relationship("Teacher", back_populates="classes")
    # Relationship to access the students in the class
    students = relationship("Student", back_populates="student_class")

    def __repr__(self):
        return f"<Class(id={self.id}, class_name={self.class_name})>"

"""****************************************************************************"""

# create subjects table
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String)

    # Relationship to access teachers teaching the subject
    teachers = relationship("Teacher", back_populates="subject")
    # Relationship to access scores for the subject
    scores = relationship("Score", back_populates="subject")
    # Relationship to access grades for the subject
    grades = relationship("Grade", back_populates="subject")

    def __repr__(self):
        return f"<Subject(id={self.id}, subject_name={self.subject_name})>"

"""****************************************************************************"""

# create scores table
class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))  # foreign key to students table
    subject_id = Column(Integer, ForeignKey("subjects.id"))  # foreign key to subjects table
    score = Column(Float)
    max_score = Column(Float)  # 100.00

    # Relationship to access the student for a score
    student = relationship("Student", back_populates="scores")
    # Relationship to access the subject for a score
    subject = relationship("Subject", back_populates="scores")

    def __repr__(self):
        return f"<Score(id={self.id}, student_id={self.student_id}, subject_id={self.subject_id}, score={self.score}/{self.max_score})>"

"""****************************************************************************"""

# create grades table
class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))  # foreign key to students table
    subject_id = Column(Integer, ForeignKey("subjects.id"))  # foreign key to subjects table
    grade = Column(Float)  # to be calculated from the scores table

    # Relationship to access the student for a grade
    student = relationship("Student", back_populates="grades")
    # Relationship to access the subject for a grade
    subject = relationship("Subject", back_populates="grades")

    def __repr__(self):
        return f"<Grade(id={self.id}, student_id={self.student_id}, subject_id={self.subject_id}, grade={self.grade})>"

"""****************************************************************************"""

# Create tables in the database
Base.metadata.create_all(engine)
