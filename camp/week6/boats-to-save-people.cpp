class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int curr = 0, ans = 0,n = people.size(), i=0,j=n-1;
        while(i<=j){
            curr+=people[i]+people[j];
            if(curr<=limit){
                i++;j--;
                ans++;
                curr=0;
            }else if (curr>limit){
                while(i<j&& curr<limit){
                    curr+=people[i];
                }
                ans ++;
                curr=0;
                j--;
            }
        }
        return curr?ans+1:ans;
    }
};