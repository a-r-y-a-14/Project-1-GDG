dict = {}
def add_student(dict,name,scores):
    name = input("Enter the name of the student:")
    scores = eval(input("Enter the scores:[maths,physics,chemistry]"))
    if name in dict.keys():
        print("Student",name,"aldready added, use update_scores to update scores")
    else:
        dict[name] = scores
        print("Student",name,"added succesfully")

def update_scores(dict,name,scores):
    name = input("Enter the name of the student:")
    scores = eval(input("Enter the scores:[maths,physics,chemistry]"))
    if name in dict.keys():
        dict[name] = scores
        print("Scores of",name,"updated succesfully")
    else:
        print("Student",name,"doesn't exist, use add_student to add them")

def get_stats(dict,name):
    name = input("Enter the name of the student:")
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

def display_students(dict):
    for x in dict.items():
        print(x)
    else:
        print("No stuidents available")


#_main_
f = input("Do you want to continue?(yes/no)")
while f == "yes":
    func = input("Enter the function to be done(add_student,update_scores,display_students,get_statistics,stop):")
    if func == "add_students":
        add_student(dict,"name","scores")
    elif func == "update_scores":
        update_scores(dict,"name","scores")
    elif func == "get_stats":
        get_stats(dict,"name")
    elif func == "display_students":
        display_students(dict)
    else:
        print("Thank you, have a nice day!!")
        break
else:
    print("Thank you, have a nice day!!")