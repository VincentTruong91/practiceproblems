//sliding window/ two pointer
//time complexity -> O(n)
//space complexity -> O(1)
class Solution{
public:
    int maxProfit(vector<int>& profits){
        int l = 0;
        int r = 1;
        int maxProfit = 0;

        while (r < len(profits)){
            if (profits[l] < profits[r]){
                profit = profits[r] - profits[l];
                maxProfit = max(maxProfit, profit);
            }
            else{
                l = r;
            }   
            r++;
        }
    }
}