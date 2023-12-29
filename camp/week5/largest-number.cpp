class Solution {
public:
    string largestNumber(vector<int>& n) {
        vector<string> nums;
        for(int i = 0; i<n.size(); i++){
            nums.push_back(to_string(n[i]));
        }
        string ans="";

        sort(nums.begin(), nums.end(),[&](string s, string t){
        return s+t>t+s;
        });
        bool isz = true;
        for(auto i: nums){
            if(i!="0")isz = false;
            ans+=i;
        }
        if(isz){
            ans = "0";
        }
        return ans;
    }

};