dict = {}
f = input("Do you want to continue?(yes/no)")
while f == "yes":
    func = input("Enter the function to be done(add_student,update_scores,display_students,get_statistics,stop):")

    #_add_student
    if func == "add_student":
        name = input("Enter the name:")
        scores = eval(input("Enter the scores:[maths,physics,chemistry]"))
        if name in dict.keys():
            print("Student",name,"aldready added, use update_scores to update scores")
        else:
            dict[name] = scores
            print("Student",name,"added succesfully")
        continue

    #_update_scores
    if func == "update_scores":
        name = input("Enter the name:")
        scores = eval(input("Enter the scores:[maths,physics,chemistry]"))
        if name in dict.keys():
            dict[name] = scores
            print("Scores of",name,"updated succesfully")
        else:
            print("Student",name,"doesn't exist, use add_student to add them")
        continue

    #display_students
    if func == "display_students":
        for x in dict.items():
            print(x)
        continue

    #_get_statistics
    if func == "get_statistics":
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
        continue

    if func == "stop":
        print("Thank you, have a nice day!")
        break      
else:
    print("Thank you, have a nice day!")