//Hashmap solutipn
//Time Complexity -> O(n) used for loop
//Space Complexity -> O(n) used a hashmap/unordered map

//before the compiler processes the actual compiliation, we should includes preprocessor directives
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for(int i = 0; i < nums.size(); i++){
            int need = target - nums[i];
            if(seen.find(need) != seen.find(end)) {
                //if the key itterator doesn't reach to the end
                return {seen[i], i};
            }
            seen.insert({nums[i], i});
        }
        return {};
    }
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

//Brute force strategy
//Time complexity -> O(n^2) nested for loop
//Space complexity -> O(1) no additional data structure used
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target){
        for (int i = 0; i < nums.size(); i++){
            for(int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target){
                    return {nums[i], nums[j]};
                }
            }
        }
        return {};
    }
}