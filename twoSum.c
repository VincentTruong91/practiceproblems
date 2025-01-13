// nested for loop
//Time complexity -> O(n^2) used nested for loop
// Space complexity -> O(1) memory because only storing 2 values
#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    for(int i = 0; i < numSize; i++){
        for(int j = i + 1; j < numSize; j++){
            if (nums[i] + nums[j] == target){
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

////////////////////////////////////////////////
//////////////////////////////////////////////////

