class Solution {
public:
    int minProcessingTime(vector<int>& pt, vector<int>& tasks) {
        sort(pt.begin(),pt.end());
        sort(tasks.begin(),tasks.end(),greater<>());
        int mx = 0;
        cout<<pt.size()<<", "<<tasks.size()<<endl;
        for(int i = 0; i<pt.size(); i++){
            mx = max(pt[i]+tasks[i*4+1],max(pt[i]+tasks[i*4+2],max(pt[i]+tasks[i*4+3],max(pt[i]+tasks[i*4],mx))));
        }
        return mx;
    }
};