class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        if (nums[0] + nums[1] + nums[2] >= target) {
            return nums[0] + nums[1] + nums[2];
        }
        if (nums[nums.size() - 1] + nums[nums.size() - 2] + nums[nums.size() - 3] <= target) {
            return nums[nums.size() - 1] + nums[nums.size() - 2] + nums[nums.size() - 3];
        }
        int res = nums[0]+nums[1]+nums[2];
        int minDiff = abs(res-target);


        for (int i = 0; i<nums.size(); i++){
            int left = i + 1;
            int right = nums.size()-1;
            while(left<right){
                int sum = nums[left]+nums[right]+nums[i];
                int diff = abs(sum-target);
                if(diff < minDiff){
                    res = sum;
                    minDiff = abs(res-target);
                }
                if(sum<target){
                    while(left<right && nums[left]==nums[left+1])
                    left++;

                    left++;
                }else{
                    while(left<right && nums[right]==nums[right-1])
                    right--;
                    right--;
                }
            }
        }
        return res;
    }
};