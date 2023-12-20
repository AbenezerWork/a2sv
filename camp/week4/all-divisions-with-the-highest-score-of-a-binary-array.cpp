class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        int right = 0;
        for (int i = 0; i<nums.size(); i++){
            if (nums[i]){
                right++;
            }
        }
        vector<int> ans(nums.size()+1);
        ans[0]=right;
        int maxVal=right;
        int left =0;
        for ( int i = 0; i<nums.size(); i++){
            if(nums[i]){
                right--;
            }else{
                left++;
            }
            ans[i+1]=left+right;
            maxVal = max(maxVal,left+right);
        }
        vector<int> res;
        for (int i = 0; i<ans.size(); i++){
            if (ans[i]==maxVal){
                res.push_back(i);
            }
        }
        return res;
    }
};