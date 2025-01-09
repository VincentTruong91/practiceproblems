//use hashmap and stack
//Time complexity -> O(n)
//Space complexity -> O(n)
#include <unordered_map>
class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char,char> hashmap = 
        {
            { '}', '{' },
            { ')', '(' },
            { ']', '[' }
        };
        std::stack<int> stack;

        for(char c : s) {
            if (hashmap.count(c)) {
                if(!stack.empty() && stack.top() == hashmap[c]){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
            //this means that it's an open character
            stack.push(c);                
            }
        }
        return stack.empty();
    }
};
