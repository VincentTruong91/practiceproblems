//stack
//time complexity = O(nlogn)
//space complexity O(n)

#import <vector>
#import <stack>
#import <utility> //for pair keyword
class Solution{
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed){
        std::vector<std::pair<int,int>> pair;
        for(int i = 0; i < position.size(), i++){
            pair.push_back({position[i], speed[i]});
        } //populated pairs for car position and speed

        std::sort(pair.rbegin(), pair.rend()); //r is reverse (sort in reverse order)

        std::stack<double> stack;
        //auto tells compiler to deduce type of variable p
        //& p is a reference to each element of container pair
        for(auto& p : pair){
            double time = ((double)(target - p.first)/ p.second); //target-position = distance to target, distance to target / speed = the time to get there
            if (!stack.empty() && time < stack.top()){
                stack.pop()
            }
            //push the current car's time onto stack
            stack.push(time);
        }
        return stack.size() // return number of fleets
    }
}