# https://leetcode.com/problems/combination-sum/description/
class Solution {
    public List<List<Integer>> res = new ArrayList<>();
    public void helper(int idx, int[] ar, int target, ArrayList<Integer> list) {
        
        if(idx == ar.length) {
            if(target == 0) res.add(new ArrayList<>(list));
            return;
        }
        
        if(ar[idx] <= target) {
            list.add(ar[idx]);
            helper(idx, ar, target-ar[idx], list);
            list.remove(list.size()-1);
        }
        helper(idx+1, ar, target, list);
        return;

    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        helper(0, candidates, target, new ArrayList<Integer>());
        return res;
    }
}