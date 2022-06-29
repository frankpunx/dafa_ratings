import math

# Glicko algorithm implementation

sigma = 350 # 350 is assumed to be the RD of an unrated player

q = math.log(10) / 400

def g_RD_i(RD_i):
    return 1 / math.sqrt(1 + (3 * q**2 * RD_i**2) / math.pi**2)

def E_s_r0_ri_RDi(RD_i, r_0, r_i):
    return 1 / (1 + 10**(g_RD_i(RD_i) * (r_0 - r_i) / -400))


def glicko(player, RD_0, c, t, opposing_team_avg, S):
    """
    Glicko rating system. returns new mu and sigma for player.

    Parameters
    ----------
    player : Player
        player to rate
    RD_0 : float
        player to rate current sigma
    c : float
         constant that governs the increase in uncertainty between rating periods.
    t : int
        rating period since the last competition.
    opposing_team_avg : array
        ratings for oppoing team. len of number of games played in the last period.
    S : int
        results of games played. 0 == LOSS, 1 == WIN. len of number of games played in the last period.

    
    """

    # new rating deviation
    RD = min(math.sqrt(RD_0**2 + c**2 * t), sigma)

    sum_d2 = 0
    for p in opposing_team_avg:
        sum_d2 += (g_RD_i(p["sigma"]))**2 * E_s_r0_ri_RDi(p["sigma"], player.mu, p["mu"]) * (1 - E_s_r0_ri_RDi(p["sigma"], player.mu, p["mu"]))

    d2 = 1 / (q**2 * sum_d2)

    sum_r = 0
    for p, si in zip(opposing_team_avg, S):
        sum_r += g_RD_i(p["sigma"]) * (si - E_s_r0_ri_RDi(p["sigma"], player.mu, p["mu"]))

    r = player.mu + (q / ((1 / RD**2) + (1 / d2))) * sum_r

    new_RD = math.sqrt(((1 / RD**2) + (1 / d2))**(-1))

    return r, new_RD



