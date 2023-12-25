class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if(arr.size()<3)return false;
        if(arr[0]>arr[1]){
            return false;
        }
        if (arr[arr.size()-1]>arr[arr.size()-2])return false;
        bool isup = true;
        for(int i = 0; i<arr.size()-1; i++){
            if(isup && arr[i]>arr[i+1]){
                isup = false;
            }
            if (!isup && arr[i]<arr[i+1]){
                return false;
            }
            if (arr[i]==arr[i+1]){
                return false;
            }
        }
        return true;
    }
};