class Solution:
    def inbound(self, nx, ny, x,y):
        return 0 <= nx < x and 0 <= ny < y
    def exist(self, board: List[List[str]], word: str) -> bool:

        
        

        def recc(x, y, now):

            if now == len(word):
                return True

            for i,j in direction:
                nx = x+i
                ny = y+j

                if self.inbound(nx, ny, len(board), len(board[0])) and (nx, ny) not in visited and word[now] == board[nx][ny]:
                    visited.add((nx, ny))
                    if recc(nx, ny, now+1):
                        return True
                    visited.remove((nx, ny))
            return False

        direction = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited = set()
                    now = 1
    
                    visited.add((i, j))
    
                    if recc(i,j,now):
                        return True
        return False
