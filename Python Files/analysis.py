from cube import create_solved_cube
cube = create_solved_cube()

def count_face_colours(cube, face):
    count = {}
    for sticker in cube[face]:
        if sticker in count:
            count[sticker] += 1
        else:
            count[sticker] = 1
    return count

def most_completed_face(cube):
    highest_face = None
    best_count = 0
    best_colour = None
    
    for face in cube:
        counts = count_face_colours(cube, face)
        
        if not counts:
            continue
            
        face_best_colour = max(counts, key=counts.get)
        face_max_count = counts[face_best_colour]
        
        if face_max_count > best_count:
            best_count = face_max_count
            highest_face = face
            best_colour = face_best_colour
            
    return highest_face, best_count, best_colour

face, count, colour = most_completed_face(cube)
print(f"Face: {face}, Count: {count}, Colour: {colour}")

def get_face(cube, orientation, face):
    return cube[orientation[face]]

ORIENTATIONS = {
    "D": {
        "U": "U",
        "D": "D",
        "F": "F",
        "B": "B",
        "L": "L",
        "R": "R",
    },

    "F": {
        "U": "B",
        "D": "F",
        "F": "U",
        "B": "D",
        "L": "L",
        "R": "R",
    },

    "U": {
        "U": "D",
        "D": "U",
        "F": "B",
        "B": "F",
        "L": "L",
        "R": "R",
    },

    "B": {
        "U": "F",
        "D": "B",
        "F": "D",
        "B": "U",
        "L": "L",
        "R": "R",
    },

    "L": {
        "U": "R",
        "D": "L",
        "F": "F",
        "B": "B",
        "L": "U",
        "R": "D",
    },
    
    "R": {
        "U": "L",
        "D": "R",
        "F": "F",
        "B": "B",
        "L": "D",
        "R": "U",
    }
}

def orient_to_face(best_face):
    return ORIENTATIONS[best_face].copy()

CORNERS = {
    "UFR": [
        ("U", 3),
        ("F", 1),
        ("R", 0)
    ],
    "UFL": [
        ("U", 2),
        ("F", 0),
        ("L", 1)
    ],
    "UBR": [
        ("U", 1),
        ("B", 0),
        ("R", 1)
    ],
    "UBL": [
        ("U", 0),
        ("B", 1),
        ("L", 0)
    ],
    "DFR": [
        ("D", 1),
        ("F", 3),
        ("R", 2)
    ],
    "DFL": [
        ("D", 0),
        ("F", 2),
        ("L", 3)
    ],
    "DBR": [
        ("D", 3),
        ("B", 2),
        ("R", 3)
    ],
    "DBL": [
        ("D", 2),
        ("B", 3),
        ("L", 2)
    ]
}

def get_corner(cube, orientation, position):
    locations = CORNERS[position]
    corner = {}

    for face, index in locations:
        oriented_face = orientation[face]
        colour = cube[oriented_face][index]
        corner[face] = colour
    
    return corner

def find_corner(cube, orientation, colours):
    target_set = set(colours)

    for position in CORNERS:
        current_corner = get_corner(cube, orientation, position)

        if set(current_corner.values()) == target_set:
            return position
        
    return None