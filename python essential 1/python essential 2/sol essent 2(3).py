class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            # Check if the list is empty
            if len(self.scores) == 0:
                raise ValueError
            
            # Using indexing to get first and last score
            first_score = self.scores[0]
            last_score = self.scores[-1]
            difference = last_score - first_score
            
            print("Difference between last and first score is:", difference)

        except ValueError:
            print("No scores available to calculate difference")


# Example Usage
scores = [55, 65, 75, 85]
student = StudentPerformance(scores)
student.score_difference()