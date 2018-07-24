/**
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i, j;
        int[] result = new int[2];
        for(i = 0; i < nums.length; i++) {
            for(j = i+1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        result[0] = -1;
        result[1] = -1;
        return result;
    }
}