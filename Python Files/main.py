from cube import create_solved_cube
from display import display_cube
from moves import *
from analysis import *

cube = create_solved_cube()

orientation = ORIENTATIONS["F"]

print(get_corner(cube, orientation, "DFR"))