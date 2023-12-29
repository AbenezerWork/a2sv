class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        for(int i = 0; i<9; i++){
            set<char> s;
            set<char> p;
            for(int j = 0; j<9; j++){
                if ( s.count(board[i][j])){
                    return false;
                }
                if(board[i][j]!='.')
                    s.insert(board[i][j]);
                if (p.count(board[j][i])){
                    return false;
                }
                if(board[j][i]!='.')
                    p.insert(board[j][i]);
            }
        }
        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                set<int> s;
                for(int k = 0; k<3; k++){
                    for(int l = 0; l<3; l++){
                        char c = board[i*3+k][j*3+l];
                        if(s.count(c)){
                            return false;
                        }
                    if(c!='.')
                        s.insert(c);
                    }
                }
            }
        }
        return true;
    }
};
/*
[["5","3",".", ".","7",".", ".",".","."]
,["6",".",".", "1","9","5", ".",".","."]
,[".","9","8", ".",".",".", ".","6","."]

,["8",".",".", ".","6",".", ".",".","3"]
,["4",".",".", "8",".","3", ".",".","1"]
,["7",".",".", ".","2",".", ".",".","6"]

,[".","6",".", ".",".",".", "2","8","."]
,[".",".",".", "4","1","9", ".",".","5"]
,[".",".",".", ".","8",".", ".","7","9"]]*/