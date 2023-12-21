class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if (digits.back() == 9){
            int i = digits.size()-1;
            while (i>=0 && digits[i] == 9 ){
                digits[i] = 0;
                i--;
            }
            cout<<i;
            if(i==-1){
                digits[0]=1;
                digits.push_back(0);
            }else{
                digits[i]++;
            }
        }else
        digits[digits.size()-1]++;
        return digits;
    }
};