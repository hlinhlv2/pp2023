# Input functions:
# • Input number of students in a class
# • Input student information: id, name, DoB
# • Input number of courses
# • Input course information: id, name
# • Select a course, input marks for student in this course
# Listing functions:
# • List courses
# • List students
# • Show student marks for a given course

# Input Functions
# Input students' information for the class
def input_student():
    student_number = int(input("Enter number of students: "))
    student_list = []
    for i in range(student_number): 
        student_info = {}
        student_info["id"] = input("Enter student id: ")
        # Check if student id already exists
        for j in range(i):
            while student_info["id"] == student_list[j]["id"]:
                print("Student id already exists")
                student_info["id"] = input("Enter student id: ")
        student_info["name"] = input("Enter student name: ") 
        student_info["dob"] = input("Enter student DoB: ")
        print() # Just a seprarator

        # Add student to the list
        student_list.append(student_info)
    return student_list

# Input courses' information for B2 class
def input_course():
    course_number = int(input("Enter number of courses: "))
    course_list = []
    for i in range(course_number):
        course_info = {}
        course_info["id"] = input("Enter course id: ")
        # Check if course id already exists
        for j in range(i):
            while course_info["id"] == course_list[j]["id"]:
                print("Course id already exists")
                course_info["id"] = input("Enter course id: ")
        course_info["name"] = input("Enter course name: ")
        print() # Just a seprarator

        # Add course to the list
        course_list.append(course_info)
    return course_list

# Select a course, input marks for student in that course
def input_marks(student_list, course_list):
    id_checked = True # Define a variable to check if the course id is correct
    while id_checked:
        course_selected_id = input("Enter course id: ")
        # Check if course id is correct
        if any (course_selected_id == course["id"] for course in course_list):
            id_checked = False
            for index, course in enumerate(course_list):
                if course_selected_id == course["id"]:
                    correct_course_index = index
            # Define the course name for the selected course id        
            course_selected_name = course_list[correct_course_index]["name"]
            # Input marks for students in the selected course
            for student in student_list:
                student["mark"] = input(f"Enter mark for {student['name']}: ")
            mark_list = student_list    # Define a new list to store the marks
            return mark_list, course_selected_name
        else:
            print("Course not found!!!")
            print() # Just a seprarator
            id_checked = True    # Continue to check if the course id is correct
            
# Listing Functions
# Display the student list in the class in Dictionary format   
def list_students(student_list):
    print("Student list: ")
    for student in student_list:
        print(student)

# Display the course list that these student enrolled in Dictionary format
def list_courses(course_list):
    print("Course list: ")
    for course in course_list:
        print(course)

# Display the student marks for the course in Dictionary format
def show_marks(mark_list, course_selected_name):
    print(f"Student marks for {course_selected_name}: ")
    for student in mark_list:
        print(student)

# Main function
def main():
    my_class = input_student()
    print("=" * 20)
    b2_courses = input_course()
    print("=" * 20)
    list_students(my_class)
    print("=" * 20)
    list_courses(b2_courses)
    print("=" * 20)
    my_class_marks = input_marks(my_class, b2_courses)
    print("=" * 20)
    show_marks(my_class_marks[0], my_class_marks[1])

# Run the program
main()
