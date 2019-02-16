"""
#File: student.py

Resources to manage a student's name and test scores.
"""

class Student():
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initally 0."""
        self.myName = name
        self.myScores = []
        for count in range(number):
            self.myScores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.myName
    
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.myScores[i-1] = score

    def getScore(self):
        """Returns the ith score, counting from 1."""
        return self.myScores[i-1]
    def getAverage(self):
        """Returns the average score."""
        sum = 0.0
        for num in self.myScores:
            sum = sum + num
        average = sum/len(self.myScores)
        return average
    def getHighScore(self):
        """Returns the highest score."""
        highest = 0
        for grade in self.myScores:
            if grade > highest:
                highest = grade
        return highest
    def __str__(self):
        """Returns the string representation of the student."""
        ans = "Name: " + self.myName + "\n"
        ans = ans + "Scores: "
        for grade in self.myScores:
            ans = ans + str(grade) + " "
        return ans
    
