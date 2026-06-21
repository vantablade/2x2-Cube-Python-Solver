import copy

def copy_cube(cube):
    return copy.deepcopy(cube)

def create_solved_cube():
    return {
        "U": ["W", "W", "W", "W"],
        "D": ["Y", "Y", "Y", "Y"],
        "F": ["G", "G", "G", "G"],
        "B": ["B", "B", "B", "B"],
        "L": ["O", "O", "O", "O"],
        "R": ["R", "R", "R", "R"]
    }

def get_cube_input():
    cube = {}

    faces = ['U', 'D', 'F', 'B', 'L', 'R']

    for face in faces:
        while True:
            colours = input(f'Enter the 4 colours for {face} from top left corner to bottom right (seperated by spaces): ').upper().split()

            if len(colours) == 4:
                cube[face] = colours
                break
            else:
                print('Please enter exactly 4 colours')

    return cube

def is_solved(cube):

    for face in cube:

        stickers = cube[face]

        if len(set(stickers)) != 1:
            return False

    return True