import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();
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
                list.add(nums[j]);
            }
        }
        return list;
    }
}