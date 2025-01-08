//HashSet
//Time complexity -> O(n^2)
//Space Complexity -> O(n^2)
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <map> //unordered_map or map can be used for storing sets of values for the squares (map = sorted, unordered_map = not-sorted)
using namespace std;

class Solution{
    bool isValidSudoku(vector<vector<char>>& board){
        unordered_map<int, unordered_set<char>> rows, cols;
        map<pair<int,int>, unordered_set<char>> squares;

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                if (board[r][c] == '.'){
                    continue;
                }

                pair<int,int> squareKey = {r/3, c/3};

                if(rows[r].count(board[r][c]) ||
                cols[c].count(board[r][c]) ||
                squares[squareKey].count(board[r][c])){
                    return false;
                }

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[squareKey].insert(board[r][c]);
            }
        }
        return true;
    }
};