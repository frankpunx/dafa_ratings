from glicko import glicko
from player import Player
from utils import team_avg_ratings

LOSS = 0
WIN = 1

# glicko average player is mu = 1500, sigma = 350

# PS: Values used for mu and sigmas are examples not real ratings

# Team 1
# 2 players

# p1 very good skills
p1 = Player(1, 15, 0, 1900, 150)

# p2 good skills
p2 = Player(2, 9, 4, 1600, 250)

team_mu_1, team_sigma_1 = team_avg_ratings([p1, p2])





# Team 2
# 2 players

# p1 good skills
p3 = Player(3, 12, 3, 1650, 240)

# p2 good skills
p4 = Player(4, 13, 4, 1700, 220)

team_mu_2, team_sigma_2 = team_avg_ratings([p3, p4])


## Stats ##

print("STATS")

p1.print_player_stats()
p2.print_player_stats()
p3.print_player_stats()
p4.print_player_stats()

print(f'\nTeam 1 mu (avg), sigma (avg): {team_mu_1} {team_sigma_1}\n')

print(f'\nTeam 2 mu (avg), sigma (avg): {team_mu_2} {team_sigma_2}\n')


# Team 1 and Team 2 play a game
# Team 2 wins the game

p1.add_loss()
p2.add_loss()

p3.add_win()
p4.add_win()

# new ratings

uncertainty = 69
period = 1


new_mu_p1, new_sigma_p1 = glicko(p1, p1.sigma, uncertainty, period, [{"mu": team_mu_2, "sigma": team_sigma_2}], [LOSS])
new_mu_p2, new_sigma_p2 = glicko(p2, p2.sigma, uncertainty, period, [{"mu": team_mu_2, "sigma": team_sigma_2}], [LOSS])
new_mu_p3, new_sigma_p3 = glicko(p3, p3.sigma, uncertainty, period, [{"mu": team_mu_1, "sigma": team_sigma_1}], [WIN])
new_mu_p4, new_sigma_p4 = glicko(p4, p4.sigma, uncertainty, period, [{"mu": team_mu_1, "sigma": team_sigma_1}], [WIN])

p1.mu = new_mu_p1
p1.sigma = new_sigma_p1
p2.mu = new_mu_p2
p2.sigma = new_sigma_p2
p3.mu = new_mu_p3
p3.sigma = new_sigma_p3
p4.mu = new_mu_p4
p4.sigma = new_sigma_p4





## Stats ##

print("STATS")

p1.print_player_stats()
p2.print_player_stats()
p3.print_player_stats()
p4.print_player_stats()
