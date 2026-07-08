from cube import create_solved_cube
from display import display_cube
from moves import *

cube = create_solved_cube()

cube = apply_algorithm(cube, "R U R' U'")
display_cube(cube)
