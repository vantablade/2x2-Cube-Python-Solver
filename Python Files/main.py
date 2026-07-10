from cube import create_solved_cube
from display import display_cube
from moves import *
from analysis import *

cube = create_solved_cube()

cube = most_completed_face(cube)
print(most_completed_face)
