numRows = int(input('Enter a number: '))


if numRows == 0:
    triangle = [[]]
    

elif numRows == 1:
    triangle = [[1]]

elif numRows == 2:
    triangle = [[1],[1,1]]
    
else:
    row = 2
    triangle = [[1],[1,1]]
    while row < numRows:
        row_list = [1]
        for e in range(1,row):
            row_list.insert(e,triangle[row-1][e-1]+triangle[row-1][e])
        row_list.append(1)
        triangle.append(row_list)   
        row += 1
        
print(*triangle,sep = ','+'\n')