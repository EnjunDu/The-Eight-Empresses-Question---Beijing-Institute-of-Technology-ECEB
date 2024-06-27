import pprint

def safe(board, row, column, n):
    for i in range(row):
        if board[i] == column or  board[i] - i == column - row or board[i] + i == column + row:
            return False
    return True

def queens(n):
    solutions = []
    stack = [(0, [])]

    while stack:
        row, board = stack.pop()
        if row == n:
            solutions.append([0]*n)
            for i in range(n):
                solutions[-1][i]=[0]*n
                solutions[-1][i][board[i]]=1
        else:
            for col in range(n):
                if safe(board, row, col, n):
                    stack.append((row + 1, board + [col]))

    return solutions

def main():
    n = 8
    solutions = queens(n)
    for idx, solution in enumerate(solutions, start=1):
        print(f"解法 {idx}:")
        pprint.pprint(solution)
    print("共有{}钟解法".format(len(solutions)))


if __name__ == "__main__":
    main()