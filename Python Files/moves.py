from cube import copy_cube
from cube import create_solved_cube

def rotate_face_clockwise(face):
    return [
        face[2],
        face[0],
        face[3],
        face[1]
    ]

def move_U(cube):

    cube = copy_cube(cube)

    cube["U"] = rotate_face_clockwise(cube["U"])

    f_top = cube["F"][0], cube["F"][1]
    r_top = cube["R"][0], cube["R"][1]
    b_top = cube["B"][0], cube["B"][1]
    l_top = cube["L"][0], cube["L"][1]

    cube["F"][0], cube["F"][1] = r_top
    cube["L"][0], cube["L"][1] = f_top
    cube["B"][0], cube["B"][1] = l_top
    cube["R"][0], cube["R"][1] = b_top

    return cube

def move_U_prime(cube):

    cube = move_U(cube)
    cube = move_U(cube)
    cube = move_U(cube)

    return cube

def move_U2(cube):

    cube = move_U(cube)
    cube = move_U(cube)

    return cube

def move_R(cube):
    cube = copy_cube(cube)
    cube["R"] = rotate_face_clockwise(cube["R"])
    
    u_right = cube['U'][1], cube['U'][3]
    b_left  = cube['B'][0], cube['B'][2]
    d_right = cube['D'][1], cube['D'][3]
    f_right = cube['F'][1], cube['F'][3]
    
    cube['U'][1], cube['U'][3] = f_right
    cube['B'][0], cube['B'][2] = u_right[1], u_right[0]  # Inverts U3 -> B0, U1 -> B2
    cube['D'][1], cube['D'][3] = b_left[1], b_left[0]    # Inverts B2 -> D1, B0 -> D3
    cube['F'][1], cube['F'][3] = d_right
    
    return cube

def move_R_prime(cube):

    cube = move_R(cube)
    cube = move_R(cube)
    cube = move_R(cube)

    return cube

def move_R2(cube):
    
    cube = move_R(cube)
    cube = move_R(cube)

    return cube

def move_F(cube):
    cube = copy_cube(cube)
    cube["F"] = rotate_face_clockwise(cube["F"])

    u_bottom = cube['U'][2], cube['U'][3]
    r_left   = cube['R'][0], cube['R'][2]
    d_top    = cube['D'][0], cube['D'][1]
    l_right  = cube['L'][1], cube['L'][3]

    # Clockwise cycle assignments
    cube['U'][2], cube['U'][3] = l_right[1], l_right[0]  # L3 -> U2, L1 -> U3
    cube['R'][0], cube['R'][2] = u_bottom                # U2 -> R0, U3 -> R2
    cube['D'][0], cube['D'][1] = r_left[1], r_left[0]    # <-- FIX: R2 -> D0, R0 -> D1
    cube['L'][1], cube['L'][3] = d_top                   # D0 -> L1, D1 -> L3

    return cube

def move_F_prime(cube):

    cube = move_F(cube)
    cube = move_F(cube)
    cube = move_F(cube)

    return cube

def move_F2(cube):
    
    cube = move_F(cube)
    cube = move_F(cube)

    return cube

MOVES = {
    "U": move_U,
    "U'": move_U_prime,
    "U2": move_U2,
    "R": move_R,
    "R'": move_R_prime,
    "R2": move_R2,
    "F": move_F,
    "F'": move_F_prime,
    "F2": move_F2
}

def apply_algorithm(cube, algorithm):

    moves = algorithm.split()

    for move in moves:
        cube = MOVES[move](cube)

    return cube