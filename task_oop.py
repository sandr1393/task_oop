
from itertools import chain

student = {'Ruoy':[10, 8, 8],'Tony':[10, 9, 10]}
lecterer = {'ivan':[10, 10, 10],'jon':[9, 10, 9]}

print()

def average_value_rating(data_dict):
    """Расчет среднего значений словаря

    :type data_dict: dict
    :type return: str

    """
    res = list(chain(*data_dict.values()))
    if len(res) == 0:
        return f'Нет оценок'
    else: 
        res = list(chain(*data_dict.values()))
        return f'{(sum(res)/len(res)):.2f}'
    return res
        

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

 
    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            # print("Лектор действительно преподователь. И студент и лектор на одном курсе")
            if course in lecture.grades_students:
                lecture.grades_students[course] += [grade]
            else:
                lecture.grades_students[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \
            \nСредняя оценка за лекции: {average_value_rating(self.grades)}\
            \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\
            \nЗавершенные курсы: {', '.join(self.finished_courses)}'
    
    def __eq__(self, other):
        if average_value_rating(ruoy_student.grades) == average_value_rating(tony_student.grades):
            return 'Cтуденты учатся одинаково'
        elif average_value_rating(ruoy_student.grades) < average_value_rating(tony_student.grades):
            return f'Лучший студент:\n{tony_student}'
        else:
            return f'Лучший студент:\n{ruoy_student},'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_students = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \
            \nСредняя оценка за лекции: {average_value_rating(self.grades_students)}' 
    
    def __eq__(self, other):
        if average_value_rating(ivan_lecterer.grades_students) == average_value_rating(jon_lecterer.grades_students):
            return 'Преподавателей оценили одинаково'
        elif average_value_rating(ivan_lecterer.grades_students) > average_value_rating(jon_lecterer.grades_students):
            return f'Лучший преподаватель:\n{ivan_lecterer}'
        else:
            return f'Лучший преподаватель:\n{jon_lecterer},'

class Reviewer (Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}" 

ruoy_student = Student('Ruoy', 'Eman', 'your_gender')
ruoy_student.courses_in_progress += ['Python', 'Git', 'JavaScript']
ruoy_student.finished_courses += ['CSS', 'HTML']

tony_student = Student('Tony', 'Stark', 'Iron Man')
tony_student.courses_in_progress += ['Python']
tony_student.finished_courses += ['Курс по спасению вселенной','Ассеблер']

alex_reviewer = Reviewer('Alex', 'Markof')
alex_reviewer.courses_attached += ['Python', 'Git']
alex_reviewer.rate_hw(ruoy_student, ruoy_student.courses_in_progress[0], 10)
alex_reviewer.rate_hw(ruoy_student, ruoy_student.courses_in_progress[0], 8)
alex_reviewer.rate_hw(ruoy_student, ruoy_student.courses_in_progress[0], 8)
alex_reviewer.rate_hw(ruoy_student, ruoy_student.courses_in_progress[1], 10)

alex_reviewer.rate_hw(tony_student, ruoy_student.courses_in_progress[0], 10)
alex_reviewer.rate_hw(tony_student, ruoy_student.courses_in_progress[0], 9)
alex_reviewer.rate_hw(tony_student, ruoy_student.courses_in_progress[0], 10)

ivan_lecterer = Lecturer('Ivan', 'Super')
ivan_lecterer.courses_attached += ['Python', 'Git']

jon_lecterer = Lecturer('Jon', 'Snow')
jon_lecterer.courses_attached += ['Python', 'Java']

ruoy_student.rate_lecture(ivan_lecterer, ruoy_student.courses_in_progress[0], 10)
ruoy_student.rate_lecture(ivan_lecterer, ruoy_student.courses_in_progress[0], 10)
ruoy_student.rate_lecture(ivan_lecterer, ruoy_student.courses_in_progress[0], 10)
ruoy_student.rate_lecture(ivan_lecterer, ruoy_student.courses_in_progress[1], 10)
ruoy_student.rate_lecture(ivan_lecterer, ruoy_student.courses_in_progress[1], 9)

ruoy_student.rate_lecture(jon_lecterer, ruoy_student.courses_in_progress[0], 9)
ruoy_student.rate_lecture(jon_lecterer, ruoy_student.courses_in_progress[0], 10)
ruoy_student.rate_lecture(jon_lecterer, ruoy_student.courses_in_progress[0], 9)


print(alex_reviewer)
print(ivan_lecterer)
print(jon_lecterer)
print(ruoy_student)
print(tony_student)
print(ivan_lecterer == jon_lecterer)
print(ruoy_student == tony_student)
print(f'Среняя оценка всех студентов {average_value_rating(student)}')
print(f'Среняя оценка всех лекторов {average_value_rating(lecterer)}')
