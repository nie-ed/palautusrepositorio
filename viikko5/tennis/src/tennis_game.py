class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.equal_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.player_advantage_or_won()
        
        else:
            return self.current_score()

    def equal_score(self):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
    
    def player_advantage_or_won(self):
        difference_in_scores = self.player1_score - self. player2_score

        if difference_in_scores == 1:
            score = "Advantage player1"
        elif difference_in_scores == -1:
            score = "Advantage player2"
        elif difference_in_scores >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"        
        return score
    
    def current_score(self):
        if self.player1_score == 0:
            score = "Love"
        elif self.player1_score == 1:
            score = "Fifteen"
        elif self.player1_score == 2:
            score = "Thirty"
        else:
            score = "Forty"

        if self.player2_score == 0:
            score += "-Love"
        elif self.player2_score == 1:
            score += "-Fifteen"
        elif self.player2_score == 2:
            score += "-Thirty"
        else:
            score += "-Forty"
        return score