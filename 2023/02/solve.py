def find_possible_games(puzzle_input):
    possible_games = []
    target_cubes = {'red': 12, 'green': 13, 'blue': 14}

    for game in puzzle_input:
        game_id, cubes = game.split(':')
        cubes = cubes.split(';')

        valid_game = True
        for cube_set in cubes:
            colors = cube_set.split(',')
            for color in colors:
                count, color = color.strip().split(' ')
                if int(count) > target_cubes[color]:
                    valid_game = False
                    break
            if not valid_game:
                break

        if valid_game:
            possible_games.append(int(game_id))

    return sum(possible_games)

def toggle_input(use_example_input):
    """
    Toggles between using example input and importing input from a file.

    Args:
        use_example_input (bool): Flag indicating whether to use example input or import from a file.

    Returns:
        None
    """
    if use_example_input:
        puzzle_input = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
    else:
        puzzle_input = import_input_file()

    transformed_input = [transform_input_line(line) for line in puzzle_input]
    result = find_possible_games(transformed_input)
    print("Part 1 of the daily puzzle:")
    print(result)

def import_input_file():
    filepath = '/Users/michiel/SOURCE/CC_AI/AoC/2023/02/input.txt'
    with open(filepath, 'r') as file:
        puzzle_input = file.readlines()
    return [line.strip() for line in puzzle_input]

def transform_input_line(line):
    line = line.replace('Game ', '')
    return line.strip()

toggle_input(False)  # Call the toggle_input function with the desired input option

# Part 2
# Path: 2023/02/solve.py

