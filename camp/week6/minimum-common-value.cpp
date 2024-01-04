class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int j = 0,i=0;
        while(i<nums1.size() && nums2.size()>j){
            while(j<nums2.size() && nums1[i]>nums2[j]){
            j++;
        }
        if(j>=nums2.size())return -1;
        if(nums1[i]==nums2[j]){
            return nums1[i];
        }
        while(i<nums1.size() && nums1[i]<nums2[j]){
            i++;
        }
        if(i>=nums1.size())return -1;
        if(nums1[i]==nums2[j]){
            return nums1[i];
        }
        }
        
        return -1;
    }
};