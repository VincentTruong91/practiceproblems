//stack
//time complexity = O(n) because we use a for each loop
//space complexity = O(n) because we use a stack in memory as the data structure

#include <vector>
#include <stack>

std::stack<int> stack;
        for(const string&token : tokens){
            if (token == "+"){
                int a = stack.top();
                stack.pop(); // a should first be assigned to the top of the stack, and then it should be removed
                int b = stack.top();
                stack.pop(); //same goes for b, assign b as the top of the stack, then remove the top element of the stack
                stack.push(b + a);
            }
            else if (token == "-"){
                int a = stack.top()
                stack.pop();
                int b = stack.top()
                stack.pop();
                stack.push(b - a)
            }
            else if (token == "*"){
                int a = stack.top()
                stack.pop();
                int b = stack.top()
                stack.pop();
                stack.push(b * a);
            }
            else if (token == "/"){
                a = stack.top()
                stack.pop();
                b = stack.top()
                stack.pop();
                stack.push(b/a);
            }
            else{
                stack.push(stoi(int)); //stoi (string to integer)
            }
        }