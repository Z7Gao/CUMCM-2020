adjMisson1 = [[0,6,0,0,0,0,0,0,3],[0,0,2,0,0,0,0,0,3],\
              [0,0,0,2,0,0,0,0,0],[0,0,0,0,2,0,0,0,3],\
              [0,0,0,0,0,2,0,0,0],[0,0,0,0,0,0,2,0,3],\
              [0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,3]]
adjMisson2 = []

for i in range(16):
    adjChild = []
    for j in range(16):
        adjChild.append(0)
    adjMisson2.append(adjChild)

adjMisson2[0][1] = 7
adjMisson2[1][2] = 1
adjMisson2[2][3] = 1
adjMisson2[2][9] = 2
adjMisson2[2][15] = 3
adjMisson2[3][4] = 1
adjMisson2[4][5] = 1
adjMisson2[4][9] = 2
adjMisson2[4][15] = 3
adjMisson2[5][6] = 1
adjMisson2[6][7] = 1
adjMisson2[6][9] = 2
adjMisson2[6][15] = 3
adjMisson2[7][8] = 1
adjMisson2[8][9] = 2
adjMisson2[8][15] = 3
adjMisson2[9][10] = 2
adjMisson2[9][15] = 2
adjMisson2[10][11] = 1
adjMisson2[10][15] = 2
adjMisson2[11][12] = 1
adjMisson2[11][15] = 2
adjMisson2[12][13] = 1
adjMisson2[12][15] = 2
adjMisson2[13][14] = 1
adjMisson2[13][15] = 2
adjMisson2[14][15] = 2

def findAllPath(adjMatrix, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for i in range(end + 1):
        if (adjMatrix[start][i] > 0 and i not in path):
            newPaths = findAllPath(adjMatrix, i, end, path)
            for newPath in newPaths:
                paths.append(newPath)

    return paths

print(findAllPath(adjMisson1, 0, 8))
print(findAllPath(adjMisson2, 0, 15))
print(adjMisson1)
print(adjMisson2)