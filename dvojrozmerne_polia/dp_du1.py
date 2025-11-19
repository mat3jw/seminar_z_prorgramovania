def get_min_max(table):
    mn = float("inf")
    mx = float("-inf")
    for row in table:
        for x in row:
            if x < mn:
                mn = x
            if x > mx:
                mx = x
    return (mn, mx)

def swap_rows(table, row1, row2):
    table[row1], table[row2] = table[row2], table[row1]

def swap_columns(table, col1, col2):
    for row in table:
        row[col1], row[col2] = row[col2], row[col1]

def follow_snail(table):
    result = []
    n = len(table)
    m = len(table[0])

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    while top <= bottom and left <= right:

        # doprava
        for col in range(left, right + 1):
            result.append(table[top][col])
        top += 1

        # dole
        for row in range(top, bottom + 1):
            result.append(table[row][right])
        right -= 1

        if top <= bottom:
            # doľava
            for col in range(right, left - 1, -1):
                result.append(table[bottom][col])
            bottom -= 1

        if left <= right:
            # hore
            for row in range(bottom, top - 1, -1):
                result.append(table[row][left])
            left += 1

    return result