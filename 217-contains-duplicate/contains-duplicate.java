class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Bruteforce: 
        // Create nested loops, the outer loop would store the digit that we want to find the duplicate and the inner loop would be to find the same digit as the digit stored in the outer loop. Time Complexity would be O(n^2)

        // Better Solution:
        // Iterate only once, while iterating, store the digit into a hashmap or set if there is no occurence of that digit yet, but if there is occurence, means the digit appears twice
        HashSet<Integer> setOfNum = new HashSet<>();

        for (int num : nums) {
            if (setOfNum.contains(num)) {
                return true;
            }

            setOfNum.add(num);
        }

        return false;
    }
}