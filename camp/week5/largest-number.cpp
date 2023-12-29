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
        if(nums[0]=="0")return "0";
        for(auto i: nums){
            ans+=i;
        }
        return ans;
    }

};