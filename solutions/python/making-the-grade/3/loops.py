"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    # print('debug2',student_scores)
    int_list = []
    for score in student_scores:
        round_off = round(score)
        # print('debug3',round_off)
        int_list.append(round_off)
        # print('debug1',int_list,type(int_list))
    return int_list
        
    # round_off = round(student_scores)
    # print('debug1',round_off)

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    # fail_students = []
    for score in student_scores:
        if score <= 40:
            # fail_students.append(score)
            count = count + 1
    return count
  
def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_marks = []
    for score in student_scores:
        if score >= threshold:
            best_marks.append(score)
    return best_marks


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    result = 0
    grade_list = [41]
    mark_range = highest - 40
    slot = mark_range // 4
    for index in range(0,3):
        if index == 0:
            result = slot + 41
            grade_list.append(result)
        else:
            result =result +slot
            grade_list.append(result)
    return grade_list
 

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    # print(f'debug2 {student_names}')
    # print(f'debug3 {student_scores}')
    rank = 1
    format_list = []
    for index,score in enumerate(student_scores):
        # print(f'debug4 {index}')
        # print(f'debug5 {score}')
        temp = f"{rank}. {student_names[index]}: {score}"
        rank = rank + 1
        format_list.append(temp)
    return format_list

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    # print('debug1',student_info)
    # topper = []
    for value in student_info:
        if value[1] == 100:
            # topper.append(value)
            # print(f'debug2 {topper}')
            # print(f'debug2 {value}')
            # topper.append(value)
            return value    
    return []