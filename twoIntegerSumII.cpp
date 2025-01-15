//two pointer
//time complexity -> O(n) uses while loop
//space complexity -> O(1) we used two pointer and doesn't use any extra memory
class Solution{
public:
    vector<int> twoSum(vector<int>& numbers, int target){
        int l = 0;
        int r = numbers.size()-1;
        while (l < r){
            if(numbers[l] + numbers[r] == target){
                return {l + 1, r + 1};
            }
            else if (numbers[l] + numbers[r] > target){
                r--;
            }
            else{ // two values from pointers are less than target
                l++;
            }
        }
    }
};

///////////////////////////////////////////////
///////////////////////////////////////////////
//hashmap
//Time complexity -> O(n) due to using for loop
//space complexity -> O(n) in memory because unordered map uses memory, uses data structure
#include <unordered_map>
class Solution{
    vector<int> twoSum(vector<int>& numbers, int target){
        std::unordered_map<int, int> hashmap;
        for(int i = 0; i < numbers.size(); i++){
            temp = target - numbers[i];
            if(hashmap.count(temp)){
                return {hashmap[temp] + 1, numbers[i] + 1}
            }
            hashmap[numbers[i]] = i;
        }
    }
}

