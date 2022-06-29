
def team_avg_ratings(team_array):
    """Given an array of Player objects Returns the mu's and sigma's average.

    Parameters
    ----------
    team_array : array
        array with a team of players.
    """
    team_size = len(team_array)
    sum_mu = 0
    sum_sigma = 0

    for p in team_array:
        sum_mu += p.mu
        sum_sigma += p.sigma

    return sum_mu / team_size, sum_sigma / team_size
