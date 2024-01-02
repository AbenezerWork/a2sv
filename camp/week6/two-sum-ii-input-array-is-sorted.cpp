class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0, j= nums.size()-1;

        while (i<j){
            if(nums[i]+nums[j]>target){
                j--;
            }else
            if(nums[i]+nums[j]<target){
                i++;
            }else{
                vector<int> v;
                v.push_back(i+1);
                v.push_back(j+1);
                return v;
            }
        }
        return vector(1,1);
    }
};