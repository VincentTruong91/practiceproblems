//Using hashset
//Time Complexity -> O(n) because we are using a for each loop
//Space Complexity -> O(n) in memory bc we are storing values in an unordered set
#include <vector>
using namespace std; // not use std::
//We don't use an unordered_map because it stores key-value pairs, but we can use unordered_set to check for the unique key's existence.
class Solution {
    bool hasDuplicate(vector<int>& nums){
        unordered_set<int> checkedAlready; //would've been std::unordered_set<int> but is not because of using namespace std;
        for(num : nums){
            if(checkedAlready.count(num)) {
                return true;
            }
            checkAlready.insert(num);
        }
        return false;
    }
}

/////////////////////////////////////////////////////
/////////////////////////////////////////////////////

//Brute force
//Time Comp. -> O(n^2) bc uses 2 for loops nested
//Space Comp. -> O(1) bc it doesn't initialize any arr, and only returns true/false
#include <vector>
class Solution {
public:
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
};

/////////////////////////////////////////////////////
/////////////////////////////////////////////////////

//Use Sorting Algorithm
//Time Complexity -> O(nlogn) bc we are using a sorting alorithm
//Space Complexity -> O(1) in memory bc we aren't using any other data structures
#include <vector>
#include <algorithm>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums){
        std::sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size()-1; i++) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }
};