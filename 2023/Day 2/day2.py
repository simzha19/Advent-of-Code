import re

input_file = open('input.txt', 'r')

remove_beginning_string = r'Game (\d+):'

def extract_number_and_color(input_string):
    pattern = r'(\d+) (red|green|blue)'
    match = re.match(pattern, input_string)

    if match:
        number = int(match.group(1))
        color = match.group(2)
        return number, color
    else:
        return None, None

count = 0
times = 1
for line in input_file.readlines():
    game_number_match = int(re.search(remove_beginning_string, line).group(1))
    curr_game = re.sub(remove_beginning_string, '', line)
    all_games_good = True
    for games in curr_game.split(';'):
        color_counts = {'red': 0, 'blue': 0, 'green': 0}
        for marble in games.split(','):
            number, color = extract_number_and_color(marble.strip())
            if color in color_counts:
                color_counts[color] += number
        if color_counts['red'] > 12 or color_counts['green'] > 13 or color_counts['blue'] > 14:
            all_games_good = False
            break
    if all_games_good:
        count += game_number_match

print(count)