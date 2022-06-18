class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] arr = { -1, -1 };
        int startIndex = findIndex(target, nums, true);
        arr[0] = startIndex;
        int endIndex = findIndex(target, nums, false);
        arr[1] = endIndex;
        return arr;

    }

    public int findIndex(int target, int[] nums, boolean sIndex) {
        int start = 0;
        int end = nums.length - 1;
        int ans = -1;
        int mid = 0;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (target < nums[mid]) {
                end = mid - 1;
            } else if (target > nums[mid]) {
                start = mid + 1;
            } else {
                ans = mid;
                if (sIndex) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
        }
        return ans;
    }
}