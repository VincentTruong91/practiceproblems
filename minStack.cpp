class MinStack {
public:
    MinStack(){
        std::stack<int> stack;
        std::stack<int> minStack;
    }
    void push(int val) {
        stack.push(val);
        val = std::min(val, minStack.empty() ? val : minStack.top()) // if it is empty, min of val and minstack, else just val
        minStack.push(val);
    }
    void pop(){
        stack.pop()
        minStack.pop()
    }
    int top(){
        return stack.top()
    }
    int getMin(){
        return minStack.top()
    }
};