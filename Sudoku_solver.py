
def solver(bod):

    # boolean function. return true if solved.
    toFind = find_empty_location(bod)
    # return true if all the position is filled. (without zero)
    if toFind == (-1,-1):
        return True

    for i in range(1,10):
        if isValid(bod, toFind, i):
            bod[toFind[0]][toFind[1]] = i
            if solver(bod):
                return True
            bod[toFind[0]][toFind[1]] = 0

    return False

def print_board(bod):

    for i in range(len(bod)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - -")
        
        for j in range (len(bod[0])):
            if j % 3 == 0 and j != 0:
                print (" | ", end = "")

            if j == 8:
                print(str(bod[i][j]))
            else:
                print(str(bod[i][j]) + " ", end="")
# check row 
def isValid_row(bod,pos,n):
    for col in range(9):
        if bod[pos[0]][col] == n:
            return False
    return True

# check col
def isValid_col(bod,pos,n):
    for row in range(9):
        if bod[row][pos[1]] == n:
            return False
    return True

# check for the unit:

def isValid_unit(bod, pos, n):
    # check unit

    unit_x = pos[1] // 3
    unit_y = pos[0] // 3
        
    for i in range(unit_y*3,unit_y*3 + 3):
        for j in range (unit_x*3,unit_x*3 + 3):
            if bod[i][j] == n:
                return False
    return True    

def isValid(bod,pos,n):
     return not (isValid_col(bod,pos,n) or isValid_row(bod,pos,n) or isValid_unit(bod,pos,n))


def find_empty_location(bod):
    for row in range(9):
        for col in range(9):
            if bod[row][col] == 0:
                return (row, col)
    return (-1,-1)



if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid =[[0 for x in range(9)]for y in range(9)] 
      
    # assigning values to the grid 
    board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
    # if success print the grid 
    if(solver(board)): 
        print_board(board) 
    else: 
        print("No solution exists")
    


                
