import re

input_file = open('input.txt', 'r')

remove_beginning_string = r'Card  *(\d+):'

sum_of_all_games = 0
curr_game_num = 1
extra_scratch_cards = {}
for line in input_file.readlines():
    curr_game = re.sub(remove_beginning_string, '', line)
    numbers = curr_game.split("|")
    winning_numbers = [int(number) for number in numbers[0].strip().split()]
    my_numbers = [int(number) for number in numbers[1].strip().split()]
    won = 0
    for number in my_numbers:
        if number in winning_numbers:
            won += 1



    num_scratch_cards_curr_game = 1
    if curr_game_num in extra_scratch_cards:
        num_scratch_cards_curr_game += extra_scratch_cards[curr_game_num]
    sum_of_all_games += num_scratch_cards_curr_game
    for games_won in range(won):
        if curr_game_num + 1 + games_won not in extra_scratch_cards:
            extra_scratch_cards[curr_game_num + 1 + games_won] = num_scratch_cards_curr_game
        else:
            extra_scratch_cards[curr_game_num + 1 + games_won] += num_scratch_cards_curr_game
    curr_game_num += 1

print(sum_of_all_games)