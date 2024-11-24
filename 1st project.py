class StudentExamScoresTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        """Add a new student and their scores."""
        if name in self.students:
            print(f"Student '{name}' already exists. Use 'update_scores' to modify scores.")
        else:
            self.students[name] = scores
            print(f"Added student '{name}' with scores: {scores}")

    def update_scores(self, name, scores):
        """Update scores for an existing student."""
        if name in self.students:
            self.students[name] = scores
            print(f"Updated scores for '{name}' to: {scores}")
        else:
            print(f"Student '{name}' does not exist. Use 'add_student' to add them first.")
    
    def display_students(self):
        """Display all students and their scores."""
        if self.students:
            print("Student List:")
            for name, scores in self.students.items():
                print(f"  {name}: {scores}")
        else:
            print("No students available.")

    def statistics(self, name):
        """Calculate and return average, highest, and lowest scores for a student."""
        if name in self.students:
            scores = self.students[name]
            if scores:
                avg_score = sum(scores) / len(scores)
                highest_score = max(scores)
                lowest_score = min(scores)
                print(f"Statistics for '{name}':")
                print(f"  Average Score: {avg_score}")
                print(f"  Highest Score: {highest_score}")
                print(f"  Lowest Score: {lowest_score}")
                return avg_score, highest_score, lowest_score
            else:
                print(f"No scores available for '{name}'.")
        else:
            print(f"Student '{name}' not found.")
        return None
    
    def remove_student(self, name):
        """Remove a student from the system."""
        if name in self.students:
            del self.students[name]
            print(f"Removed student '{name}' from the system.")
        else:
            print(f"Student '{name}' does not exist.")


#_main_

tracker = StudentExamScoresTracker()

  #_Add_students
tracker.add_student("Ram", [97, 92, 88])
tracker.add_student("Shyam", [68, 73, 85])

  #_Update_scores
tracker.update_scores("Ram", [95, 98, 67])

  #_Display_students
tracker.display_students()

  #_Calculate_statistics
tracker.calculate_statistics("Ram")
tracker.calculate_statistics("Shyam")

  #_Remove_Student
tracker.remove_student("Ram")


