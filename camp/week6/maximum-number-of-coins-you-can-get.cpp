class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end(), greater<>());
        int sum = 0;
        for(int i = 1; i<2*piles.size()/3; i+=2){
            sum+=piles[i];
        }
        return sum;
    }
};