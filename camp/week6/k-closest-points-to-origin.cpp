class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), [&](vector<int>& x, vector<int>& y){
            return sqrt(pow(x[0],2)+pow(x[1],2))<sqrt(pow(y[0],2)+pow(y[1],2));
        });
        vector<vector<int>> ans;
        for(int i = 0; i< k; i++){
            ans.push_back(points[i]);
        }
        return ans;
    }
};