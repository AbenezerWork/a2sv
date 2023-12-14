class Solution {
public:
    string reverseWords(string s) {
        int wordCount=1;
        for(char i : s){
            if (i==' '){
                wordCount++;
            }
        }
        int onWord=0;
        string words[wordCount];
        for(int i=0; i<s.size(); i++){
            if (s[i]==' '){
                onWord++;
                cout<<onWord<<endl;
            }else{
                words[onWord].push_back(s[i]);
                cout<<words[onWord];
            }
            
        }
        string answer = "";
        for (int i=wordCount-1;i>=0;i--){
            if(words[i]==""){
                cout<<"hi"<<words[0]<<"hi"<<endl;
                continue;
            }else{
                answer+=words[i];
            }
            if(words[i]!=""){
                answer+=" ";
            }
        }
        answer.pop_back();
        return answer;
    }
};