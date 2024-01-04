class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        int size=nums.size();
        for(int i=0;i<size-2;++i){
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left=i+1;
            int right=size-1;
            while(left<right){
                int sum=nums[left]+nums[right]+nums[i];
                if(sum==0){
                    res.push_back({nums[right],nums[left],nums[i]});
                    while(left<right && nums[left]==nums[left+1]){
                        left++;
                    }
                    while(left<right && nums[right]==nums[right-1]){
                        right--;
                    }
                    left++;
                    right--;
                }else if(sum>0){
                    right--;
                }else{
                    left++;
                }
            }
        }
        
        return res;
    }
};