class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # Check if there are at least 3 marks
            if len(self.marks) < 3:
                raise ValueError
            
            # Using negative indexing to get last three marks
            last_three = self.marks[-3:]
            average = sum(last_three) / 3
            print("Average of last 3 marks is:", average)

        except ValueError:
            print("Not enough marks to calculate average")



marks = [50, 60, 70, 80, 90]
student = StudentMarks(marks)
student.last_three_avg()
