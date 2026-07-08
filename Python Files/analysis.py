from cube import create_solved_cube
cube = create_solved_cube()

def count_face_colours(cube, face):
    for face in cube:
        count = {}
        for sticker in cube[face]:
            if sticker in count:
                count[sticker] += 1
            else:
                count[sticker] = 1
        return count

def most_completed_face(cube):
    highest_face = None
    highest_count = 0
    best_colour = None
    
    for face in cube:
        counts = count_face_colours(cube, face)
        
        if not counts:
            continue
            
        face_best_colour = max(counts, key=counts.get)
        face_max_count = counts[face_best_colour]
        
        if face_max_count > highest_count:
            highest_count = face_max_count
            highest_face = face
            best_colour = face_best_colour
            
    return highest_face, highest_count, best_colour

face, count, colour = most_completed_face(cube)
print(f"Face: {face}, Count: {count}, Colour: {colour}")