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
    game_max_color_counts = {'red': 0, 'blue': 0, 'green': 0}
    for games in curr_game.split(';'):
        color_counts = {'red': 0, 'blue': 0, 'green': 0}
        for marble in games.split(','):
            number, color = extract_number_and_color(marble.strip())
            if color in color_counts:
                color_counts[color] += number
        for colors in color_counts:
            game_max_color_counts[colors] = max(game_max_color_counts[colors], color_counts[colors])
    power_of_curr_game = 1
    for color in game_max_color_counts:
        power_of_curr_game *= game_max_color_counts[color]
    count += power_of_curr_game
print(count)