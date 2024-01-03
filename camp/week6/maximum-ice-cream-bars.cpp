class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int len = coins, mx = 0;
        unordered_map<int, int> m;
        for(int i : costs){
            m[i]++;
            mx = max(mx, i);
        }
        int count=0, i = 0; 
        while(i<=mx && coins > 0){
            if(m[i]){
                //cout<<i<<", "<<m[i]<<", "<<coins<<", "<<count<<endl;
                while(coins>=i && m[i]>0){
                    coins-=i;
                    count++;
                    m[i]--;
                }
            }
            i++;
        }
        return count;
    }
};