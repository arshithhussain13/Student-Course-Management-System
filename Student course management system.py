class CourseLimitError(Exception):
    pass

class Student:
    max_courses = 5
    
    def _init_(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
        self.courses = []
        self.marks = []
        
    def add_courses(self, course_name: str, mark: int):
        try:
            if course_name in self.courses:
                raise ValueError("Course already exists")
                
            if len(self.courses) >= self.max_courses:
                raise CourseLimitError("Cannot enroll more than 5 courses")
                
            if not (0 <= mark <= 100):
                raise ValueError("Marks must be between 0 and 100")
            
            self.courses.append(course_name)
            self.marks.append(mark)
            
        except(ValueError, CourseLimitError) as e:
            print("Add Course Error:",e)
    
    def remove_courses(self, course_name: str):
        try:
            index = self.courses.index(course_name)
            self.courses.remove(course_name)
            self.marks.pop(index)
            
        except ValueError:
            print("Remove Course Error: Course not found")
            
    def get_average_marks(self):
        try:
            total = sum(self.marks)
            count = len(self.marks)
            return total / count
            
        except ZeroDivisionError:
            print("Average Error: No courses available")
            return 0
            
    def get_unique_courses(self):
        return set(self.courses)
        
    def _str_(self):
        return (
            f"Student_Id:{self.student_id}\n"
            f"Name:{self.name}\n"
            f"Courses:{self.courses}\n"
            f"Marks:{self.marks}\n"
            f"Average:{self.get_average_marks()}")
        
s1 = Student(101, "Arshith")
s2 = Student(102, "Arjun")

s1.add_courses("Python", 80)
s1.add_courses("Java", 90)
s1.add_courses("SQL", 85)
s1.add_courses("AI", 75)

s1.remove_courses("AI")
s1.remove_courses("SQL")

s2.add_courses("Java", 95)
s2.add_courses("SQL", 80)

print(s1)
print(s2)