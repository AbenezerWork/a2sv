class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>sor(nums.size());
        for(int i = 0; i< nums.size(); i++){
            sor[i]=nums[i];
        }
        sort(sor.begin(), sor.end());
        unordered_map<int,int> m;
        vector<int> ans(nums.size());
        for(int i = 0; i<nums.size(); i++){
            if (!m[sor[i]]){
                m[sor[i]]=i+1;
            }
        }
        for(int i = 0; i<nums.size(); i++){
            ans[i]=m[nums[i]]-1;
        }
        return ans;
    }
};