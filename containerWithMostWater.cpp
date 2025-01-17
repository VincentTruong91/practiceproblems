// two pointer
//time complexity -> O(n)
//space complexity -> O(1)
class Solution{
public:
    int containerWithMostWater(vector<int>& heights){
        int l = 0;
        int r = 0;
        int res = 0;

        while (l < r){
            int heightOfContainer = max(heights[l], heights[r]);
            int widthOfContainer = r - l;
            int waterInContainer = heightOfContainer * widthOfContainer;
            res = max(res, waterInContainer);

            if(l <= r){
                l++;
            }
            else{
                r++;
            }
        }
        return res;
    }
}