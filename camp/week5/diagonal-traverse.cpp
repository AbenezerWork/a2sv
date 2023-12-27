class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int i = 0, j = 0,k=1,n=mat.size(),m=mat[0].size();
        map<int,vector<int>> el;
        vector<int> ans;
        for (int i = 0; i<n; i++){
            for (int j = 0; j<m; j++){
                el[j+i].push_back(mat[i][j]);
            }
        }
        for(auto& it: el){
            if(it.first%2==0){
                for(int i = it.second.size()-1; i>=0; i--){
                    ans.push_back(it.second[i]);
                    cout<<it.second[i]<<endl;
                }
            }else{
                for (int i = 0; i<it.second.size(); i++){   
                    ans.push_back(it.second[i]);
                    cout<<it.second[i]<<endl;
                }
            }
        }
        return ans;
    }
};