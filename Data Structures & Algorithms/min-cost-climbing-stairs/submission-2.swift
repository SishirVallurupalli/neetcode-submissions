class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        
        var dict: [Int: Int] = [:]
        func brute(_ curr: Int) -> Int {
            if let val = dict[curr] {
                return val
            }
            
            if curr >= cost.count {
                return 0
            }
            dict[curr] = min(cost[curr] + brute(curr + 1), cost[curr] + brute(curr + 2))
            return dict[curr]!
        }
        return min(brute(0), brute(1))
    }
}
