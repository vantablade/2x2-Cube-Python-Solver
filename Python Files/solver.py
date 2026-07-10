from analysis import *

def solve(cube):

    face = most_completed_face(cube)

    orient_cube(face)

    while not is_solved(cube):

        case = identify_case(cube)

        algorithm = choose_algorithm(case)

        cube = apply_algorithm(cube, algorithm)

    return cube