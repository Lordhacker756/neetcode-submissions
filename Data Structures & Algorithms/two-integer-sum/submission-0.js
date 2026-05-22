class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
      let mp = new Map();

        for(let i=0; i<nums.length; i++){
            let compliment = target - nums[i];
            
            // We have an item which we need to add, to get the target
            if(mp.has(compliment)){
                return [mp.get(compliment), i]
            }

            // Add the item into the map
            mp.set(nums[i], i)
        }
    }
}