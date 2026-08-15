import string

def run(program):
    my_lst = []
    letter_dct = dict.fromkeys(string.ascii_uppercase, 0)
    pc = 0
    labels = {}
    if len(program) == 0:
        return my_lst
    for index, line in enumerate(program):
        if line.endswith(':'):
            labels[line[:-1]] = index


    while pc < len(program):
        task = program[pc]
        parts = task.split(" ")

        cut_lst, letter_dct = commands(letter_dct, task, parts)
        my_lst.extend(cut_lst)

        if parts[0] == 'END':
            break

        elif parts[0] == 'JUMP':
            pc = labels[parts[1]]

        elif parts[0] == 'IF':
            if if_statement(letter_dct, parts):
                pc = labels[parts[5]]
            else:
                pc += 1

        else:
            pc += 1

    return my_lst


def commands(letter_dct, task, parts):
    cut_lst = []
    parts = task.split(" ")

    if parts[0] == 'PRINT':
        if parts[1] in letter_dct:
            cut_lst.append(letter_dct[parts[1]])
        else:
            cut_lst.append(int(parts[1]))
        
    elif parts[0] == 'MOV':
        if parts[2] in letter_dct:
            letter_dct[parts[1]] = letter_dct[parts[2]]
        else:
            letter_dct[parts[1]] = int(parts[2])
    
    elif parts[0] == "ADD":
        if parts[2] in letter_dct:
                letter_dct[parts[1]] += letter_dct[parts[2]]
        else:
            letter_dct[parts[1]] += int(parts[2])
    
    elif parts[0] == "SUB":
        if parts[2] in letter_dct:
            letter_dct[parts[1]] -= letter_dct[parts[2]]
        else:
            letter_dct[parts[1]] -= int(parts[2])
    
    elif parts[0] == "MUL":
        if parts[2] in letter_dct:
            letter_dct[parts[1]] *= letter_dct[parts[2]]
        else:
            letter_dct[parts[1]] *= int(parts[2])
    
    return cut_lst, letter_dct


def if_statement(letter_dct, parts):
    variable1 = letter_dct[parts[1]]
    if parts[3] in letter_dct:
        variable2 = letter_dct[parts[3]]
    else:
        variable2 = int(parts[3])

    if parts[2] == '==':
        return variable1 == variable2
    elif parts[2] == '>':
        return variable1 > variable2
    elif parts[2] == '<':
        return variable1 < variable2
    elif parts[2] == '>=':
        return variable1 >= variable2
    elif parts[2] == '<=':
        return variable1 <= variable2
    elif parts[2] == '!=':
        return variable1 != variable2