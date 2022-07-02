# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = []
    stack = []

    for j in moves:
        for i in range(len(board)):
            if board[i][j - 1] > 0:
                stack.append(board[i][j - 1])
                board[i][j - 1] = 0
                if stack[-1:] == stack[-2:-1]:
                    answer += stack[-1:]
                    stack = stack[:-2]
                break

    return len(answer) * 2
