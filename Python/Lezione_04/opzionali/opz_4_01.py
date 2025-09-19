'''1. School Grading System:

     Create a function that takes a student's name and their 
     scores in different subjects as input.
    The function calculates the average score and prints the 
    student's name, average, and a message indicating whether 
    the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and 
    scores, calling the function for each student.
'''


def student_average(name, *args):
    sum: int = 0
    for arg in args:
        sum += arg
    avg: float = sum / len(args)
    if avg >= 60:
        print(f"Dear {name} you've successfully passed your exam with an average of {avg}")
    else:
        print(f"Dear {name} you've did not passed your exam due to the average of {avg}")

student_average("Marco", 57, 43, 78, 87, 61, 100)

student_list: list[str, int] = ["Studente1", 48, 86, 28, 75, 86, 
                                "Studente2", 96, 27, 90, 82, 37, 
                                "Studente3", 39, 69, 96, 46, 72]

votes_list: list[int] = []
for i in range(len(student_list)):
    if type(student_list[i]) == str:
        student: str = student_list[i]
    else:
        votes_list.append(student_list[i])
        if i == len(student_list) - 1:
            votes_tuple: tuple = tuple(votes_list)
            student_average(student, *votes_tuple)
        elif type(student_list[i+1]) == str:
            votes_tuple: tuple = tuple(votes_list)
            student_average(student, *votes_tuple)
            votes_list: list[int] = []
