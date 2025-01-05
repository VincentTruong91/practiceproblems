// Hashmap
//Time Complexity -> O(n) uses a for loop
//Space Complexity -> O(n) uses an unordered_map (hashmap)

using namespace std;

class Solution {
    bool isAnagram(string s, string t){
        if (s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> mapS;
        unordered_map<char, int> mapT;

        for(int i = 0; i < s.length(); i++){
            mapS[s[i]]++;
            mapT[t[i]]++;
        }

        return mapS == mapT;
    }
}

/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////

//Sorted way
//Time Complexity -> O(nlogn) because we are using the sort algorithm
//Space Complexity -> O(1)

#include <algorithm>
class Solution{
    bool isAnagram(string s, string t){
        if (s.length() != t.length()){
            return false;
        }

        return sort(s.begin(), s.end()) == sort(t.begin(), t.end())
    }
}