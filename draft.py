dict = {}

#_add_student_
def add_student(dict,name,scores):
    if name in dict:
        print("Student",name,"aldready added, use update_scores to update scores")
    else:
        dict[name] = scores
        print("Student",name,"added succesfully")

#_update_scores
def update_scores(dict,name,scores):
    if name in dict:
        dict[name] = scores
        print("Scores of",name,"updated succesfully")
    else:
        print("Student",name,"doesn't exist, use add_student to add them")

#_display_students
def display_students(dict):
    for x in dict.items():
        print(x)

#_statistics
def statistics(dict,name):
    if name in dict:
        scores = dict[name]
        if scores:
            avg_score = sum(scores) / len(scores)
            highest_score = max(scores)
            lowest_score = min(scores)
            print("Statistics for",name,":")
            print("Average Score:",avg_score)
            print("Highest Score:",highest_score)
            print("Lowest Score:",lowest_score)
        else:
            print("No scores available for:",name)
    else:
        print("Student",name,"doesn't exist, use add_student to add them")

#_remove_student
def remove_student(dict,name):
    if name in dict:
        del dict[name]
        print("Student",name,"removed succesfully")
    else:
        print("Student",name,"doesn't exist")

#_main_
add_student(dict,"John",[23,67,43])
update_scores(dict,"John",[34,92,99])
update_scores(dict,"Dahl",[34,92,99])
display_students(dict)
statistics(dict,"John")
remove_student(dict,"John")
remove_student(dict,"Dahl")