def print_upper(len_left_instruction, upper_instructions):
    num_lines = len(upper_instructions[0])
    print(' '*(2 * len_left_instruction -1) + '┬', end='')
    print('─┬'*(len(upper_instructions)))

    for idx_line in range(num_lines):
        print(' '*(len_left_instruction+1), end='')
        for sequence in upper_instructions:
            print(f'│{sequence[idx_line]}', end='')
        print('│')
    
    print('─', end='')
    for i in range(len_left_instruction-1):
        print('┬─', end='')
    print('┼'+'─┴' * (len(upper_instructions)))

def print_curr_instruction(instruction):
    for i in instruction:
        print(f'{i}│', end='')

def print_linear_bitmap(linear_bitmap):
    for pixel in linear_bitmap:
        print('█' if pixel=='m' else '─', end='')
        print('┼', end='')
    print()

def print_below(left_instructions, img):
    for line_idx in range(len(img)):
        print_curr_instruction(left_instructions[line_idx])
        print_linear_bitmap(img[line_idx])

def print_image(left_instructions, upper_instructions, img):
    print_upper(len(left_instructions[0]), upper_instructions)
    print_below(left_instructions, img)

#########################################################################################
def get_upper_instructions1():
    return [
        [4],
        [3],
        [4],
        [1],
        [1]
    ]
def get_left_instructions1():
    return [
        [0, 1],
        [3, 1],
        [0, 4],
        [1, 1],
        [1, 1]
    ]
###########################################################################################################
def get_empty_image(cols, rows):
    img = []
    for _ in range(rows):
        img.append(['?'] * cols)
    return img

def init_knowledge(instruction, max_pixel_size):
    num_instruction = len(instruction)

    min_consequtive_requirements = num_instruction - 1
    for i in range(num_instruction):
        if instruction[i] == 0:
            min_consequtive_requirements -= 1

    for item in instruction:
        min_consequtive_requirements += item
    odef = max_pixel_size - min_consequtive_requirements

    new_knowledge = []
    start_idx = 0
    for i in range(num_instruction):
        sequence = instruction[i]
        
        if sequence == 0:
            new_knowledge.append([0, [[0, 0]]])
        else:
            n = sequence - odef
            if n > 0:
                end_idx = start_idx + sequence + odef
                new_knowledge.append([sequence, [[start_idx, end_idx]]])
                start_idx += sequence + 1
            else:
                new_knowledge.append([sequence, [[start_idx, max_pixel_size]]])
                start_idx += sequence + 1

    return new_knowledge

def update_linear_bitmap_by_scopes(knowledge, max_pixel_size):
    linear_bitmap = [max_pixel_size]

    for info in knowledge:
        instruction = info[0]
        scopes = info[1]

        print('info', info)
        if len(scopes) == 1:
            scope_pair = scopes[0]
            start_fill_idx = scope_pair[1] - instruction
            end_fill_idx =  instruction + scope_pair[0]

            for i in range(start_fill_idx, end_fill_idx):
                linear_bitmap[i] = 'm'

################################################################################################################

upper_instructions = get_upper_instructions1()
left_instructions = get_left_instructions1()
COLS = len(upper_instructions)
ROWS = len(left_instructions)
img = get_empty_image(COLS, ROWS)

for row in range(ROWS):
    curr_knowledge = init_knowledge(left_instructions[row], COLS)
    img[row] = update_linear_bitmap_by_scopes(curr_knowledge, COLS) #todo pushing to a priority queue
print_image(left_instructions, upper_instructions, img)

for col in range(COLS):
    curr_knowledge = init_knowledge(upper_instructions[col], ROWS)
    vertical_list = []
    for horiz_list in img:
        vertical_list.append(horiz_list[col])
    update_linear_bitmap_by_scopes(curr_knowledge, vertical_list) #todo pushing to a priority queue #buggggggggggggggggggggg not in place
print_image(left_instructions, upper_instructions, img)