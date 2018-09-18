def initmatrix():
    aa=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    return aa
def isGameOver(aa=[
    [0,0,0],
    [0,0,0],
    [0,0,0]]):
    if aa[0][0]==aa[0][1]==aa[0][2]!=0:return 1
    if aa[1][0]==aa[1][1]==aa[1][2]!=0:return 1
    if aa[2][0]==aa[2][1]==aa[2][2]!=0:return 1
    if aa[0][0]==aa[1][0]==aa[2][0]!=0:return 1    
    if aa[0][1]==aa[1][1]==aa[2][1]!=0:return 1    
    if aa[0][2]==aa[1][2]==aa[2][2]!=0:return 1    
    if aa[0][0]==aa[1][1]==aa[2][2]!=0:return 1    
    if aa[0][2]==aa[1][1]==aa[2][0]!=0:return 1
    for yy in range(0,3):
        for xx in range(0,3):
            if aa[yy][xx]==0:return 0
    return 2
