
class Player(object):
    """
    Player class : represents a player in a game.
    It contains player stats such as number of wins and losses.
    mu is the rank of the player, sigma is (deviation) measures the accuracy of the rating.
    """

    def __init__(self, player_id, num_wins = 0, num_losses = 0, mu = 1500, sigma = 350):
        self.player_id = player_id
        self.num_wins = num_wins
        self.num_losses = num_losses
        self.mu = mu
        self.sigma = sigma

    def get_total_played(self):
        return self.num_wins + self.num_losses

    def get_percentage_wins(self):
        if self.get_total_played() == 0:
            return 0
        else: 
            return self.num_wins / self.get_total_played()

    def add_win(self):
        self.num_wins += 1

    def add_loss(self):
        self.num_losses += 1

    def print_player_stats(self):
        print(f'\nPlayer {self.player_id}')
        print(f'Total games played: {self.get_total_played()}')
        print(f'Percentage games won: {self.get_percentage_wins()}')
        print(f'Rating: MU - {self.mu}, SIGMA - {self.sigma}')
        print("-----------------------")


    