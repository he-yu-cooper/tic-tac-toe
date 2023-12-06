# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.score_history = []

    def update_score(self, points):
        self.score += points
        self.score_history.append(points)

    def get_total_score(self):
        return sum(self.score_history)

    def __str__(self):
        return f"{self.name} - Score: {self.score}, Total Score: {self.get_total_score()}"
