import math
arr = "ABCD"
arr_2 = "ABMD"
sqr = math.sqrt(len(arr))
sqr = int(sqr)

matrix = [[arr[i*sqr + j] for j in range(sqr)] for i in range(sqr)]
matrix_2 = [[arr_2[i*sqr + j] for j in range(sqr)] for i in range(sqr)]

def calc_moves():
    moves = []
    indexes = {}
    indexes_2 = {}
    for i, row in enumerate(matrix, start=0):
        for ii, char in enumerate(row,start=0): 
            indexes[char] = i,ii
            
    for i, row in enumerate(matrix_2, start=0):
        for ii, char in enumerate(row,start=0): 
            indexes_2[char] = i,ii
    
    counter = 0
  
    for k,v in indexes.items():
     
        if indexes_2[k] == v:
            
            pass

        else:
           
            if counter == 1:

                diff_col = indexes[k][0] - indexes_2[k][0]
                diff_row = indexes[k][1] - indexes_2[k][1]
                abs_col = abs(diff_col)
                abs_row = abs(diff_row)

                
                if diff_col < 0:
                    
                    for n in range(abs_col):
                        moves.append(f"U{indexes[k][1]}")
                if diff_row < 0:
                    
                    for n in range(abs_row):
                        moves.append(f"L{indexes[k][0]}")
                if diff_col > 0:
                    
                    for n in range(abs_col):
                        moves.append(f"D{indexes[k][1]}")
                if diff_row > 0:
                    
                    for n in range(abs_row):
                        moves.append(f"R{indexes[k][0]}")
            counter += 1
    return moves
    
def final_moves(calc_moves, matrix, matrix_2):
    
    temp = []
    for item in calc_moves:
        
        direction = item[0]
        index = item[1]

        def move_up(matrix_2):
            
            for col in matrix_2:
                print("Column:", col)
                print("Need to remove : ", col[int(index)])
                
                
                
        if direction == "U":
           print("UPPPPP")
           
           move_up(matrix_2)
                
                
    
final_moves(calc_moves(), matrix, matrix_2)

                 
moves()
