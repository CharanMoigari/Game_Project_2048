import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat
def addnew2(grid):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while grid[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    grid[r][c]=2
    return grid
def compress(grid):
    newmat=[]
    for i in range(4):
        newmat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if grid[i][j]!=0:
                newmat[i][pos]=grid[i][j]
                if j!=pos:
                    change=True
                pos+=1
    return newmat

    
def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                grid[i][j]=grid[i][j]*2
                grid[i][j+1]=0
    return grid
        
def reverse(grid):
    newmat=[]
    for i in range(4):
        newmat.append([])
        for j in range(4):
            newmat[i].append(grid[i][4-j-1])
    return newmat
            
def transpose(grid):
    newmat=[]
    for i in range(4):
        newmat.append([])
        for j in range(4):
            newmat[i].append(grid[j][i])
    return newmat
def move_up(grid):
    newgrid=transpose(grid)
    newgrid=compress(newgrid)
    newgrid=merge(newgrid)
    newgrid=compress(newgrid)
    newgrid=transpose(newgrid)
    return newgrid
   
    
    #Implement This Function
    pass

def move_down(grid):
    newgrid=transpose(grid)
    newgrid=reverse(newgrid)
    newgrid=compress(newgrid)
    newgrid=merge(newgrid)
    newgrid=compress(newgrid)
    newgrid=reverse(newgrid)
    newgrid=transpose(newgrid)
    return newgrid

    
    #Implement This Function
    pass

def move_right(grid):
    newgrid=reverse(grid)
    newgrid=compress(newgrid)
    newgrid=merge(newgrid)
    newgrid=compress(newgrid)
    newgrid=reverse(newgrid)
    return newgrid

    #Implement This Function
    pass

def move_left(grid):
    newgrid=compress(grid)
    newgrid=merge(newgrid)
    newgrid=compress(newgrid)
    return newgrid
    
    #Implement This Function
    pass


mat = start_game()
mat[1][3] = 2
mat[2][2] = 2
mat[3][0] = 4
mat[3][1] = 8
mat[2][1] = 4
inputs = [int(ele) for ele in input().split()]
for ele in inputs:
    if ele == 1:
        mat = move_up(mat)
    elif ele == 2:
        mat = move_down(mat)
    elif ele == 3:
        mat = move_left(mat)
    else:
        mat = move_right(mat)
    print(mat)