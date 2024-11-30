dict = {}
def add_student(dict,name,scores):
    name = input("Enter the name of the student:")
    scores = eval(input("Enter the scores:"))
    if name in dict.keys():
        print("Student",name,"aldready added, use update_scores to update scores")
    else:
        dict[name] = scores
        print("Student",name,"added succesfully")

def update_scores(dict,name,scores):
    name = input("Enter the name of the student:")
    scores = eval(input("Enter the scores:"))
    if name in dict.keys():
        dict[name] = scores
        print("Scores of",name,"updated succesfully")
    else:
        print("Student",name,"doesn't exist, use add_student to add them")


#_main_
add_student(dict,"name","scores")
update_scores(dict,"name","scores")