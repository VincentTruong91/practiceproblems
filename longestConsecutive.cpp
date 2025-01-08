//hashset
//time complexity -> O(n) due to using for loop + while loop
//space compelxity -> O(n) due to using hashset
#include <unordered_set>
#include <vector>

using namespace std;
class Solution{
public:
    int longestConsecutive(vector<int>& nums){
        unordered_set<int> hashSet(nums.begin(), nums.end());
        int longest = 0;
        for(int num : hashSet){
            if (hashSet.find(num-1) == hashSet.end()){
                int length = 1;
                while(hashSet.find(num+length) != hashSet.end()){
                    length++;
                }
                longest = max(length,longest);
            }
        }
        return longest;
    }
};
///////////////////////////////////////////////////////
///////////////////////////////////////////////////////