if __name__ == '__main__':
    n = int(input())
    array = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        row = input()
        for j in range(n):
            array[i][j]=row[j]
    
    def calc_pos(pos1,pos2):
        x1,y1 = pos1
        x2,y2 = pos2
        if x1==x2:
            max_val1 = count(array[x1])
            row1 = []
            for i in range(n):
                row1.append(array[i][y1])
            max_val2 = count(row1)
            row2 = []
            for i in range(n):
                row2.append(array[i][y2])
            max_val3 = count(row2)
            return max([max_val1,max_val2,max_val3])
        else:
            row1 = []
            for i in range(n):
                row1.append(array[i][y1])
            max_val1 = count(row1)
            max_val2 = count(array[x1])
            max_val3 = count(array[x2])
            return max([max_val1,max_val2,max_val3])
        
    def count(line):
        before=''
        num_c = 1
        num_cs = []
        for i in range(n):
            if (line[i]=='C')&(before=='C'):
                num_c+=1
            else:
                num_cs.append(num_c)
                num_c = 1
            before = line[i]
        num_y = 1
        num_ys = []
        for i in range(n):
            if (line[i]=='Y')&(before=='Y'):
                num_y+=1
            else:
                num_ys.append(num_y)
                num_y = 1
            before = line[i]
        num_z = 1
        num_zs = []
        for i in range(n):
            if (line[i]=='Z')&(before=='Z'):
                num_z+=1
            else:
                num_zs.append(num_z)
                num_z = 1
            before = line[i]
        num_p = 1
        num_ps = []
        for i in range(n):
            if (line[i]=='P')&(before=='P'):
                num_p+=1
            else:
                num_ps.append(num_p)
                num_p = 1
            before = line[i]

        return max([max(num_cs),max(num_ps),max(num_ys),max(num_zs)])

    index_x = 0
    max_result = 0
    while index_x<n:
        index_y=0
        while index_y<n:
            #위
            if index_y-1 >= 0:
                if array[index_x][index_y-1]!=array[index_x][index_y]:
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x][index_y-1]
                    array[index_x][index_y-1] = temp
                    result = calc_pos((index_x,index_y),(index_x,index_y-1))
                    if result > max_result:
                        max_result = result
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x][index_y-1]
                    array[index_x][index_y-1] = temp

            #아래
            if index_y+1 < n:
                if array[index_x][index_y+1]!=array[index_x][index_y]:
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x][index_y+1]
                    array[index_x][index_y+1] = temp
                    result = calc_pos((index_x,index_y),(index_x,index_y+1))
                    if result > max_result:
                        max_result = result
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x][index_y+1]
                    array[index_x][index_y+1] = temp  
            #좌
            if index_x-1 >= 0:
                if array[index_x-1][index_y]!=array[index_x][index_y]:
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x-1][index_y]
                    array[index_x-1][index_y] = temp
                    result = calc_pos((index_x,index_y),(index_x-1,index_y))
                    if result > max_result:
                        max_result = result
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x-1][index_y]
                    array[index_x-1][index_y] = temp
            #우
            if index_x+1 < n:
                if array[index_x+1][index_y]!=array[index_x][index_y]:
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x+1][index_y]
                    array[index_x+1][index_y] = temp
                    result = calc_pos((index_x,index_y),(index_x+1,index_y))
                    if result > max_result:
                        max_result = result
                    temp = array[index_x][index_y]
                    array[index_x][index_y] = array[index_x+1][index_y]
                    array[index_x+1][index_y] = temp
            index_y+=1
        index_x+=1
    print(max_result)

