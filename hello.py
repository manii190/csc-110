def main():
    

def point_grade(score, total_points):
    percentage = (score / total_points) * 100 #total percentage
    return round(percentage, 2) #round to 2

def get_grade_results(score, total_points):
    percentage = point_grade(score, total_points) #percentage
    grade = letter_grade(percentage)
    result = pass_or_fail(grade)
    message = "Your grade is " + str(percentage) + \
        " (" + str(grade) + " - " + str(result) +")"
    return message