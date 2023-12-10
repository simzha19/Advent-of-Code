input_file = open('input.txt', 'r')

symbol_coords = {}
number_coords = {}

input_file_lines = input_file.readlines()

for line_index in range(len(input_file_lines)):
    line = input_file_lines[line_index]
    curr_num = ''
    curr_num_coords = (0,0)
    for letter_index in range(len(line.strip())):
        current_letter = line[letter_index]
        if not current_letter == '.' and not current_letter.isdigit():
            current_symbol_coords = (line_index, letter_index)
            symbol_coords[current_symbol_coords] = current_letter
        if current_letter.isdigit():
            if curr_num == '':
                curr_num_coords = (line_index, letter_index)
            curr_num += current_letter
        if (not current_letter.isdigit() or letter_index == len(line.strip()) - 1) and curr_num != '':
            number_coords[curr_num_coords] = curr_num
            curr_num = ''

added_nums = {}

def add_number(curr_num, number_coord, adjacent_numbs):
    if number_coord not in added_nums:
        added_nums[number_coord] = curr_num
        adjacent_numbs.append(curr_num)
def find_adjacent_number(symbol_coord):
    x,y = symbol_coord
    adjacent_numbs = []
    for number_coord in number_coords:
        numb_x, numb_y = number_coord
        curr_num = number_coords[number_coord]
        # Number is above or top left
        if numb_x == x - 1:
            if numb_y <= y and (numb_y + len(curr_num) - 1) >= y - 1:
                add_number(curr_num, number_coord,adjacent_numbs)
            elif numb_y == y + 1:
                add_number(curr_num, number_coord,adjacent_numbs)
        elif numb_x == x + 1:
            if numb_y <= y and (numb_y + len(curr_num) - 1) >= y - 1:
                add_number(curr_num, number_coord,adjacent_numbs)
            elif numb_y == y + 1:
                add_number(curr_num, number_coord, adjacent_numbs)
        elif numb_x == x:
            if (numb_y + len(curr_num) - 1) == y - 1:
                add_number(curr_num, number_coord,adjacent_numbs)
            if numb_y == y + 1:
                add_number(curr_num, number_coord,adjacent_numbs)
    print(adjacent_numbs)

sum = 0
for symbol_coord in symbol_coords:
    find_adjacent_number(symbol_coord)

for coords in added_nums:
    sum += int(added_nums[coords])
print(sum)

