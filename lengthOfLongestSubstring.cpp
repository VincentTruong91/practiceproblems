//sliding windown
//time complexity -> O(n) goes through all char in s with for loop
//space complexity -> O(m) unique characters stored in set
#include <unordered_set>
//using namespace std;
class Solution{
public:
    int lengthOfLongestSubstring(string s){
        int l = 0;
        std::unordered_set<char> charSet;
        int res = 0;

        for(int r = 0; r < s.length(); r++){
            while(charSet.find(s[r]) != charSet.end()){
                charSet.erase(s[l]);
                l++;
            }
            charSet.insert(s[r]);
            res = max(res, r-l+1);
        }
        return res;
    }
};