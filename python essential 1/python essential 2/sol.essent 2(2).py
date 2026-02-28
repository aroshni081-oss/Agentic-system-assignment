class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            # Check if there are at least 2 scores
            if len(self.scores) < 2:
                raise ValueError
            
            # Using negative indexing to get last two scores
            last_two = self.scores[-2:]
            highest = max(last_two)
            print("Highest score among last two is:", highest)

        except ValueError:
            print("Not enough scores to find highest value")


scores = [45, 67, 89, 72]
student = StudentScores(scores)
student.highest_last_two()
