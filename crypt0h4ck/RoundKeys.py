state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j]^=k[i][j]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    array = []
    for x in matrix:
        array += x
    return bytes(array)

matrix = add_round_key(state, round_key)

print(matrix2bytes(matrix))

# This challenge requires to implement a function that XOR 2 matrix 
# $ python3 RoundKeys.py 
# b'crypto{r0undk3y}'