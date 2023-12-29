class Solution {
public:
    string sortSentence(string s) {
        unordered_map<int, string> m;
        string curr;
        for(int i = 0; i< s.size(); i++){
            if (isdigit(s[i])){
                m[s[i]]=curr;
            }else if(s[i]==' '){
                curr = "";
            }else{
                curr.push_back(s[i]);
            }
        }
        string ans;
        for(int i = '1'; i<='9'; i++){
            if(m[i].size()){
                ans.append(m[i]+" ");
            }
        }
        return ans.substr(0,ans.size()-1);
    }
};