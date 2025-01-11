#include <vector>
#include <stack>

class Solution {
public:
    int evalRPN(vector<str>& tokens) {
        std::stack<int> stack;
        for(const string&token : tokens){
            if (token == "+"){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b + a);
            }
            else if (token == "-"){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b - a)
            }
            else if (token == "*"){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b * a);
            }
            else if (token == "/"){
                a = stack.pop();
                b = stack.pop();
                stack.push(b/a);
            }
        }
    }
};