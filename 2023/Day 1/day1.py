input_file = open('input.txt', 'r')

count = 0
for line in input_file.readlines():
    curr_num = ''
    curr_line = ''.join(filter(str.isdigit, line))
    curr_num = curr_line[0] + curr_line[-1]
    curr_num = int(curr_num)
    count += curr_num

print(count)
