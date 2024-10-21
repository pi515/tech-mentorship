from secret_things import get_list_of_lists

# season_games[0] = [home_team, away_team, home_score, away_score]
# season_games[0] = ['Columbus Blue Jackets', 'LA Kings', 10, 5]
season_games = get_list_of_lists()

# {teamName: teamScore...} 
# {'Columbus Blue Jackets': 1, 'LA Kings': -1, ...} 
team_scores = {}

# fill in dict with team names and initialise to 0
for game in season_games:
	team_scores[game[0]] = 0 # home team
	team_scores[game[1]] = 0 # away team


for game in season_games:
	home_team = game[0]
	away_team = game[1]
	home_score = game[2]
	away_score = game[3]

	if home_score > away_score:
 		team_scores[home_team] += 1
 		team_scores[away_team] -= 1
	elif home_score < away_score:
		team_scores[away_team] += 1
		team_scores[home_team] -= 1
	else:
		team_scores[away_team] += 0.5
		team_scores[home_team] += 0.5

for k, v in team_scores.items():
	print(k, v)
