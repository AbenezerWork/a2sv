class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        vector<int> arr(flips.size());
        int count = 0;
        int mx = 0;
        int last = 0;
        for(int i = 0; i < flips.size(); i++){
            arr[flips[i]-1]=1;
            mx  = max(flips[i],mx);


            for(int j = last; j<flips.size(); j++){
                if(!arr[j])break;
                if(arr[j]){

                    last=j;
                }
                if(arr[j] && j==mx-1){
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};