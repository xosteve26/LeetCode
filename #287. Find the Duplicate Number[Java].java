class Solution {
    public int findDuplicate(int[] list) {
        int i = 0;
        while (i < list.length) {
            if (list[i] != list[list[i] - 1] && i < list.length) {
                int temp = list[list[i] - 1];
                list[list[i] - 1] = list[i];
                list[i] = temp;
            } else {
                i += 1;
            }
        }
        for (int j = 0; j < list.length; j++) {
            if (list[j] != j + 1) {
                return list[j];
            }
        }
        return -1;

    }
}