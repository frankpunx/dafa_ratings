# dafa_ratings
Code for technical exam

## About
This repo has the sample code how to estimate players rankings (skill level) for games e.g. N:N

There are 2 different approaches:

1 - Implementing the Glicko algorithm.

2 - Using the python library [TrueSkill](https://trueskill.org/)

For approach 1 the skill level of the team is calculated based on the average mu and sigma of the opposite team (this is a limitation of the current implementation).

For approache 2 the library implements team N:N match rule.

### Assumptions
- Even teams
- Teams ranks have similar skills
- Ranking system (1 and 2) only uses the final standings of the teams in a match in order to update the skill.

### Files
- player.py - class Player
- glicko.py - implementation of glicko algorithm
- glicko_example.py - use case of the glicko algorithm
- trueSkill_example - use case of the TrueSkill python library



