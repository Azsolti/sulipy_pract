import random

arr = "ABCDEFGHIJKLMNOPQRSTUVWXY"
arr_2 = "ABHDEFGMIJKLRNOPQWSTUVCXY"
matrix = [[arr[i*5 + j] for j in range(5)] for i in range(5)]
matrix_2 = [[arr_2[i*5 + j] for j in range(5)] for i in range(5)]

def moves():
    indexes = {}
    indexes_2 = {}
    for i, row in enumerate(matrix, start=0):
        for ii, char in enumerate(row,start=0): 
            indexes[char] = i,ii
            
    for i, row in enumerate(matrix_2, start=0):
        for ii, char in enumerate(row,start=0): 
            indexes_2[char] = i,ii

    for k,v in indexes.items():
        if indexes_2[k] == v:
            pass
        
        elif indexes_2[k][0] == v[0]:
                print("This should move left or right")
        
        else:
            print("This should move towards top or bottom")
            print(indexes[k])
            print(indexes_2[k])
            print("---------------")
            
      
moves()
