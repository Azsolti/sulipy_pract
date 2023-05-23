import random

arr = "ABCDEFGHIJKLMNOPQRSTUVWXY"
arr_2 = "DEABCFGHIJKLMNOPQRSTUVWXY"
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
            
        else:
            res = indexes_2[k][1] - v[1]
            print(res)
            print("---------------")
            print(indexes[k])
            print("---------------")
            print(indexes_2[k])
            
