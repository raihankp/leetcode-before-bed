class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapNumsIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int targetPair = target - nums[i];
            if (!mapNumsIndex.containsKey(targetPair)) {
                mapNumsIndex.put(nums[i], i);
            } else {
                return new int[] {mapNumsIndex.get(targetPair), i};
            }
        }

        return new int[] {-1};
    }
}