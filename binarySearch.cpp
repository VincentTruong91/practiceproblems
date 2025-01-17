class Solution{
public:
    int binarySearch(vector<int> nums, int target){
        l = 0;
        r = nums.size() - 1;

        while (l <= r){
            //m = (l + r) / 2; //this might cause an overflow 2^32 if nums is large
            m = l - ((r - l) / 2) //use this to solve overflow
            if(nums[m] < target){
                l = m + 1;
            }
            else if(nums[m] > target){
                r = m - 1;
            }
            else{ //we found our solution
                return m;
            }
        }
        return -1;
    }
};