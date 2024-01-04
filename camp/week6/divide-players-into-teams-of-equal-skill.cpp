class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        long long chem=skill.front()+skill.back();
        int n = skill.size();
        long long s = 0;
        for(int i = 0; i<n/2; i++){
            if(skill[i]+skill[n-i-1]!=chem){
                return -1;
            }
            s+=skill[i]*skill[n-i-1];
        }
        return s;
    }
};