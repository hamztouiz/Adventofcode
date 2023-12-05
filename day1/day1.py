
digits_as_letters= [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_digit(line: str, inverse: bool) ->  int:

    if line[0+(inverse*2):3+(inverse*2)] in digits_as_letters:
        return digits_as_letters.index(line[0+(inverse*2):3+(inverse*2)]) + 1
    elif line[0+(inverse*1):4+(inverse*1)] in digits_as_letters:
        return digits_as_letters.index(line[0+(inverse*1):4+(inverse*1)]) + 1
    elif line[0:5] in digits_as_letters:
        return digits_as_letters.index(line[0:5]) + 1
    else:
        return 0


def find_digits(line: str, digit1: int, digit2: int) -> int:
    # retur a number formed by the first and last of the string
    if digit1 == 0:
        if line[0].isdigit() == False:
            digit1 = find_digit(line[0:5],False)
            line = line[1:]
        else:
            digit1 = int(line[0])

    if digit2 == 0:
        if line[-1].isdigit() == False:
            digit2 = find_digit(line[-5:], True)
            line = line[:-1]
        else:
            digit2 = int(line[-1])
        
    if digit1 != 0 and digit2 != 0:
        return int(digit1)*10 + int(digit2)
    else:
         return find_digits(line, digit1, digit2)


with open('input_day_one.txt') as input_file:
    sum: int = 0
    for line in input_file:
            sum += find_digits(line[:-1],0,0)
    print(sum)


