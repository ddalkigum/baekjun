board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves =[1,5,3,5,1,2,1,4]	


def solution(board, moves):
    bascket = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]>0:     # 인형이 존재하는지 확인
                bascket.append(board[j][i-1])
                board[j][i-1]=0     # 뽑은후에 인형값을 0으로 줌    
                print(bascket)
                break               # 그 뒤에는 안봐도 되니까 break로 for문을 탈출해줌
        if len(bascket)>1:
            if bascket[-1] == bascket[-2]:
                del bascket[-2]
                del bascket[-1]
                answer +=2
    return answer

answer = solution(board, moves)
