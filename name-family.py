class Student:
    courseMarks={}
    name= ""
    family
    def __init__(self, name, family):
        self.name = name
        self.family = family
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
    def average(self):
        theSum = 0
        i = 0
        for course in courseMarks:
            theSum += courseMarks[course]
            i += 1
        if (i == 0):
            return 0
        return theSum/i