class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] result = new int[2];
        int i = 0;
        while (i < nums.length) {
            if (nums[i] != nums[nums[i] - 1]) {
                int temp = nums[i];
                nums[i] = nums[nums[i] - 1];
                nums[temp - 1] = temp;
            } else {
                i += 1;
            }
        }
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j + 1) {
                result[0] = nums[j];
                result[1] = j + 1;
            }
        }
        return result;

    }
}