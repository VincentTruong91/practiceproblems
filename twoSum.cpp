class twoSum{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int,int> discovered;
        for (int i = 0; i < nums.size(); i++)
        {
            int difference = target - nums[i];

            if(discovered.find(difference) != discovered.end()) 
            { 
                //if the key itterator doesn't reach to the end (finds difference as key)
                return [discorvered[i], i];
            }
            discovered.insert({nums[i], i});
        }
        return {};
    }
}