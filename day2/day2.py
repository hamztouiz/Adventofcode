

balls_restriction: dict = {'red' : 12 , 'green' : 13, 'blue': 14 }

def game_is_possible(line: str) -> bool:
    sets: list = str(line).split(':')[1].split(';')
    for set in sets:
      for balls in set.split(','):
        if int(balls.split(' ')[1]) > balls_restriction[balls.split(' ')[2]] :
            return 0           
    return 1


with open('input.txt') as input_file:
    sum: int = 0
    for i,line in enumerate(input_file):
            sum += (i+1)*game_is_possible(line.replace('\n',''))
    print(sum)
