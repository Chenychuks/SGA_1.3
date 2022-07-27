#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-07-23
Purpose: working with OOP in python
"""


class student:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@stutent.com'

    def fullname(self):
        return '{} {}'. format(self.first, self.last)
# Task 1 Create a class called “Group_leader” that inherits from the class “Students”


class Group_Leader(student):
    def __init__(self, first, last, student=None):
        super() .__init__(first, last)
        if student is None:
            self.student = []
        else:
            self.student = student
# Task 2 Define a method that adds students to the list of student under the group leader.

    def add_stud(self, stud):
        if stud not in self.student:
            self.student.append(stud)
# Task 3 Define a method that removes students from the list of students under the group leader.

    def remove_stud(self, stud):
        if stud in self.student:
            self.student.remove(stud)
# Task 4 Define a method that prints out the full names of students in the list of students under group leader.

    def print_stud(self):
        for stud in self.student:
            print('-->', stud.fullname())


# Task 5 Create 3 more instances of the parent class student.
Stud_1 = student('joy', 'James')
stud_2 = student('Balley', 'Kenny')
stud_3 = student('John', 'White')
stud_4 = student('Adeoye', 'Peace')
stud_5 = student('Daniel', 'King')
# Task 6 Create 2 instances of the sub class Group leader.

Leader1 = Group_Leader('Grace', 'Okon', [Stud_1])
Leader2 = Group_Leader('Millicent', 'Akon', [stud_2])
# Task 7 dd 2 students each to the list of students under the instances of Group leader sub class
Leader1.add_stud(stud_5)
Leader1.add_stud(stud_3)
Leader2.add_stud(stud_4)

# Task 8 Remove 1 student each from the list of students under the group leader sub class
Leader1.remove_stud(Stud_1)
Leader2.remove_stud(stud_2)

# Task 9 Print the full name of the students in the list of students under the instances of the group leader subclass.

Leader1.print_stud()
Leader2.print_stud()

# Task 10 Print the email of the instances of the group leader subclass.

print(Leader1.email)
print(Leader2.email)
