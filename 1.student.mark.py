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

def input_student():
    student_number = int(input("Enter number of students: "))
    student_list = []
    for i in range(student_number):
        student_info = {}
        student_info["id"] = input("Enter student id: ")
        student_info["name"] = input("Enter student name: ")
        student_info["dob"] = input("Enter student DoB: ")
        print()
        student_list.append(student_info)
    return student_list

def input_course():
    course_number = int(input("Enter number of courses: "))
    course_list = []
    for i in range(course_number):
        course_info = {}
        course_info["id"] = input("Enter course id: ")
        course_info["name"] = input("Enter course name: ")
        print()
        course_list.append(course_info)
    return course_list

def input_mark(student_list, course_list):
    course_select = input("Enter course id: ")
    for course in course_list:
        if course["id"] == course_select:
            course_name = course["name"]
            for student in student_list:
                # input mark with student name
                student["mark"] = input(f"Enter mark for {student['name']}: ")
    mark_list = student_list
    return mark_list, course_name

def list_students(student_list):
    print("Student list: ")
    for student in student_list:
        print(student)

def list_courses(course_list):
    print("Course list: ")
    for course in course_list:
        print(course)

def show_mark(mark_list, course_name):
    print(f"Student mark for {course_name}: ")
    for student in mark_list:
        print(student)

# Test
CS_class = input_student()
print("=" * 20)
B2_courses = input_course()
print("=" * 20)
list_students(CS_class)
print("=" * 20)
list_courses(B2_courses)
print("=" * 20)
CS_class_mark = input_mark(CS_class, B2_courses)
print("=" * 20)
show_mark(CS_class_mark[0], CS_class_mark[1])
