class Solution {
public:
    bool compare(string s, string t){
        int ns = s.size(),nt = t.size();
        int j = 0,i=0,p =0; 
        while(p<100){
            if(j == nt && i == ns){
                return false;
            }
            if(j==nt){
                j = 0;
            }
            if(i == ns){
                i = 0;
            }
            if(t[j]>s[i]){
                return true;
            }
            if(s[i]>t[j]){
                return false;
            }
            p++;j++;i++;
        }
        return false;
    }
    string ans="";
    string largestNumber(vector<int>& n) {
        vector<string> nums;
        for(int i = 0; i<n.size(); i++){
            nums.push_back(to_string(n[i]));
        }
        for(int i = 0; i< nums.size(); i++){
            for(int j = 0; j<nums.size()-i-1; j++){
                if(compare(nums[j],nums[j+1])){
                    swap(nums[j],nums[j+1]);
                }
            }
        }
        bool isz = true;
    for(int i = 0; i<nums.size(); i++){
        if(nums[i]!="0"){
            isz = false;
        }
        ans+= nums[i];
    }
    if(isz){
        ans = "0";
    }
    return ans;
    }

};