def get_list_of_lists():
	season_games = []
	with open('nhl_season_games.csv') as file:
		for line in file.readlines():
			season_games.append(line.strip('\n').split(','))

	return season_games
