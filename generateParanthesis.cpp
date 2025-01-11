class Solution {
public:
    void backtrack(int numOfOpen, int numOfClosed, int n, vector<string>& result, string& stringPar){
        if(numOfOpen == numOfClosed && numOfOpen == n){
            result.push_back(stringPar);
            return;
        }

        if (numOfOpen < n){
            stringPar += '(';
            backtrack(numOfOpen + 1, numOfClosed, n, result, stringPar);
            stringPar.pop_back();
        }

        if (numOfClosed < numOfOpen){
            stringPar += ")";
            backtrack(numOfOpen, numOfClosed + 1, n, result, stringPar);
            stringPar.pop_back();
        }

    }
    vector<string> generateParenthesis(int n){
        vector<string> result;
        string stringPar;
        backtrack(0,0,n,result, stringPar);
        return result;
    }
}