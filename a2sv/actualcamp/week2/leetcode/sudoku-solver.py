class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row = defaultdict(set)
        self.col = defaultdict(set)
        self.box = defaultdict(set)
        for x in range(9):
            for y in range(9):
                self.row[y].add(board[x][y])
                self.col[x].add(board[x][y])
                self.box[((x)//3)*3 + (y//3)].add(board[x][y])

        def checker(x,y):
            #checking for row
            if board[x][y] in self.row[y]:
                return False
                    
            
            col = set()
            if board[x][y] in self.col[x]:
                return False
            
            if board[x][y] in self.box[((x)//3)*3 + y//3]:
                return False
            return True

        def recc(x,y):
            #print(x,y)
            if x == 9:
                #print(board,self.box)
                return True
            
            if board[x][y]!='.':
                if y == 8:
                    return recc(x+1,0)
                else:
                    return recc(x, y+1)

            #print(((x)//3)*3+(y//3))
            for i in range(1,10):
                board[x][y] = str(i)
                if not checker(x,y):
                    board[x][y] = '.'
                    continue

                else:
                    self.row[y].add(str(i))
                    self.col[x].add(str(i))
                    self.box[((x)//3)*3 + (y//3)].add(str(i))
                    if y == 8:
                        res = recc(x+1,0)
                    else:
                        res = recc(x, y+1)
                if not res:
                    self.row[y].remove(board[x][y])
                    self.col[x].remove(board[x][y])
                    self.box[((x)//3)*3+(y//3)].remove(board[x][y])
                    board[x][y] = '.'
                else:
                    return True
            return False
        recc(0,0)


        

                
        