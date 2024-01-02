class Solution {
public:
    bool isPalindrome(string st) {
        string s = "";
        for( char c : st ){
            if (isalnum(c)){
                if(!isdigit(c)){
                    s+=(tolower(c));
                }else
                s+=(c);
            }
        }
        int n = s.size();
        
        for(int i = 0; i< s.size()/2; i++){
            if(s[i]!= s[n-i-1]){
                return false;
            }
        }

        return true;

    }
};