def is_face_on_photo(photo):
    rows = len(photo)
    cols = len(photo[0])

    for r in range(rows - 1):
        for c in range(cols - 1):
            square = [
                photo[r][c], photo[r][c+1],
                photo[r+1][c], photo[r+1][c+1]
            ]
            if sorted(square) == sorted(["f", "a", "c", "e"]):
                return True

    return False

print(is_face_on_photo([['f','a'], ['c','e']]))     # True
print(is_face_on_photo([['f','a'], ['c','x']]))     # False
print(is_face_on_photo([['e','c','x'], ['a','x','x'], ['f','x','x']]))  # True

