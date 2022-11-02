from solver import Solver
import api

api_key = ''

with open('secret') as f:
	api_key = f.readline().rstrip()

map_name = 'Fancyville'
bag_type = 2
training_map = map_name in ('Suburbia', 'Fancyville')
debugprint=True

def main():
	print('Starting game...')
	response = api.mapInfo(api_key, map_name)
	print(response)
	days = 31 if training_map else 365

	solver = Solver(game_info=response)
	solution = solver.Solve(bag_type, days)

	print(solution.toJSON())

	submit_game_response = api.submit_game(api_key, map_name, solution)

	if debugprint:
		for i, day in enumerate(submit_game_response['weekly']):
			print(day, solution.orders[i])

		print(submit_game_response['score'])

if __name__ == '__main__':
	main()