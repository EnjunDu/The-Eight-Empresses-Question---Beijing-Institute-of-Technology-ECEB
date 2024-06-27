import pprint

def safe(board,row,column,n): #board:棋盘、row:行、column:列
    #检查同一列是否有皇后
    for i in range(row):
        if board[i][column]==1:
            return False
    #检查对角线有无皇后
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row,-1,-1),range(column,n)):
        if board[i][j] == 1:
            return False
    #如果均没有错误，则返回正确
    return True

def queens(board,row,n,solutions):
    if row==n:
        #当找到解法时，存储在solutions中
        solution =[row[:] for row in board]
        solutions.append(solution)
        return
    for column in range (n):
        if safe(board,row,column,n):
            board[row][column]=1
            #递归使得放完全部八皇后
            queens(board,row+1,n,solutions)
            #回溯清零重新摆放
            board[row][column]=0

def main():
    n=8
    board=[[0]*8 for i in range (0,n)]
    solutions=[]

    queens(board,0,n,solutions)
    for index,solution in enumerate(solutions,start=1):
        print(f"解法{index}:")
        pprint.pprint(solution)

    print("共有{}种摆法".format(len(solutions)))

if __name__=="__main__":
    main()

