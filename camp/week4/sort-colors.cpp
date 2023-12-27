class Solution {
public:
    void sortColors(vector<int>& nums) {
        int arr[3]= {0,0,0};
        for(auto i : nums){
            arr[i]++;
        }
        int s = 0;
        for(int i = 0; i<3; i++){
            while(arr[i] && s<nums.size()){
                nums[s]=i;
                arr[i]--;
                s++;
            }
        }
    }
};