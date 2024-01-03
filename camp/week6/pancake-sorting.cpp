class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        int mi = -1, m = 0;
        vector<int> ans;
        for(int i = 0;  i< arr.size(); i++){
            mi = -1;m= 0;
            for(int j = 0; j<arr.size()-i; j++){
                if(arr[j]>m){
                    //cout<<"hello"<<endl;
                    m = arr[j];
                    mi = j;
                }
            }
            //cout << mi <<endl;
            ans.push_back(mi+1);
            ans.push_back(arr.size()-i);
            reverse(arr.begin(), arr.begin()+mi+1);
            reverse(arr.begin(), arr.end()-i);
        }
        return ans;
    }
};