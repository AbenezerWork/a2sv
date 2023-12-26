class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> order;
        for(int i = 0; i<arr2.size(); i++){
            order[arr2[i]]=i+1;
        }
        sort(arr1.begin(), arr1.end(), [&](int x, int y){
                if (order[x]==0){
                    order[x]=1001+x;
                }
                if (order[y]==0){
                    order[y]=1001+y;
                }
            return order[x]<order[y];
        });
        return arr1;
    }
};