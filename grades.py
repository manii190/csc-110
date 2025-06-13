'''
Mani AbhiramReddy
csc110
project-2
this is above marks,grades ,fail,and
finalaly providing
a
'''
def letter_grade(marks):
    '''
    Fuctions like if and else are used for catagarizing grades by marks
ARGS:each marks as differnt grade
return:grades are a,b,c,d,e,x
    '''
    #Greater or equal to 90, is A grade
    if marks >= 90:
        return 'A'
    
    #Greater or equal to 80, is B grade
    if marks >=80:
        return 'B'
    
    # Greater or equal to 70,is C grade
    if  marks >= 70:
        return 'C'
    
    #Greater or equal to 60,is D grade
    if marks >= 60:
        return 'D'
    
    #less than 60 or equal to 0 ,is E grade
    if marks < 60 and marks >= 0:
        return 'E'
    
    # negative cases or more than 100, is "x" grade
    if marks < 0 or marks > 100:
        return 'X'
    else:
        return 'X'
    
    
def pass_or_fail(grade):
    '''
    this function determines the pass or fail
    
    Args:
        grade: some grade are into pass class and some are into fail class
    Returns:
        it check the grade and give out put that either pass or fail
    '''
    #  letter 'A' is the graded as pass
    if grade == 'A':
        return 'Pass'
    
    # 'B' is the graded as pass
    if grade == 'B':
        return 'Pass'
    
    # 'C' is the graded as pass
    if grade == 'C':
        return 'Pass'
    
    # 'D' is the graded as pass
    if grade == 'D':
        return 'Pass'
    
    #'E' is the grade as fail
    if grade == 'E':
        return 'Fail'
    
    # other cases are showen as fail
    else:
        return 'Error'
    
    
def point_grade(score, total_points):
    '''
    the function calculate the marks by score and total points
    and rounds it to two decimals
    it divide score by total_points into 100
    Args:
        score: the score we get
        total_points: maximum points that can be scored.
    Returns:
        calculated percentage and round it to 2 decimals
    '''
    marks = (score / total_points) * 100
    return round(marks, 2)
def get_grade_results(score, total_points):
    '''
    This function combains all tye pervious funtions
    Args:
        score: the score we get
        total_points: maximum points that can be scored.
    Returns:
        it shows the marks,grade,fail or pass with in a sentences
    '''
    marks = point_grade(score, total_points)
    grade = letter_grade(marks)
    result = pass_or_fail(grade)
    return "Your grade is " + str(round(marks, 2)) + " (" + \
    grade + " - " + result + ")"
def main():
    '''
    the funtion combines all the funtions and show the final result
    Args:
        None
    Returns:
        None
    '''
    # test letter_grade function
    assert letter_grade(90) == "A"
    assert letter_grade(80) == "B"
    assert letter_grade(70) == "C"
    assert letter_grade(60) == "D"
    assert letter_grade(59) == "E"
    assert letter_grade(-59) == "X"
    
    # test pass_or_fail function
    assert pass_or_fail("B") == "Pass"
    assert pass_or_fail("E") == "Fail"
    assert pass_or_fail("ABCD") == "Error"
    
    # test point_grade function
    assert point_grade(0, 100) == 0.0
    assert point_grade(100, 100) == 100.0
    assert point_grade(45, 80) == 56.25
    assert point_grade(37, 40) == 92.5
    
    # test get_grade_results function
    assert get_grade_results(0, 100) == "Your grade is 0.0 (E - Fail)"
    assert get_grade_results(45, 80) == "Your grade is 56.25 (E - Fail)"
    assert get_grade_results(37, 40) == "Your grade is 92.5 (A - Pass)"
main()