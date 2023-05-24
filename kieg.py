arr = "ABCDEFGHIJKLMNOPQRSTUVWXY"
arr_2 = "CWMFJORDBANKGLYPHSVEXTQUI"
matrix = [[arr[i*5 + j] for j in range(5)] for i in range(5)]
matrix_2 = [[arr_2[i*5 + j] for j in range(5)] for i in range(5)]

def moves():
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
            print(indexes_2[k], indexes[k])
            
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

                 
moves()
