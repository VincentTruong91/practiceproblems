//stack
//time complexity -> O(n)
//Space complexity -> O(n)
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<pair<int, int>> stack; //pair: {temp, index}
        vector<int> result(temperatures.size(), 0);

        for(int i = 0; i < temperatures.size(); i++){
            int temp = temperatures[i];
            while(!stack.empty() && temp > stack.top().first){
                auto pair = stack.top();
                stack.pop(); //pop the pair
                result[pair.second] = i - pair.second;
            }
            stack.push({temp, i});
        }
        return result;

    }
};