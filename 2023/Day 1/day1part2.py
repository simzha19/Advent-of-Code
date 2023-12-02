input_file = open('input.txt', 'r')

digit_to_text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def min_and_max_in_line(number_to_index):
    curr_min = -1
    curr_max = -1
    min = ''
    max = ''
    for i in range(len(number_to_index)):
        for j in range(len(number_to_index[i])):
            if curr_min == -1 or number_to_index[i][j] < curr_min:
                curr_min = number_to_index[i][j]
                min = str(i)
            if curr_max == -1 or number_to_index[i][j] > curr_max:
                curr_max = number_to_index[i][j]
                max = str(i)
    return min+max

count = 0
for line in input_file.readlines():
    number_to_index = []
    curr_num = ''
    # Find all occurences of text in the string
    for digit in range(len(digit_to_text)):
        curr_digit = digit_to_text[digit]
        indices = [i for i in range(len(line)) if line.startswith(curr_digit, i)]
        number_to_index.append(indices)
    for index in range(len(line)):
        if line[index].isdigit():
            number_to_index[int( line[index])].append(index)
    curr_line_value = int(min_and_max_in_line(number_to_index))
    count += curr_line_value

print(count)
