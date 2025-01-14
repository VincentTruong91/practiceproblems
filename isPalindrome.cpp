//two pointer
//time complexity -> O(n)
//space complexity -> O(1)
class Solution{
public:
    bool isPalindrome(string s){
        pLeft = 0;
        pRight = s.length()-1;

        while(pLeft < pRight){
            
            while(pLeft < pRight && !alphaNum(s[pLeft])){
                pLeft++;
            }

            while(pRight > pLeft && !alphaNum(s[pRight]))

            if(tolower(s[pLeft]) != tolower(s[pRight])){
                return false;
            }
        }
        return true;
    }

    bool alphaNum(char c){
        return ((c >= 'A' && c <= 'Z') ||
        (c >= 0 && c <= 9) ||
        (c >= 'a' && c <= 'z'))
    }
}