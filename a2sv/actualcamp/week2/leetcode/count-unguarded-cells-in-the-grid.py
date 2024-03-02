class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0]*n for i in range(m)]
        for i in range(len(walls)):
            mat[walls[i][0]][walls[i][1]]="W"
        
        for i in range(len(guards)):
            x, y = guards[i]
            mat[x][y]="G"
        for i in range((len(guards))):

            x, y = guards[i]
            x+=1
            while x<m and mat[x][y]!="G" and mat[x][y] != "W":
                mat[x][y]="x"
                x+=1

            x, y = guards[i]
            x-=1
            while x>=0 and mat[x][y] != "W" and mat[x][y]!='G':
                mat[x][y]="x"
                x-=1

            x, y = guards[i]
            y+=1
            while y<n and mat[x][y] != "W" and mat[x][y] != 'G':
                mat[x][y]="x"
                y+=1

            x, y = guards[i]
            y-=1
            while y>=0 and mat[x][y] != "W" and mat[x][y]!="G":
                mat[x][y]="x"
                y-=1
        ans = 0
        for i in range(m):
            ans+=mat[i].count(0)
        return ans



