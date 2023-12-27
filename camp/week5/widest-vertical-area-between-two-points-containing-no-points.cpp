class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(),points.end(), [&](vector<int>& x ,vector<int>& y){
            return x[0]<y[0];
        });
        int mx = 0;

        for(int i = 0; i<points.size()-1; i++){
            mx = max(mx, points[i+1][0]-points[i][0]);
        }
        return mx;

    }
};