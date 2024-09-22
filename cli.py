from helper import view_students, add_student, view_teachers, add_teacher, view_student_grades, view_student_scores

def display_menu():
    print("\033[92m" + "\n" + "="*40)  # Green color start
    print("       📚  \033[1m\033[93mSCHOOL DATABASE MENU\033[0m  📚       ")  # Yellow + bold for the title
    print("\033[92m" + "="*40)  # End color
    print("1. View all students")
    print("2. Add new student")
    print("3. View all teachers")
    print("4. Add new teacher")
    print("5. View student scores")
    print("6. View student grades")
    print("7. Exit\033[0m")  # End color (reset)
    print("\033[92m" + "="*40 + "\033[0m")  # Green color end
    
#main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_students()
        elif choice == "2":
            add_students()
        elif choice == "3":
            view_teachers()
        elif choice == "4":
            add_teachers()
        elif choice == "5":
            view_student_scores()
        elif choice == "6":
            view_student_grades()
        elif choice == "7":
            print("Exiting the program. Goodbye!!")
            break
        else:
            print("Invalid choice. Try again")

if __name__=="__main__":
    main()
