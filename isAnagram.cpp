class isAnagram
{
    public:
    bool isAnagram(string s, string t)
    {
        if s.length() == t.length()
        {
            return false; //theres no way that both strings are anagrams of each other if there are unequal in length
        }

        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        //because they are the same length, we can use either one of the strings to itterate over
        for(int i = 0; i < s.length(); i++)
        {
            sMap[s[i]]++; //adds whatever char at s[i] into the unordered map
            tMap[t[i]]++;
        }
        return sMap == tMap; //return if the maps are the same (listing of chars)
    }
}