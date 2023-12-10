import re

input_file = open('input.txt', 'r')

remove_beginning_string = r'Card  *(\d+):'

sum_of_all_games = 0
for line in input_file.readlines():
    curr_game = re.sub(remove_beginning_string, '', line)
    numbers = curr_game.split("|")
    winning_numbers = [int(number) for number in numbers[0].strip().split()]
    my_numbers = [int(number) for number in numbers[1].strip().split()]
    won = 0
    for number in my_numbers:
        if number in winning_numbers:
            if won == 0:
                won += 1
            else:
                won *= 2
    sum_of_all_games += won

print(sum_of_all_games)