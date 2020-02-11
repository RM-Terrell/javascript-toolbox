import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/grading/problem
def round_check(grade):
    """
    :param int grade:
    :return int grade:
    """
    # rounding range is within 3 of next multiple of 5
    for round_idx in range(1, 3):
        round_test = grade + round_idx
        if round_test % 5 == 0:
            grade = round_test
            break
    return grade


def gradingStudents(grades):
    """
    :param [int] grades:
    :return [int] rounded_grades:
    """
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
            continue
        rounded_grades.append(round_check(grade))

    return rounded_grades


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print(result)
