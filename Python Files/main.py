from cube import *
from display import display_cube
from moves import *
from analysis import *

cube = create_solved_cube()
cube = apply_algorithm(cube, "R2 U2 F R F2 R2 U R U'")

for face in cube: 
    print(face, cube[face])