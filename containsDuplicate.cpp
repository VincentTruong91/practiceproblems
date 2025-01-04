//Using hashset
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};

//Brute force
//Time Comp. -> O(n^2) bc uses 2 for loops nested
//Space Comp. -> O(1) bc it doesn't initialize any arr, and only returns true/false
class Solution {
    bool hasDuplicate(vector<int>& nums) {
        for(int i =0; i < nums.size(); i++){
            for(int j = i + 1; j < nums.size(); j++){
                if (nums[i] == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}