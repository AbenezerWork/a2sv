class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_map<int, int> m;
        int sum=0;
        int prev=0;
        for(int j = 0 ; j< nums.size(); j++){
            int i = nums[j];
            if(!m[i]){
                m[i] = prev +1;
                prev = m[i];
                // cout<<m[i]<<",";
                sum+=m[i];
                // cout<<sum<<endl;
            }else{
                sum+=m[i];
            }

        }
        return sum-nums.size();
    }
};