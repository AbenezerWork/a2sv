class Solution {
public:
    long long smallestNumber(long long num) {
        if(!num)return 0;
        long long sign = num/abs(num);
        string n = to_string(abs(num));
        if(sign<0){
            sort(n.begin(), n.end(), greater<>());
            return -1*stoll(n);
        }else{
            sort(n.begin(),n.end());
            int i = 0;
            for (; i<n.size(); i++){
                if(n[i] != '0'){
                    break;
                }
            }
            swap(n[0], n[i]);
            return (stoll(n));
        }
        return 0;
    }
};