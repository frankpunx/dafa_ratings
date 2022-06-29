from player import Player
import trueskill as ts

# trueskill average player is mu = 25, sigma = 8.33

# PS: Values used for mu and sigmas are examples not real ratings

# Team 1
# 2 players

# p1 very good skills
p1 = Player(1, 15, 0, 40, 4)

# p2 good skills
p2 = Player(2, 9, 4, 30, 6.5)

rating_p1 = ts.Rating(p1.mu, p1.sigma)
rating_p2 = ts.Rating(p2.mu, p2.sigma)

team_1_ratings = [rating_p1, rating_p2]





# Team 2
# 2 players

# p1 good skills
p3 = Player(3, 12, 3, 34, 5)

# p2 good skills
p4 = Player(4, 13, 4, 32, 6)

rating_p3 = ts.Rating(p3.mu, p3.sigma)
rating_p4 = ts.Rating(p4.mu, p4.sigma)

team_2_ratings = [rating_p3, rating_p4]




## Stats ##

print("STATS")

p1.print_player_stats()
p2.print_player_stats()
p3.print_player_stats()
p4.print_player_stats()

# < 50 unfair game
print(f'\nTeam 1 Vs Team 2 chance to draw: {ts.quality([team_1_ratings, team_2_ratings])}\n')





# Team 1 and Team 2 play a game
# Team 2 wins the game

p1.add_loss()
p2.add_loss()

p3.add_win()
p4.add_win()

# new ratings
(new_r1, new_r2), (new_r3, new_r4) = ts.rate([team_1_ratings, team_2_ratings], ranks=[1, 0]) # lower rank wins

p1.mu = new_r1.mu
p1.sigma = new_r1.sigma
p2.mu = new_r2.mu
p2.sigma = new_r2.sigma
p3.mu = new_r3.mu
p3.sigma = new_r3.sigma
p4.mu = new_r4.mu
p4.sigma = new_r4.sigma





## Stats ##

print("STATS")

p1.print_player_stats()
p2.print_player_stats()
p3.print_player_stats()
p4.print_player_stats()

# Obs: Teams got more even