class Solution {
    struct obj : Hashable {
       let n: Int
        let first: Bool
    }

    func rob(_ nums: [Int]) -> Int {
        var dict: [obj: Int] = [:]
        func brute(_ n: Int, _ first: Bool) -> Int {
            let curr = obj(n: n, first: first)
            if let val = dict[curr] {
                return val
            }
            if nums.count == 1 {
                return nums[0]
            }
            if n >= nums.count {
                return 0
            }
            if first && n == nums.count - 1 {
                return 0
            }
            
            var result: Int
            if n == 0 {
                // Choice 1: Rob the first house (mark first = true)
                // Choice 2: Skip the first house (mark first = false)
                result = max(nums[0] + brute(2, true), brute(1, false))
            } else {
                result = max(nums[n] + brute(n + 2, first), brute(n + 1, first))
            }
            
            dict[curr] = result
            return result
        }
        
        return brute(0, false)
    }
}
